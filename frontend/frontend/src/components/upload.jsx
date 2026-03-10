import { useState } from "react";
function Upload() {
    const [file, setFile] = useState(null);

    const handleUpload = async () => {

    if (!file) {
        alert("No file detected! Add a file first.");
        return;
    }

    // ✅ check file type
    const validTypes = [
        "text/csv",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    ];

    if (!validTypes.includes(file.type)) {
        alert("Only CSV or XLSX files are allowed!");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("https://data-analyzer-backend-eas4.onrender.com/upload", {
        method: "POST",
        body: formData
    });

    if (res.ok) {
        alert("File uploaded successfully!");
    } else {
        alert("Upload failed! Please upload a valid file.");
    }
};

    return (
        <div className="upload-section">

            <h2 className="heading">Upload Dataset</h2>

            <div className="upload-buttons">

                <label className="choose">
                    Choose File
                    <input
                        type="file" accept = ".csv, .xlsx"
                        className="hidden"
                        onChange={(e) => setFile(e.target.files[0])}
                    />
                </label>

                <button onClick={handleUpload}>
                    Upload
                </button>

            </div>

        </div>
    );
}

export default Upload;