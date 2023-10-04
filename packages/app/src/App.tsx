import React, { useEffect, useRef, useState } from 'react';
import { Breadcrumb, Button, Layout, theme } from 'antd';
import AppSider from './components/AppSider/AppSider'
import './App.css'
import { useAppContext } from './context/AppContext';
const { Content, Footer } = Layout;

const commandProps: any = {
  'shop': {
    label: 'Shop',
    description: 'Secret Shop Auto Buy',
  },
  'hunt': {
    label: 'Hunt',
    description: 'Hunt Auto Battle'
  },
  'arena': {
    label: 'Arena',
    description: 'Arena NPC Auto Battle'
  },
  'daily': {
    label: 'Daily',
    description: 'Daily Actions'
  },
}

const App: React.FC = () => {
  const {
    token: { colorBgContainer },
  } = theme.useToken();
  const [logsInterval, setLogsInterval] = useState(0)
  const { command, logs, setLogs } = useAppContext()
  const [windowSize, setWindowSize] = useState(getWindowSize());

  useEffect(() => {
    function handleWindowResize() {
      setWindowSize(getWindowSize());
    }

    window.addEventListener('resize', handleWindowResize);

    return () => {
      window.removeEventListener('resize', handleWindowResize);
    };
  }, []);

  function getWindowSize() {
    const { innerWidth, innerHeight } = window;
    return { innerWidth, innerHeight };
  }

  async function handleStop() {
    if (!logs.find(el => el.type == "b")) {
      await window.pywebview.api.stopRunningCommand()
      setLogs([...logs, <b>Stopped!</b>])
      clearInterval(logsInterval)
    }
  }

  async function handleStart() {
    await window.pywebview.api['start' + commandProps[command].label]()
    handleLogs()
  }

  function handleLogs() {
    const interval = setInterval(async () => {
      const res: string = await window.pywebview.api.getLogs()
      let logs: any[] = []
      res.split('\n').forEach(el => {
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
            <Breadcrumb.Item>{commandProps[command].label}</Breadcrumb.Item>
            <Breadcrumb.Item>{commandProps[command].description}</Breadcrumb.Item>
          </Breadcrumb>
          <Button onClick={() => handleStart()} style={{ marginRight: 8 }}>
            Start
          </Button>
          <Button onClick={() => handleStop()}>
            Stop
          </Button>
          <div className='logs' style={{ padding: 12, marginTop: 8, minHeight: 360, height: windowSize.innerHeight - 500, background: colorBgContainer }}>
            {...logs}
          </div>
        </Content>
        {/* <Footer style={{ textAlign: 'center' }}>Ant Design ©2023 Created by Ant UED</Footer> */}
      </Layout>
    </Layout>
  );
};

export default App;