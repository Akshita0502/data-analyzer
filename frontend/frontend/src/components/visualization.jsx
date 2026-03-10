import { useState } from "react";

function Visualization(){

const [charts, setCharts] = useState([]);

const generateCharts = async () => {

    const res = await fetch("https://data-analyzer-backend-eas4.onrender.com/visualization");
    const data = await res.json();

    setCharts(data.charts);
};

return(
<div>

<div className="action-buttons">
<button onClick={generateCharts}>
Generate Charts
</button>
</div>

<div className="chart-container">

{charts.map((chart,index)=>(
    <img
        key={index}
        src={`https://data-analyzer-backend-eas4.onrender.com/charts/${chart}`}
        alt="chart"
        width="300"
    />
))}

</div>

</div>
);
}

export default Visualization;