import speech_recognition as sr
from gtts import gTTS
from datetime import datetime
import random
from Jarvis_command_text import *
from Jarvis_fose_command import execute_command  # тут всі голоові команди
from jarvis_voice import speak, listen_command,correct_command


jarvis = ["джарвіс", "jarvis", "асистент"]


def main_loop():
    while True:
        text = listen_command()
        if any(name in text for name in jarvis):

            for name in jarvis:
                text = text.replace(name, "").strip()

            print(f"Команда після активації: {text}")

            found_fraza =  correct_command(text)

            

            if not found_fraza:
                answer_text = random.choice(jarvis_error)
                speak(answer_text)
                continue

            answer_text = dict_respound[found_fraza]
            if answer_text == "replic":
                answer_text = random.choice(ration_jarvis)
            

            elif answer_text == "час":
                now = datetime.now()
                current_time = now.strftime("%H:%M")
                print(f"[JARVIS]:поточний час --- {current_time}")
                answer_text = f"Наданний момент Сер {current_time}"

            speak(answer_text)

            if text:
                execute_command(found_fraza)
