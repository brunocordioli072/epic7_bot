import { useEffect, useRef } from "react";
import { AppContext } from "../../context/AppContext";
import './LogsContainer.css'
import { useContextSelector } from "use-context-selector";

const AlwaysScrollToBottom = () => {
    const elementRef = useRef<HTMLDivElement>(null);
    useEffect(() => {
        if (elementRef.current)
            elementRef.current.scrollIntoView({ behavior: 'smooth' })
    });
    return <div ref={elementRef} />;
};


const Logs: React.FC = () => {
    const logs = useContextSelector(AppContext, (state) => state.logs);

    return (
        <div className='logs'>
            <div className="title">Logs</div>
            {...logs}
            <AlwaysScrollToBottom />
        </div>
    )
}

export default Logs