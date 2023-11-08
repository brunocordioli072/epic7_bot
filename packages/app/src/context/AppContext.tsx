import React, { useContext, useState } from "react";
import {
    ShoppingOutlined,
    RocketOutlined,
    BorderlessTableOutlined,
    RetweetOutlined,
} from '@ant-design/icons';

interface Command {
    label: string;
    description: string;
    python_command: string;
    module: string
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
});

export const AppProvider = ({ children }: { children: any }) => {
    const [commands, setCommands] = useState<Command[]>([
        {
            "label": "Shop",
            "description": "Secret Shop Auto Buy",
            "python_command": "start_shop",
            "module": 'secret_shop',
            "icon": <ShoppingOutlined />,
        },
        {
            "label": "Hunt",
            "description": "Hunt Auto Battle",
            "python_command": "start_hunt",
            "module": 'hunt',
            "icon": <RocketOutlined />,
        },
        {
            "label": "Arena",
            "description": "Arena NPC Auto Battle",
            "python_command": "start_arena",
            "module": 'arena',
            "icon": <BorderlessTableOutlined />,
        },
        {
            "label": "Daily",
            "description": "Daily Actions",
            "python_command": "start_daily",
            "module": 'daily',
            "icon": <RetweetOutlined />,
        },
    ])
    const [command, setCommand] = useState<Command>(commands.find((el: any) => el.label === "Shop") as any)
    const [logs, setLogs] = useState<JSX.Element[]>([])
    const [summary, setSummary] = useState<JSX.Element>(null as any)

    return (
        <AppContext.Provider value={{ commands, setCommands, command, setCommand, logs, setLogs, summary, setSummary }}>
            {children}
        </AppContext.Provider>
    )
}

export const useAppContext = () => useContext(AppContext);