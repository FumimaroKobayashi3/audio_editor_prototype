import { useState } from 'react'
import FileUploader from './components/FileUploader.jsx'
import './components/themes.css'
import FileProcessing from './components/FileProcessing.jsx'

function App() {
  const [Screen, SetScreen] = useState('FileUploader')
  const [FileName, SetFileName] = useState('')

  function HandleRenderScreen(){
    if (Screen === 'FileProcessing') {
      return <FileProcessing FileName={FileName} />
    }
    else{
      return <FileUploader SetScreen={SetScreen} SetFileName={SetFileName} />
    }
    
  }
  return (
    <>
      <h1>Audio Editor</h1>
      <h2>Editor of audio easy nightcore and daycore editor and plus reverbing</h2>
      {HandleRenderScreen()}
    </>
  )
}

export default App
