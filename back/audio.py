from pydub import AudioSegment

def func_trim_volume(var_srcpath, var_output, var_start_sec, var_end_sec, var_volume_db):
    var_audio = AudioSegment.from_file(var_srcpath)
    var_start = (int(var_start_sec)*1000)
    var_end = (int(var_end_sec)*1000)
    var_audio = var_audio[var_start:var_end]
    var_audio = var_audio + var_volume_db
    var_audio.export(var_output, format = "wav")
    return var_output


if __name__ == "__main__":
    func_trim_volume("audio_upload/Dist-Thins-Out.wav", "audio_upload/tekken_cut.wav", "0", "17", +5)