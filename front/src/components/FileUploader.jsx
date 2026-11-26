import {useState, useEffect} from 'react'
import './themes.css'

export default function FileUploader({SetScreen, SetFileName}) {
    const [Status , setStatus] = useState('')
    const [File , setFile] = useState(null)
    useEffect(() => {
        fetch('http://localhost:8000/ping')
            .then(response => response.json())
            .then(data => {
                if (data.key_status === 200) {
                    setStatus("Online")
                } else {
                    setStatus("Offline")
                }
            })
            .catch(() => {
                setStatus("Offline")
            })
    }, [])
    function handleUpload(){
        if (File) {
            const formData = new FormData()
            formData.append('arg_file', File)
            fetch('http://localhost:8000/audio_upload', {
                method: 'POST', body: formData
            })
            .then(response => response.json())
            .then(data => {
                SetFileName(data.key_name)
                SetScreen('FileProcessing')
            })
            .catch(() => {
                setStatus("Offline")
            })
        }
        
    }    
    return(
        <>
        <div>
            <p>Server Status: {Status}</p>
            <input
                type="file"
                accept="audio/*"
                onChange={(event) => setFile(event.target.files[0])}
            />
            <button onClick={handleUpload}>Upload</button>
        </div>
        </>
    )
}