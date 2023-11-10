import { useState } from 'react';
import { Layout, Menu } from 'antd';
import {
    DesktopOutlined,
    ShoppingOutlined,
    RocketOutlined,
    BorderlessTableOutlined,
    RetweetOutlined,
} from '@ant-design/icons';
import type { MenuProps } from 'antd';
import './AppSider.css'
import { useAppContext } from '../../context/AppContext';

const { Sider } = Layout;

type MenuItem = Required<MenuProps>['items'][number];

function getItem(
    label: React.ReactNode,
    key: React.Key,
    icon?: React.ReactNode,
    children?: MenuItem[],
): MenuItem {
    return {
        key,
        icon,
        children,
        label,
    } as MenuItem;
}

const AppSider: React.FC = () => {
    const [collapsed, setCollapsed] = useState(false);
    const { setCommand, commands, setLogs, setSummary, appVersion } = useAppContext()

    function handleSelect(key: string) {
        setCommand(commands.find(el => el.label === key) as any)
        setLogs([])
        setSummary(null as any)
    }

    return (
        <Sider collapsed={collapsed} onCollapse={(value) => setCollapsed(value)} >
            <Menu theme="dark" onSelect={(e) => handleSelect(e.key)} defaultSelectedKeys={['shop']} mode="inline" items={commands.map(el => {
                return getItem(el.label, el.label, el.icon)
            })} />
            <div className='version'>Version: {appVersion}</div>
        </Sider>
    )
}

export default AppSider