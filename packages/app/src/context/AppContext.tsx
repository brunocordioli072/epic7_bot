import React, { useContext, useState } from "react";

interface AppContextInterface {
    commands: any[]
    setCommands: React.Dispatch<React.SetStateAction<any[]>>
    command: any
    setCommand: React.Dispatch<React.SetStateAction<any>>
    logs: JSX.Element[]
    setLogs: React.Dispatch<React.SetStateAction<JSX.Element[]>>
}

export const AppContext = React.createContext<AppContextInterface>({
    commands: [],
    setCommands: () => { },
    command: {},
    setCommand: () => { },
    logs: [],
    setLogs: () => { },
});

export const AppProvider = ({ children }: { children: any }) => {
    const [commands, setCommands] = useState<any[]>([])
    const [command, setCommand] = useState({})
    const [logs, setLogs] = useState<JSX.Element[]>([])

    return (
        <AppContext.Provider value={{ commands, setCommands, command, setCommand, logs, setLogs }}>
            {children}
        </AppContext.Provider>
    )
}

export const useAppContext = () => useContext(AppContext);