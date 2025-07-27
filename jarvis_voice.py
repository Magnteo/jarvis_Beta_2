
import speech_recognition as sr
from gtts import gTTS
import pygame
import os
import time
from rapidfuzz import process
from Jarvis_command_text import dict_respound
r = sr.Recognizer()
r.pause_threshold = 0.5
def correct_command(user_text):
    keys = list(dict_respound.keys())
    best_match = process.extractOne(user_text,keys)
    if best_match:
        cmd , score ,*_ =best_match
        print(f" Найближче: {cmd} (схожість: {score:.1f}%)")
        if score >= 60:
            return cmd
    return None
def speak(text):
    tts = gTTS(text=text, lang='uk')
    tts.save("voice.mp3")
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("voice.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    pygame.quit()
    os.remove("voice.mp3")

def listen_command():
    with sr.Microphone() as source:
        print("Jarvis слухає...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, phrase_time_limit=0)
    try:
        text = r.recognize_google(audio, language="uk-UA").lower()
        print(f"Ти сказав: {text}")
        return text
    except Exception as e:
        print("Не розпізнав:", str(e))
        return ""
