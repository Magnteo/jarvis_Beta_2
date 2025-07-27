# EN version 
# Project Jarvis

## command :
    
    Magnteo -- Bohdan Holovko 

    Heyzi12 -- Shiyan Maksym

# Magneto contribution (EN):
    Created the file "Jarvis.py" where he built a voice assistant
    and added commands like time, shutdown PC, open notepad, launch Spotify,
    and open browser.

    Created notepade_bookPhone.py which saves a person’s name and phone number,
    and also corrects phone input. For that file, created the file_txt folder
    to store all .txt files.

    Made a new tasks_manager.py file — a task list that allows setting task priorities,
    and added another .txt file for that script.

    Also implemented weather voice reporting:
    created a separate file that fetches real-time weather data using the OpenWeatherMap API,
    extracts temperature, description, humidity, and wind speed,
    and converts everything into speakable text.

    Later, he refactored the project by splitting Jarvis.py into two separate modules:
    Jarvis_fose_command.py — contains system commands like opening programs,
    and jarvis_voice.py — responsible for capturing and processing voice input.

    Developed jarvis_audio_module.py — a module for recording user voice commands.
    It creates a "recordings" folder, listens to voice input, and saves the audio as a .wav file
    until the user says "stop recording". The file names are numbered automatically,
    and all steps are announced using the assistant’s voice.

    Started integrating all assistant modules into one unified structure,
    making the project modular and easier to maintain and expand.
    
    Added modern Microsoft Neural TTS via edge-tts for better speech quality.

    Implemented audio playback with pygame to avoid opening external players.
    Used asynchronous (async/await) approach for smoother speech processing.
    Improved overall user experience — Jarvis now speaks more naturally and without pop-up windows.

# Heyzi12 contribution:
    moved all commands from the file "Jarvis.py" to the file "Jarvis_command_text.py" (to make the code in "Jarvis.py" smaller),
    created the files "programs_my_pc.py" and "search_file.py" to search for a certain file on the computer and create the file "data_file_user.py" with the paths to these files,
    supplemented the file "Jarvis.py" added many new commands such as open Spotify / steam / Telegram / Code and added a check to them whether this file exists on the PC, the path to these files they take in the file "data_file_user.py" also added closing commands for these programs: close Spotify / steam / Telegram / Code several options for closing and opening commands for certain programs were added,
    created "return_file_user.py" it provides the same link to the programs, 
    created "exit_program.py" finds and closes the program and a check,
    created "menu.py" - the main menu of the program,
    created "language.py" - language
    created "start.py" - to run the program in VS,
    created "start_jarvis.bat" - to run the program in the Windows terminal
# Magneto what is planned for the project:

# Heyzi what is planned for the project:

# Required Python Librarie:
    pip install SpeechRecognition
    pip install gTTS
    pip install pygame
    pip install requests
    pip install colorama
    pip install sounddevice
    pip install simpleaudio
    pip install numpy
    pip install scipy
    pip install rapidfuzz
    pip install edge-tts
# UA version
# Проект Jarvis

## Команда :

    Magnteo -- Богдан Головко 
    
    Heyzi12 -- Шиян Максим

# Magneto вклад роботи:
    Створив файл "Jarvis.py", у якому реалізував голосового асистента
    та додав команди: показати час, вимкнути комп’ютер, відкрити блокнот, запустити Spotify,
    відкрити браузер.

    Створив файл notepade_bookPhone.py, який зберігає ім’я людини та її номер телефону,
    а також коригує помилки у введеному номері. Для цього файлу створив папку file_txt
    для зберігання всіх .txt файлів.

    Створив новий файл tasks_manager.py — менеджер задач, який дозволяє встановлювати пріоритети,
    та додав окремий .txt файл для збереження списку задач.

    Також реалізував озвучення погоди:
    створив окремий файл, який отримує актуальні погодні дані через OpenWeatherMap API,
    обробляє температуру, опис, вологість, швидкість вітру
    і перетворює всю інформацію на текст, зручний для озвучення.

    Згодом розділив головний файл Jarvis.py на два окремі модулі:
    Jarvis_fose_command.py — містить команди типу «відкрий блокнот», «вимкни ПК» тощо,
    та jarvis_voice.py — відповідає за прослуховування голосу й обробку команд.

    Створив модуль jarvis_audio_module.py для запису голосу користувача.
    Цей модуль створює папку "recordings", записує звук до команди "зупини запис",
    зберігає його у форматі .wav з автоматичною нумерацією файлів
    та озвучує усі етапи запису через функцію speak().

    Розпочав об’єднання всіх модулів асистента в єдину структуру,
    що зробило проєкт модульним, зручним для підтримки та подальшого розвитку.

    Додав алгоритм нечіткого пошуку (T9) для покращення розпізнавання команд, використовуючи бібліотеку rapidfuzz. Це дозволяє асистенту правильно розпізнавати команди навіть при помилках або неточностях у вимові.

    Додали сучасний голос Microsoft Neural TTS через edge-tts для кращої якості озвучення.
    Реалізували програвання звуку через pygame без відкриття зовнішніх плеєрів.
    Використали асинхронність (async/await) для плавнішої роботи озвучення.
    Покращили загальний користувацький досвід — Jarvis тепер говорить природніше і без зайвих вікон

# Heyzi12 вклад роботи:
    переніс всі команди з файлу "Jarvis.py" в файл  "Jarvis_command_text.py" (Щоб зробити код в "Jarvis.py" меншим) ,
    створив файлм "programs_my_pc.py" і "search_file.py" для того щоб шукати чи є певний файл на компютері та створює файл "data_file_user.py" з шляхои до цих файлів , 
    доповнив файл "Jarvis.py" додав багато нових команд таких як відкрий Spotify / steam / Telegram / Code та до них додав перевірку чи їснує цей файл на пк , шлях до цих файлів вони беруть в файлі "data_file_user.py" також додав закриття цих програм команди : закрий Spotify / steam / Telegram / Code додано було декілька варіантів команд закриття та відкриття пeвних програм , 
    створив "return_file_user.py" він надає те саме посилання на програми , 
    створив "exit_program.py" знаходить та закриває програму є перевірка ,
    створив "menu.py" - головне меню програми ,
    створив "language.py" - мова
    створив "start.py" - щоб програму запускати в VS,
    створив "start_jarvis.bat" - щоб запускати програму в термінал віндовс
# Magneto що заплановано на проєкт:

# Heyzsi що заплановано на проєкт:

# Необхідні Python-бібліотеки:
    pip install SpeechRecognition
    pip install gTTS
    pip install pygame
    pip install requests
    pip install colorama
    pip install sounddevice
    pip install simpleaudio
    pip install numpy
    pip install scipy
    pip install rapidfuzz
    pip install edge-tts
# version 1.0