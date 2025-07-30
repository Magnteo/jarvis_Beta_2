import speech_recognition as sr
from pydub import AudioSegment
import os
import re
recognizer = sr.Recognizer()

def audio_file(file_path):
    try:
        temp_wav = None
        if not file_path.endswith(".wav"):
            sound = AudioSegment.from_file(file_path)
            temp_wav = file_path.rsplit(".", 1)[0] + "_temp.wav"
            sound.export(temp_wav, format="wav")
            wav_path = temp_wav
        else:
            wav_path = file_path

        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language="uk-UA")

        
        clean_txt = re.sub(r'[^а-яА-Яa-zA-Z0-9 ]','',text).lower()
        
        if temp_wav and os.path.exists(temp_wav):
            os.remove(temp_wav)
        return clean_txt 
    except FileNotFoundError:
        return "Файл не знайдено!"
    except sr.UnknownValueError:
        return "Не вдалося розпізнати аудіо"
    except Exception as e:
        return f"Помилка: {e}"
    
print(audio_file(r"Dexter\audio\hello-dexter-morgan.mp3"))