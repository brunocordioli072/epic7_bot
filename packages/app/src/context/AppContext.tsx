import React, { useContext, useState } from "react";
import {
    ShoppingOutlined,
    RocketOutlined,
    BorderlessTableOutlined,
    RetweetOutlined,
} from '@ant-design/icons';

interface Command {
    id: string
    label: string;
    description: string;
    python_command: string;
    table: string
    icon: JSX.Element;
}

interface AppContextInterface {
    commands: Command[]
    setCommands: React.Dispatch<React.SetStateAction<Command[]>>
    command: Command
    setCommand: React.Dispatch<React.SetStateAction<Command>>
    logs: JSX.Element[]
    setLogs: React.Dispatch<React.SetStateAction<JSX.Element[]>>
    summary: JSX.Element
    setSummary: React.Dispatch<React.SetStateAction<JSX.Element>>
    appVersion: string;
    setAppVersion: React.Dispatch<React.SetStateAction<string>>
    fastMode: boolean
    setFastMode: React.Dispatch<React.SetStateAction<boolean>>
    currentScreen: boolean
    setCurrentScreen: React.Dispatch<React.SetStateAction<boolean>>
    devMode: boolean
    setDevMode: React.Dispatch<React.SetStateAction<boolean>>
}

export const AppContext = React.createContext<AppContextInterface>({
    commands: [],
    setCommands: () => { },
    command: {} as any,
    setCommand: () => { },
    logs: [],
    setLogs: () => { },
    summary: null as any,
    setSummary: () => { },
    appVersion: '',
    setAppVersion: () => { },
    fastMode: false,
    setFastMode: () => { },
    currentScreen: false,
    setCurrentScreen: () => { },
    devMode: false,
    setDevMode: () => { },
});

export const AppProvider = ({ children }: { children: any }) => {
    const [commands, setCommands] = useState<Command[]>([
        {
            "id": "shop",
            "label": "Shop",
            "description": "Secret Shop Auto Buy",
            "python_command": "start_shop",
            "table": 'secret_shop',
            "icon": <ShoppingOutlined />,
        },
        {
            "id": "hunt",
            "label": "Hunt",
            "description": "Hunt Auto Battle",
            "python_command": "start_hunt",
            "table": 'hunt',
            "icon": <RocketOutlined />,
        },
        {
            "id": "arena",
            "label": "Arena",
            "description": "Arena NPC Auto Battle",
            "python_command": "start_arena",
            "table": 'arena',
            "icon": <BorderlessTableOutlined />,
        },
        {
            "id": "daily",
            "label": "Daily",
            "description": "Daily Actions",
            "python_command": "start_daily",
            "table": 'daily',
            "icon": <RetweetOutlined />,
        },
    ])
    const [command, setCommand] = useState<Command>(commands.find((el: any) => el.label === "Shop") as any)
    const [logs, setLogs] = useState<JSX.Element[]>([])
    const [summary, setSummary] = useState<JSX.Element>(null as any)
    const [appVersion, setAppVersion] = useState('')
    const [fastMode, setFastMode] = useState(false);
    const [currentScreen, setCurrentScreen] = useState(false);
    const [devMode, setDevMode] = useState(false);

    return (
        <AppContext.Provider value={{
            commands,
            setCommands,
            command,
            setCommand,
            logs,
            setLogs,
            summary,
            setSummary,
            appVersion,
            setAppVersion,
            fastMode,
            setFastMode,
            currentScreen,
            setCurrentScreen,
            devMode,
            setDevMode
        }}>
            {children}
        </AppContext.Provider>
    )
}

export const useAppContext = () => useContext(AppContext);