import { useState } from "react";
function Upload() {
    const [file, setFile] = useState(null);

    const handleUpload = async () => {
        if (!file) {
            alert("no file detected! add a file first.");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        await fetch("https://data-analyzer-backend-eas4.onrender.com/upload", {
            method: "POST",
            body: formData
        });

        alert("upload successfully!");
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