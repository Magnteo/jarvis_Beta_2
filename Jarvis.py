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
from notepade_bookPhone import (
    load_contacts, 
    handle_contact_commands, 
    phone_txt
)



contacts = load_contacts(phone_txt)
print(programs_my_pc.programs)

jarvis =["джарвіс", "jarvis","асистент"]


r  =sr.Recognizer() # створюєм обєкт та визиваєи метод для визначення данних
r.pause_threshold =0.5 #початок через 0,5с.


# використовує файл mp3 та говорить
def speak(text):
    tts = gTTS(text = text , lang='uk')
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
    time.sleep(0.3)
    os.remove("voice.mp3")





# Команди які має виконати Джарвіс
def execute_command(command):
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
        
        elif command == 'відкрий блокнот':
            os.system('start notepad')


        elif command == 'відкрий браузер':
            os.startfile('https://www.google.com')


# Джарвіс слухає команди
def listen_command():
    with sr.Microphone() as source:
        print("Jarvis слухає...")
        r.adjust_for_ambient_noise(source , duration= 1) #забирає шум
        audio = r.listen(source, phrase_time_limit=0) #получені данні ми записуємо в mp3 дорішку
    try:
        text = r.recognize_google(audio, language="uk-UA").lower() #розпізнає слова з аудіо дорішки на Українській мові та переводить всі символи в нижній реєстер
        print(f"Ти сказав:{text}")
        return text
        
    except Exception as e :
        print("Не розпізнав",str(e))
        return""
    

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