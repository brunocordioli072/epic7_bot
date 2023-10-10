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

const items: MenuItem[] = [
    getItem('Shop', 'shop', <ShoppingOutlined />),
    getItem('Hunt', 'hunt', <RocketOutlined />),
    getItem('Arena', 'arena', <BorderlessTableOutlined />),
    getItem('Daily', 'daily', <RetweetOutlined />),
];


const AppSider: React.FC = () => {
    const [collapsed, setCollapsed] = useState(false);
    const { setCommand, setLogs } = useAppContext()

    function handleSelect(key: string) {
        setCommand(key)
        setLogs([])
    }

    return (
        <Sider collapsed={collapsed} onCollapse={(value) => setCollapsed(value)}>
            <div className="demo-logo-vertical" />
            <Menu theme="dark" onSelect={(e) => handleSelect(e.key)} defaultSelectedKeys={['shop']} mode="inline" items={items} />
        </Sider>
    )
}

export default AppSider