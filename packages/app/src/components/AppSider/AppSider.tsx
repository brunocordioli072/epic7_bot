import { useState } from 'react';
import { Layout, Menu } from 'antd';
import type { MenuProps } from 'antd';
import './AppSider.css'
import { useAppContext } from '../../context/AppContext';

const { Sider } = Layout;

type MenuItem = Required<MenuProps>['items'][number];

function getItem({ label, key, icon, children, disabled }: {
    label: React.ReactNode,
    key: React.Key,
    icon?: React.ReactNode,
    children?: MenuItem[],
    disabled?: boolean
}): MenuItem {
    return {
        key,
        icon,
        children,
        label,
        disabled,
    } as MenuItem;
}

const AppSider: React.FC = () => {
    const [collapsed, setCollapsed] = useState(false);
    const {
        setCommand,
        commands, setLogs,
        setSummary, appVersion,
        setFastMode,
        setCurrentScreen
    } = useAppContext()

    function handleSelect(key: string) {
        setCommand(commands.find(el => el.label === key) as any)
        setLogs([])
        setSummary(null as any)
        setFastMode(false)
        setCurrentScreen(false)
    }

    return (
        <Sider collapsed={collapsed} onCollapse={(value) => setCollapsed(value)} >
            <Menu theme="dark" onSelect={(e) => handleSelect(e.key)} defaultSelectedKeys={['shop']} mode="inline" items={commands.map(el => {
                return getItem({
                    label: el.label,
                    key: el.label,
                    icon: el.icon,
                    disabled: el.disabled
                })
            })} />
            <div className='version'>Version: {appVersion}</div>
        </Sider>
    )
}

export default AppSider