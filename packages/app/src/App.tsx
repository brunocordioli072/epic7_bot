import React, { useEffect, useRef, useState } from 'react';
import { Breadcrumb, Button, Layout, theme } from 'antd';
import AppSider from './components/AppSider/AppSider'
import './App.css'
import { useAppContext } from './context/AppContext';
const { Content, Footer } = Layout;

const App: React.FC = () => {
  const {
    token: { colorBgContainer },
  } = theme.useToken();
  const [logsInterval, setLogsInterval] = useState(0)
  const { command, setCommands, setCommand, logs, setLogs, summary, setSummary } = useAppContext()
  const [windowSize, setWindowSize] = useState(getWindowSize());

  useEffect(() => {
    function handleWindowResize() {
      setWindowSize(getWindowSize());
    }

    async function handlePywebviewStart() {
      const commands = await window.pywebview.api.get_commands()
      setCommands(commands)
      setCommand(commands.find((el: any) => el.label === "Shop"))
    }

    window.addEventListener('pywebviewready', handlePywebviewStart);
    window.addEventListener('resize', handleWindowResize);

    return () => {
      window.removeEventListener('resize', handleWindowResize);
      window.removeEventListener('pywebviewready', handlePywebviewStart);
    };
  }, []);

  function getWindowSize() {
    const { innerWidth, innerHeight } = window;
    return { innerWidth, innerHeight };
  }

  async function handleStop() {
    // Ensure it only stops once by checking if <b>Stopped!</b> were already added to logs 
    if (!logs.find(el => el.type == "b")) {
      await window.pywebview.api.stop_running_command()
      setLogs([...logs, <b>Stopped!</b>])
      clearInterval(logsInterval)
    }
  }

  async function handleStart() {
    await window.pywebview.api[command.python_command]()
    handleLogs()
  }

  function handleLogs() {
    const interval = setInterval(async () => {
      const res_stats = await window.pywebview.api.get_stats(command.module)
      if (res_stats) {
        if (command.module === "secret_shop") {
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
        }
      }
      const res_logs: string = await window.pywebview.api.get_logs()
      let logs: any[] = []
      res_logs.split('\n').forEach(el => {
        logs.push(<p>{el}</p>)
      })
      setLogs(logs as any)
    }, 500)
    setLogsInterval(interval)
  }

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <AppSider />
      <Layout>
        {/* <Header style={{ padding: 0, background: colorBgContainer }} /> */}
        <Content style={{ margin: '16px 16px' }}>
          <Breadcrumb style={{ marginBottom: '8px' }}>
            <Breadcrumb.Item>{command.label}</Breadcrumb.Item>
            <Breadcrumb.Item>{command.description}</Breadcrumb.Item>
          </Breadcrumb>
          <Button onClick={() => handleStart()} style={{ marginRight: 8 }}>
            Start
          </Button>
          <Button onClick={() => handleStop()}>
            Stop
          </Button>
          <div className='stats' style={{ padding: 12, marginTop: 8, minHeight: 156, background: colorBgContainer }}>
            <div style={{ fontStyle: "italic", fontWeight: "bold", marginBottom: "12px" }}>Summary</div>
            {summary}
          </div>
          <div className='logs' style={{ padding: 12, marginTop: 8, minHeight: 260, height: windowSize.innerHeight - 1000, background: colorBgContainer }}>
            <div style={{ fontStyle: "italic", fontWeight: "bold", marginBottom: "12px" }}>Logs</div>
            {...logs}
          </div>
        </Content>
        {/* <Footer style={{ textAlign: 'center' }}>Ant Design ©2023 Created by Ant UED</Footer> */}
      </Layout>
    </Layout>
  );
};

export default App;