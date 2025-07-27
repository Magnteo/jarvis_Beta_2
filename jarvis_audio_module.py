import os
import sounddevice as sd
import simpleaudio as sa
import numpy as np
from scipy.io.wavfile import write


# Створюємо папку для збереження записів, якщо її немає
recordings_dir = "recordings"
os.makedirs(recordings_dir, exist_ok=True)

samplerate = 44100  # це стандарна частота дискреьтзації

file_counter = 1  # для створення різних імен файлів

existing_files = [
    f
    for f in os.listdir(recordings_dir)
    if f.startswith("recording_") and f.endswith(".wav")
]

file_counter = len(existing_files)


def start_recording_until_stop():
    from Jarvis import listen_command, speak

    global file_counter
    audio_chunks = []
    print("Починаю запис. Скажи 'зупини запис' щоб завершити.")
    speak("Починаю запис. Скажи 'зупини запис' щоб завершити.")

    def callback(indata, frames, time, status):
        if status:
            print(status)
        audio_chunks.append(indata.copy())

    try:
        with sd.InputStream(
            samplerate=samplerate, channels=1, dtype="int16", callback=callback
        ):
            while True:
                command = listen_command()
                if not command:
                    continue
                if "зупинити" in command and "запис" in command:
                    break
    except KeyboardInterrupt:
        speak("Запис перервано вручну.")
        print("Запис перервано вручну.")
        return
    audio_data = np.concatenate(audio_chunks, axis=0)
    filename = f"{recordings_dir}/recording_{file_counter}.wav"
    write(filename, samplerate, audio_data)
    print(f"Запис завершено і збережено: {filename}")
    speak("Запис завершено і збережено.")
    file_counter += 1
