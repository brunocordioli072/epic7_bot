import { useEffect, useRef } from "react";
import { useAppContext } from "../../context/AppContext";
import './LogsContainer.css'

const AlwaysScrollToBottom = () => {
    const elementRef = useRef<HTMLDivElement>(null);
    useEffect(() => {
        if (elementRef.current)
            elementRef.current.scrollIntoView({ behavior: 'smooth' })
    });
    return <div ref={elementRef} />;
};


const Logs: React.FC = () => {
    const {
        logs,
    } = useAppContext()

    return (
        <div className='logs'>
            <div className="title">Logs</div>
            {...logs}
            <AlwaysScrollToBottom />
        </div>
    )
}

export default Logs