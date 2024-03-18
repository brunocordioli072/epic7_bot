import { useEffect, useRef } from "react";
import { useAppContext } from "../../context/AppContext";
import './LogsContainer.css'

const Logs: React.FC = () => {
    const {
        logs,
    } = useAppContext()
    const logsRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        if (logsRef && logsRef.current)
            logsRef.current.scrollIntoView()
    }, []);

    return (
        <div ref={logsRef} className='logs'>
            <div className="title">Logs</div>
            {...logs}
        </div>
    )
}

export default Logs