import {useState} from "react"

export default function FileProcessing({SetScreen, FileName}) {
    const [Pitch, setPitch] = useState(0.0)
    const [Speed, setSpeed] = useState(1.0)
    const [ReverbRoom, setReverbRoom] = useState(0.0)
    const [reverbWet, setReverbWet] = useState(0.0)
    const [Result, setResult] = useState('')
    const [isProcessing, setIsProcessing] = useState(false)

    function handleProcess() {
        if (!FileName) return

        setIsProcessing(true)
        fetch('http://localhost:8000/audio_process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                var_filename: FileName,
                var_pitch: Number(Pitch),
                var_speed: Number(Speed),
                var_reverb_room: Number(ReverbRoom),
                var_reverb_wet: Number(reverbWet)
            })
        })
        .then(response => response.json())
        .then(data => {
            setResult(data.key_result_file)
            setIsProcessing(false)
        })
        .catch(() => setIsProcessing(false))
    }

    return (
        <>
            <div>
                <button onClick={() => SetScreen("FileUploader")}>(Back)</button>
            </div>
            <div>
                <h1>FileName: {FileName}</h1>
            </div>
            <div>
                <label>Speed: {Speed}</label>
                <input
                    type="range"
                    min="0.5"
                    max="2.0"
                    step="0.1"
                    value={Speed}
                    onChange={(e) => setSpeed(e.target.value)}
                />

                <label>Pitch: {Pitch}</label>
                <input
                    type="range"
                    min="-12"
                    max="12"
                    step="1"
                    value={Pitch}
                    onChange={(e) => setPitch(e.target.value)}
                />

                <label>Reverb Room: {ReverbRoom}</label>
                <input
                    type="range"
                    min="0"
                    max="1"
                    step="0.05"
                    value={ReverbRoom}
                    onChange={(e) => setReverbRoom(e.target.value)}
                />

                <label>Reverb Wet: {reverbWet}</label>
                <input
                    type="range"
                    min="0"
                    max="1"
                    step="0.05"
                    value={reverbWet}
                    onChange={(e) => setReverbWet(e.target.value)}
                />
            </div>

            <button onClick={handleProcess} disabled={isProcessing}>
                {isProcessing ? 'Processing...' : 'Process'}
            </button>

            {Result && (
                <div>
                    <audio controls src={`http://localhost:8000/audio_download/${Result}`} />
                </div>
            )}
        </>
    )
}