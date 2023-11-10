import React, { useEffect, useRef, useState, } from 'react';
import { Breadcrumb, Button, Layout, notification, theme } from 'antd';
import AppSider from './components/AppSider/AppSider'
import './App.css'
import { useAppContext } from './context/AppContext';
const { Content, Footer } = Layout;

const App: React.FC = () => {
  const {
    token: { colorBgContainer },
  } = theme.useToken();
  const [api, contextHolder] = notification.useNotification();
  const [logsInterval, setLogsInterval] = useState(0)
  const { command, logs, setLogs, summary, setSummary, setAppVersion } = useAppContext()
  const [windowSize, setWindowSize] = useState(getWindowSize());

  useEffect(() => {
    function handleWindowResize() {
      setWindowSize(getWindowSize());
    }

    window.addEventListener('resize', handleWindowResize);
    window.addEventListener('pywebviewready', getVersionAndCheckForUpdate);

    return () => {
      window.removeEventListener('resize', handleWindowResize);
      window.removeEventListener('pywebviewready', getVersionAndCheckForUpdate);
    };
  }, []);

  async function getVersionAndCheckForUpdate() {
    const res = await window.pywebview.api.get_version()
    if (res) {
      setAppVersion(res.current_app_version)
      if (res.current_app_version != res.latest_app_version) {
        api.warning({
          message: `Update Available`,
          description: <a href='https://github.com/brunocordioli072/epic7_bot/releases/latest' target='_blank'>Update {res.latest_app_version} available!</a>,
          placement: "topRight",
        });
      }
    }
  }

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

  return (
    <Layout style={{ minHeight: '100vh' }}>
      {contextHolder}
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
          <div id='logs' style={{ padding: 12, marginTop: 8, minHeight: 260, maxHeight: 260, height: windowSize.innerHeight - 1000, background: colorBgContainer }}>
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