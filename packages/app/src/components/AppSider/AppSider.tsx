import { useState } from 'react';
import { Layout, Menu } from 'antd';
import type { MenuProps } from 'antd';
import './AppSider.css';
import { AppContext } from '../../context/AppContext';
import { useContextSelector } from 'use-context-selector';

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
    const setCommand = useContextSelector(AppContext, (state) => state.setCommand);
    const commands = useContextSelector(AppContext, (state) => state.commands);
    const setLogs = useContextSelector(AppContext, (state) => state.setLogs);
    const setSummary = useContextSelector(AppContext, (state) => state.setSummary);
    const appVersion = useContextSelector(AppContext, (state) => state.appVersion);
    const setFastMode = useContextSelector(AppContext, (state) => state.setFastMode);
    const setCurrentScreen = useContextSelector(AppContext, (state) => state.setCurrentScreen);

    function handleSelect(key: string) {
        setCommand(commands.find(el => el.label === key) as any);
        setLogs([]);
        setSummary(null as any);
        setFastMode(false);
        setCurrentScreen(false);
    }

    return (
        <Sider collapsed={collapsed} onCollapse={(value) => setCollapsed(value)}>
            <Menu
                theme="dark"
                onSelect={(e) => handleSelect(e.key)}
                defaultSelectedKeys={['shop']}
                mode="inline"
                items={commands.map(el => getItem({
                    label: el.label,
                    key: el.label,
                    icon: el.icon,
                    disabled: el.disabled
                }))}
            />
            <div className='version'>Version: {appVersion}</div>
        </Sider>
    );
};

export default AppSider