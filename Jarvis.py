import speech_recognition as sr
from gtts import gTTS
import pygame
import os
import time
from datetime import datetime
import random
from Jarvis_command_text import *
from Jarvis_fose_command import execute_command # тут всі голоові команди 
from jarvis_voice import speak, listen_command



jarvis =["джарвіс", "jarvis","асистент"]



    

def main_loop():
    while True:
        text = listen_command()
        if any(name in text for name in jarvis):

            for name in jarvis:
                text = text.replace(name,'').strip()

            print(f"Команда після активації: {text}")
            answer_text = ""
            respound_found = False
            found_fraza= ""
            

            for fraza in  dict_respound: 
                if fraza in text: # якщо фраза буде така сама як і текст що сказала людина
                    found_fraza = fraza
                    answer_text = dict_respound[fraza]
                    respound_found = True
                    break
            
            if answer_text =="replic":
                answer_text=random.choice(ration_jarvis)


            if not respound_found:
                answer_text = random.choice(jarvis_error)

            elif answer_text == "час":
                now = datetime.now()
                current_time = now.strftime("%H:%M")
                print(f"[JARVIS]:поточний час --- {current_time}")
                answer_text = f"Наданний момент Сер {current_time}"
            speak(answer_text)
            if text:
                execute_command(text)