from fastapi import FastAPI, UploadFile, File
from fastapi.responses import RedirectResponse, FileResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import shutil
import audio

var_app = FastAPI()

class ProcessRequest(BaseModel):
    var_filename: str
    var_start_sec: float = 0.0
    var_end_sec: float = 0.0
    var_volume_db: float = 0.0
    var_speed: float = 1.0
    var_pitch: float = 0.0
    var_reverb_room: float = 0.0
    var_reverb_wet: float = 0.0

var_shut = shutil

var_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@var_app.get("/")
def func_launch():
    return RedirectResponse(url="http://localhost:5173")

@var_app.get("/ping")
def func_ping():
    return({ 
        "key_status" : 200,
        "key_cont" : {"key_message": "Online"}
        })

@var_app.post("/audio_upload")
def func_audio_upload(arg_file: UploadFile = File(...)):
    var_file = arg_file
    var_upload = "audio_upload/"
    var_filename = str(var_file.filename)
    var_audioupload = var_upload+var_filename
    with open (var_audioupload, "wb") as var_buffer:
        var_shut.copyfileobj(var_file.file, var_buffer)
    return({
        "key_name": var_filename
    })

@var_app.get("/audio_download/{var_filename}")
def func_get_audio(var_filename: str):
    var_filepath = (f'audio_upload/{var_filename}')
    return FileResponse(var_filepath, media_type = "audio/wav")

@var_app.post("/audio_process")
def func_audioprocess(var_req: ProcessRequest):
    var_src = "audio_upload/" + var_req.var_filename
    var_out_name = "processed_" + var_req.var_filename
    var_dist = "audio_upload/" + var_out_name
    var_step1 = "audio_upload/temp_cut.wav"
    audio.func_manual_night_day(var_src, var_step1, var_req.var_speed, var_req.var_pitch)
    audio.func_manual_night_day(var_step1, var_dist, var_req.var_speed, var_req.var_pitch)
    var_step2 = "audio_upload/temp_speed.wav"
    audio.func_manual_night_day(var_step1, var_step2, var_req.var_speed, var_req.var_pitch)
    audio.func_add_reverb(var_step2, var_dist, var_req.var_reverb_room, var_req.var_reverb_wet)
    return({"key_status": 200, "key_result_file": var_out_name})