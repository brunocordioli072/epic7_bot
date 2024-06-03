import React, { useEffect } from 'react';
import { Layout, notification } from 'antd';
import AppSider from './components/AppSider/AppSider';
import './App.css';
import { useAppContext } from './context/AppContext';
import LogsContainer from './components/LogsContainer/LogsContainer';
import StatsContainer from './components/StatsContainer/StatsContainer';
import Header from './components/Header/Header';

const { Content } = Layout;

const App: React.FC = () => {
  const [api, contextHolder] = notification.useNotification();
  const setAppVersion = useAppContext((state) => state.setAppVersion);
  const setCurrentScreen = useAppContext((state) => state.setCurrentScreen);
  const setDevMode = useAppContext((state) => state.setDevMode);
  const setFastMode = useAppContext((state) => state.setFastMode);

  useEffect(() => {
    const handleKeyDownDevMode = (e: KeyboardEvent) => {
      if (e.key === "F1") {
        e.preventDefault();
        setDevMode((val) => !val);
        setCurrentScreen(false);
        setFastMode(false);
      }
    };

    window.addEventListener('pywebviewready', getVersionAndCheckForUpdate);
    window.addEventListener("keydown", handleKeyDownDevMode);

    return () => {
      window.removeEventListener('pywebviewready', getVersionAndCheckForUpdate);
      window.removeEventListener('keydown', handleKeyDownDevMode);
    };
  }, []);

  async function getVersionAndCheckForUpdate() {
    const res = await window.pywebview.api.get_version();
    if (res) {
      setAppVersion(res.current_app_version);
      if (res.current_app_version !== res.latest_app_version) {
        api.warning({
          message: `Update Available`,
          description: <a href='https://github.com/brunocordioli072/epic7_bot/releases/latest' target='_blank'>Update {res.latest_app_version} available!</a>,
          placement: "topRight",
        });
      }
    }
  }

  return (
    <Layout className='layout'>
      {contextHolder}
      <AppSider />
      <Layout>
        <Content className='content'>
          <Header />
          <StatsContainer />
          <LogsContainer />
        </Content>
      </Layout>
    </Layout>
  );
};

export default App;