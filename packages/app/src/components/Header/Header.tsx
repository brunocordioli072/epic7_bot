import { Breadcrumb, Button, Checkbox, Popconfirm } from "antd"
import { useAppContext } from "../../context/AppContext";
import { useState } from "react";

const Header: React.FC = () => {
    const [logsInterval, setLogsInterval] = useState(0)
    const {
        command,
        logs,
        setLogs,
        setSummary,
        fastMode,
        setFastMode,
        currentScreen,
        setCurrentScreen,
        devMode,
    } = useAppContext()


    async function handleStop() {
        // Ensure it only stops once by checking if <b>Stopped!</b> were already added to logs 
        if (!logs.find(el => el.type == "b")) {
            await window.pywebview.api.stop_running_command()
            setLogs([...logs, <b>Stopped!</b>])
            clearInterval(logsInterval)
        }
    }

    async function handleStart() {
        await window.pywebview.api[command.python_command]({ '--fast': fastMode, '--current': currentScreen })
        createInterval()
    }

    async function handleSummary() {
        const res_stats = await window.pywebview.api.get_summary(command.table)

        switch (command.table) {
            case "secret_shop":
                setSummary(<div style={{ margin: '0' }}>
                    <p>
                        <span style={{ fontWeight: '600' }}>Covenants Bought:</span> {res_stats.covenant_count}
                    </p>
                    <p>
                        <span style={{ fontWeight: '600' }}>Mystics Bought:</span> {res_stats.mystic_count}
                    </p>
                    <p>
                        <span style={{ fontWeight: '600' }}>Refreshes:</span> {res_stats.refreshes_count}
                    </p>
                </div> as any)
                break;
            case "hunt":
                setSummary(<div style={{ margin: '0' }}>
                    <p>
                        <span style={{ fontWeight: '600' }}>Total Rotations:</span> {res_stats.total_rotations}
                    </p>
                </div> as any)
                break;
            default:
                setSummary(<div style={{ margin: '0' }}>
                    <p>
                        <span style={{ fontWeight: '600' }}>No summary developed for {command.label} yet...</span>
                    </p>
                </div> as any)
                break;

        }
    }

    function updateLogsScroll() {
        var element: any = document.getElementById("logs");
        element.scrollTop = element.scrollHeight;
    }

    async function handleLogs() {
        const res_logs: string = await window.pywebview.api.get_logs()
        let logs: any[] = []
        res_logs.split('\n').forEach(el => {
            logs.push(<p>{el}</p>)
        })
        setLogs(logs as any)
        updateLogsScroll()
    }

    function createInterval() {
        const interval = setInterval(async () => {
            await handleLogs()
            await handleSummary()
        }, 500)
        setLogsInterval(interval)
    }


    function handleFastMode() {
        if (fastMode) {
            setFastMode(false)
        }
    }

    function handleCurrentScreen() {
        if (currentScreen) {
            setCurrentScreen(false)
        }
    }


    return (
        <>
            <Breadcrumb style={{ marginBottom: '8px' }}>
                <Breadcrumb.Item>{command.label}</Breadcrumb.Item>
                <Breadcrumb.Item>{command.description}</Breadcrumb.Item>
                {devMode ? <Breadcrumb.Item>Dev Mode</Breadcrumb.Item> : null}
            </Breadcrumb>
            <Button onClick={() => handleStart()} style={{ marginRight: 8 }}>
                Start
            </Button>
            <Button onClick={() => handleStop()}>
                Stop
            </Button>
            {command.id === "shop" && devMode ?
                <Popconfirm
                    overlayStyle={{ maxWidth: "500px" }}
                    title="Are you sure you want to use Fast Mode?"
                    description={<div>
                        <p style={{ margin: 0 }}>Turns on Fast Mode, which makes the each step of the command faster.</p>
                        <p style={{ margin: 0 }}>Warning: It's currently very unstable and requires a high-end PC to work properly.</p>
                    </div>}
                    onConfirm={() => setFastMode(true)}
                    onCancel={() => setFastMode(false)}
                    disabled={fastMode === true}
                    okText="Yes"
                    cancelText="No"
                >
                    <Checkbox checked={fastMode} style={{ paddingLeft: '12px' }} onClick={handleFastMode}>
                        Fast Mode
                    </Checkbox>
                </Popconfirm>
                : null}
            {command.id !== "daily" && devMode ?
                <Popconfirm
                    overlayStyle={{ maxWidth: "500px" }}
                    title="Are you sure you want to use Skip Lobby?"
                    description={<div>
                        <p style={{ margin: 0 }}>Turns on Skip lobby, which skips the first steps of the current command to get to the desired screen of the command. User must perform theses skipped steps manually.</p>
                        <p style={{ margin: 0 }}>Ex: On Shop Command it would skip the steps to click on the bartender and consider that the screen on bluestacks is already on the shop.</p>
                    </div>}
                    onConfirm={() => setCurrentScreen(true)}
                    onCancel={() => setCurrentScreen(false)}
                    disabled={currentScreen === true}
                    okText="Yes"
                    cancelText="No"
                >
                    <Checkbox checked={currentScreen} style={{ paddingLeft: '12px' }} onChange={handleCurrentScreen}>
                        Skip Lobby
                    </Checkbox>
                </Popconfirm>
                : null}
        </>
    )
}

export default Header