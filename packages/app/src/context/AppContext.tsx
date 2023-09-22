import React, { useContext, useState } from "react";

interface AppContextInterface {
    command: string
    setCommand: React.Dispatch<React.SetStateAction<string>>
    logs: JSX.Element[]
    setLogs: React.Dispatch<React.SetStateAction<JSX.Element[]>>
}

export const AppContext = React.createContext<AppContextInterface>({
    command: "shop",
    setCommand: () => { },
    logs: [],
    setLogs: () => { },
});

export const AppProvider = ({ children }: { children: any }) => {
    const [command, setCommand] = useState("shop");
    const [logs, setLogs] = useState<JSX.Element[]>([])


    return (
        <AppContext.Provider value={{ command, setCommand, logs, setLogs }}>
            {children}
        </AppContext.Provider>
    )
}

export const useAppContext = () => useContext(AppContext);