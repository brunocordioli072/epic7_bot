import { useContextSelector } from "use-context-selector";
import { AppContext } from "../../context/AppContext";
import './StatsContainer.css'

const StatsContainer: React.FC = () => {
    const summary = useContextSelector(AppContext, (state) => state.summary);

    return (
        <div className='stats'>
            <div className="title">Summary</div>
            {summary}
        </div>
    )
}

export default StatsContainer