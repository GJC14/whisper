import subprocess

def audio_lengh_editor(file_path, start_time, duration, file_name_new): # time format: "00:00:00.000"
    command = ["ffmpeg", "-i", file_path, "-ss", start_time, "-t", duration, file_name_new]   # ffmpeg command
    subprocess.run(command, check=True)  # run ffmpeg command