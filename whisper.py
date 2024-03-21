from dotenv import load_dotenv
from openai import OpenAI
from modules.audio_lengh_editor import audio_lengh_editor

load_dotenv()
client = OpenAI()

###
### Application
###
need_edit = input('Do you need to edit the audio file length? (y/n): ')
if need_edit == 'y' or need_edit == 'Y':
  file_path = input('Enter the file path (e.g.: ./my_voice_memo.m4a): ')
  start_time = input('Enter the start time: ')
  duration = input('Enter the duration: ')
  audio_file = './' + input('Enter the output filename (e.g.: my_voice_memo.mp3): ')
  audio_lengh_editor(file_path, start_time, duration, audio_file)
else:
  # use the relative path, for example file in root directory: ./my_voice_memo.m4a
  audio_file = input('Enter the file path (e.g.: ./my_voice_memo.m4a): ')

###
### Code mode
###
# audio_lengh_editor params (file_path, start_time, duration, output_path)
# audio_lengh_editor("./my_voice_memo.m4a", "00:00:10.000", "00:00:20.000", "./output.mp3")  # from 10s to 30s
# audio_file= open("./output.mp3", "rb")

print('\n***\nStart processing transcript\n***\n')

transcript = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)

open("./transcript", "w").write(transcript.text)
print(transcript.text)
