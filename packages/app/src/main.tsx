import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'

import './index.css'
import { AppProvider } from './context/AppContext.tsx'
import { ConfigProvider } from 'antd';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <ConfigProvider theme={{ cssVar: true }}>
      <AppProvider>
        <App />
      </AppProvider>
    </ConfigProvider>
  </React.StrictMode>,
)
