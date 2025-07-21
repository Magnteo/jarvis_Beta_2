# Команди які має виконати Джарвіс
import subprocess
import speech_recognition as sr
from gtts import gTTS
import pygame
import os
import time
from datetime import datetime
import random
from Jarvis_command_text import *
from search_us_file import programs_my_pc as pmp
from data_file_user import programs
from return_file_user import *
from exit_program import *
from tasks_manager import task_menu
from Weather import *
from jarvis_audio_module import start_recording_until_stop 
from notepade_bookPhone import (
    load_contacts, 
    handle_contact_commands, 
    phone_txt
)
contacts = load_contacts(phone_txt)
print(programs_my_pc.programs)
def execute_command(command):
        from Jarvis import listen_command, speak

        global contacts
        """
        Відкрити програму
        """

        if command == "відкрий spotify":
            
            if programs["Spotify.exe"] != False:
                os.startfile(get_program(pmp.keys[0]))
            else:
                print("у вас її немає")


        elif command == "відкрий steam":

            if programs["steam.exe"] != False:
                os.startfile(get_program(pmp.keys[3]))
                
            else:
                print("У вас її немає")


        elif any(c in command for c in["відкрий telegram" , "відкрий телеграм"]):#тут не треба or

            if programs["Telegram.exe"] != False:
                os.startfile(get_program(pmp.keys[2]))
            else:
                print("У вас її немає")
        

        elif any(c in command for c in["відкрий visual vtudio" , "відкрий vs" , "відкрий код"]):#тут не треба or

            if programs["Code.exe"] != False:
                os.startfile(get_program(pmp.keys[4]))
            else:
                print("у вас її немає")

        """
        Закрити програму
        """

        if command == "закрий spotify":
            if programs["Spotify.exe"] != False:
                found_file(pmp.keys[0])

            else:
                print("У вас її немає")


        elif command == "закрий steam":
            if programs["steam.exe"] != False:
                found_file(pmp.keys[3])
                
            else:
                print("У вас її немає")
        

        elif any(c in command for c in ["закрий telegram" , "закрий телеграм"]):#тут не треба or
            if programs["Telegram.exe"] != False:
                found_file(pmp.keys[2])
                
            else:
                print("У вас її немає")

        
        elif any(c in command for c in["закрий visual studio" , "закрий vs" , "закрий код"]):#тут не треба or
            if programs["Code.exe"] != False:
                found_file(pmp.keys[3])
                
            else:
                print("У вас її немає")

        """
        інші команди
        """


        if any(c in command for c in ['виключи комп’ютер','виключи пк']):
            confirmation = listen_command()
            os.system("shutdown /s /t 5 ")
        elif any(c in command for c in ['телефона книжка', 'телефона книга']):
            print("Відкрито меню контактів. Введіть команду (або 'вийти'):")
            while True:
                comands = input(">> ").strip().lower()
                if comands == "вийти":
                    print("Вихід з меню контактів")
                    break
                response = handle_contact_commands(comands, contacts, phone_txt)
                if response:
                    print(response)
                else:
                    print("Команда не розпізнана.")
        
        elif any(c in command for c in ["відкрий список задач","список задач","задачі"]):
            task_menu()

        elif any(c in command for c in ["погода","яка погода"]):
            response = requests.get(URL)
            data =response.json()
            if data.get("cod") !=200:
                speak("Не можу отримати погоду зараз.")
            weather_text = format_weather(data)
            print(f"[JARVIS]:{weather_text}")
            speak(weather_text)

        elif "запис" in command:
            start_recording_until_stop()
           

        elif command == 'відкрий блокнот':
            os.system('start notepad')


        elif command == 'відкрий браузер':
            os.startfile('https://www.google.com')
