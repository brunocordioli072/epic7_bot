import { useAppContext } from "../../context/AppContext";
import './StatsContainer.css'

const StatsContainer: React.FC = () => {
    const {
        summary,
    } = useAppContext()

    return (
        <div className='stats'>
            <div className="title">Summary</div>
            {summary}
        </div>
    )
}

export default StatsContainer