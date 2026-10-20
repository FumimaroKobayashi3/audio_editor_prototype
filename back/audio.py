from pydub import AudioSegment
from pedalboard import Pedalboard, Reverb, time_stretch
from pedalboard.io import AudioFile

def func_trim_volume(var_srcpath, var_output, var_start_sec, var_end_sec, var_volume_db):
    var_audio = AudioSegment.from_file(var_srcpath)
    var_start = (int(var_start_sec)*1000)
    var_end = (int(var_end_sec)*1000)
    var_audio = var_audio[var_start:var_end]
    var_audio = var_audio + var_volume_db
    var_audio.export(var_output, format = "wav")

    return var_output

def func_nightcore_daycore(var_srcpath, var_output, var_speed):
    var_audio = AudioSegment.from_file(var_srcpath)
    var_new_frame_rate = int(var_audio.frame_rate * float(var_speed))
    var_audio = var_audio._spawn(var_audio.raw_data, overrides={'frame_rate': var_new_frame_rate})
    var_audio = var_audio.set_frame_rate(44100)
    var_audio.export(var_output, format="wav")

    return var_output

def func_add_reverb(var_srcpath, var_output, var_room_size, var_wet_level):
    with AudioFile(var_srcpath) as var_reader:
        var_audidata = var_reader.read(var_reader.frames)
        var_samplerate = var_reader.samplerate
        
    var_board = Pedalboard([Reverb(room_size=float(var_room_size), wet_level=float(var_wet_level))])
    var_rev = var_board(var_audidata, var_samplerate)
    
    with AudioFile(var_output, 'w', var_samplerate, var_rev.shape[0]) as var_writer:
        var_writer.write(var_rev)
        
    return var_output
def func_manual_night_day(var_srcpath, var_output, var_speed, var_pitch):
    with AudioFile(var_srcpath) as var_reader:
        var_audio_data = var_reader.read(var_reader.frames)
        var_samplerate = var_reader.samplerate
        var_stretched = time_stretch(var_audio_data, var_samplerate, stretch_factor=float(var_speed), pitch_shift_in_semitones=float(var_pitch))
        
        with AudioFile(var_output, 'w', var_samplerate, var_stretched.shape[0]) as var_writer:
            var_writer.write(var_stretched)

        return var_output

if __name__ == "__main__":
    func_manual_night_day("audio_upload/Dist-Thins-Out.wav", "audio_upload/tekken_stretched.wav", 1.3, 0)