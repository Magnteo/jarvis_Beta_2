
import speech_recognition as sr
import os
from rapidfuzz import process
from Jarvis_command_text import dict_respound
import asyncio
import edge_tts
import tempfile
import pygame
import time
r = sr.Recognizer()
r.pause_threshold = 0.5
def correct_command(user_text):
    keys = list(dict_respound.keys())
    best_match = process.extractOne(user_text,keys)
    if best_match:
        cmd , score ,*_ =best_match
        print(f" Найближче: {cmd} (схожість: {score:.1f}%)")
        if score >= 50:
            return cmd
    return None

VOICE = "uk-UA-OstapNeural"
async def speak_async(text):
    temp_file = os.path.join(tempfile.gettempdir(), "jarvis_voice.mp3")
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(temp_file)
    pygame.mixer.init()
    pygame.mixer.music.load(temp_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pygame.mixer.quit()
    

def speak(text):
    asyncio.run(speak_async(text))

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
