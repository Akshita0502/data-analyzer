import { useState } from "react";

function Analysis() {
  const [data, setDataset] = useState(null);
  const [summary, setSummary] = useState("");

  const getanalysis = async () => {
    try {
      const res = await fetch("http://localhost:8000/analysis");
      const result = await res.json();
      setDataset(result);
    } catch (err) {
      console.error("analysis error!", err);
    }
  };

  const aisummary = async () => {
    try {
      const res = await fetch("http://localhost:8000/ai-summary");

      if (!res.ok) {
        console.error("API error:", res.status);
        return;
      }

      const data = await res.json();
      setSummary(data.summary);
    } catch (err) {
      console.error("summary error!", err);
    }
  };

  return (
    <>
      

      

      {/* ACTION BUTTONS */}
      <div className="page-container">

        <div className="action-buttons">
          <button className="analysis" onClick={getanalysis}>
            Run Analysis
          </button>

          <button className="summary" onClick={aisummary}>
            Get Summary of dataset
          </button>
        </div>

        {/* AI SUMMARY */}
        {summary && (
          <div className="ai-summary-box">
            <h2>AI Summary</h2>
            <p>{summary}</p>
          </div>
        )}

        {/* ANALYSIS RESULT */}
        {data && (
          <div className="analysis-report">

            {/* DATASET COLUMNS */}
            <div className="result-card">
              <h3>Dataset Columns</h3>

              <ul className="columns-list">
                {data.columns.map((col) => (
                  <li key={col}>{col}</li>
                ))}
              </ul>
            </div>

            {/* STATISTICS */}
            <div className="result-card">

              <h3>Statistics</h3>

              <table className="analysis-table">
                <thead>
                  <tr>
                    <th>Column</th>
                    <th>Mean</th>
                    <th>Median</th>
                    <th>Std</th>
                    <th>Min</th>
                    <th>Max</th>
                    <th>Variance</th>
                  </tr>
                </thead>

                <tbody>
                  {Object.keys(data.mean).map((col) => (
                    <tr key={col}>
                      <td>{col}</td>
                      <td>{data.mean[col]}</td>
                      <td>{data.median[col]}</td>
                      <td>{data.std[col]}</td>
                      <td>{data.min[col]}</td>
                      <td>{data.max[col]}</td>
                      <td>{data.variance[col]}</td>
                    </tr>
                  ))}
                </tbody>
              </table>

            </div>

            {/* MISSING VALUES */}
            <div className="result-card">

              <h3>Missing Values</h3>

              {Object.entries(data.missing_percentage).map(([col, val]) => (
                <p key={col}>
                  {col} : {val}%
                </p>
              ))}

            </div>

            {/* CLEANING ACTIONS */}
            <div className="result-card">

              <h3>Cleaning Actions</h3>

              {Object.entries(data.cleaning_actions).map(([col, action]) => (
                <p key={col}>
                  {col} : {action}
                </p>
              ))}

            </div>

          </div>
        )}
      </div>
    </>
  );
}

export default Analysis;