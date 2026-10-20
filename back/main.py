from fastapi import FastAPI, UploadFile, File
from fastapi.responses import RedirectResponse, FileResponse
import shutil

var_app = FastAPI()
var_shut = shutil
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