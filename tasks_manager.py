import os
from colorama import init, Fore, Style
init()

file_txt = r"file_txt\task_maneger.txt"

def load_tasks(file):
    tasks=[]
    if os.path.exists(file):
        with open(file,"r",encoding="utf-8") as files:
            lines = files.readlines()
            for read in lines:
                parts =read.strip().split('|')
                if len(parts)==3:
                    cain={
                        "time": parts[0],
                        "priority": parts[1],
                        "text": parts[2]
                    }
                    tasks.append(cain)
        
    else:
        print("файл не знайдено")
    return tasks

def save_tasks(tasks:list, file:str):
    with open(file,"w",encoding="utf-8") as files:
        for task in tasks:
            files.write(f"{task['time']}|{task['priority']}|{task['text']}\n")

def add_task(task:dict,tasks:list,file:str):
    for ts in tasks:
        if ts["text"]==task["text"]:
            return "така задача вже є"
    tasks.append(task)
    save_tasks(tasks , file)
    return"Задача створена"

def edit_task(old_text: str, new_text: str, new_time: str, new_priority: str, tasks: list, file: str):
    for task in tasks:
        if task["text"] == old_text:
            task["text"] = new_text
            task["time"] = new_time
            task["priority"] = new_priority
            save_tasks(tasks, file)
            return "Задачу оновлено"
    return "Задача не знайдена"

def delet_task(text_to_delete,tasks, file ):
    for index, task in enumerate(tasks):
        if task["text"] == text_to_delete:
            del tasks[index]
            save_tasks(tasks,file)
            return "Задача видалена"
    return"Задача не знайдена"

def clear_task(tasks:list,file:str):
    tasks.clear()
    save_tasks(tasks,file)
    return "Всі задачі видалені"

def priority_key(task):
    property_val=0 if task['priority'] =="важлива" else 1
    if task['time'] =="Немає обмежень":
        time_val="99:99"
    else:
        time_val=task['time']
    return(property_val,time_val)


def print_task(tasks):
    for task in tasks:
        color = Fore.RED if task['priority']=='важлива' else Fore.GREEN
        time_str =f"До {task['time']}" if task['time'] !="Немає обмежень" else "Немає обмежень"
        print(f"{color}{time_str}({task['priority']})-{task['text']}{Style.RESET_ALL}")
#Знизу копіпаст чата гпт
def input_priority():
    while True:
        p = input("Пріоритет (важлива/неважлива): ").strip().lower()
        if p in ["важлива", "неважлива"]:
            return p
        print("Неправильний пріоритет. Спробуйте знову.")

def task_menu():
    tasks = load_tasks(file_txt)
    print("Відкрито меню задач. Введіть команду (або 'вийти'):")

    while True:
        command = input(">> ").strip().lower()

        if command == "вийти":
            print("Вихід з меню задач.")
            break
        elif command == "додати":
            text = input("Введіть текст задачі: ").strip()
            time = input("До якого часу? (або 'Немає обмежень'): ").strip()
            priority = input_priority()
            task = {"text": text, "time": time, "priority": priority}
            print(add_task(task, tasks, file_txt))
        elif command == "редагувати":
            old_text = input("Введіть текст задачі, яку хочете змінити: ").strip()
            new_text = input("Новий текст задачі: ").strip()
            new_time = input("Новий час (або 'Немає обмежень'): ").strip()
            new_priority = input_priority()
            print(edit_task(old_text, new_text, new_time, new_priority, tasks, file_txt))
        elif command == "видалити":
            text_to_delete = input("Введіть текст задачі, яку хочете видалити: ").strip()
            print(delet_task(text_to_delete, tasks, file_txt))
        elif command == "очистити":
            confirm = input("Ви впевнені, що хочете видалити всі задачі? (так/ні): ").strip().lower()
            if confirm == "так":
                print(clear_task(tasks, file_txt))
            else:
                print("Скасовано.")
        elif command == "показати":
            if not tasks:
                print("📭 Немає задач.")
            else:
                print_tasks_sorted(tasks)
        else:
            print("Команда не розпізнана. Спробуйте: додати, редагувати, видалити, очистити, показати, вийти.")

def print_tasks_sorted(tasks):
    # Розділяємо задачі за пріоритетом
    important = [t for t in tasks if t['priority'] == 'важлива']
    others = [t for t in tasks if t['priority'] != 'важлива']

    print("\n📌 Важливі задачі:")
    print("------------------------------------")
    for task in sorted(important, key=priority_key):
        time_str = f"До {task['time']}" if task['time'] != "Немає обмежень" else "Немає обмежень"
        print(f"🔴 {time_str} ({task['priority']}) — {task['text']}")

    print("\n🟢 Інші задачі:")
    print("------------------------------------")
    for task in sorted(others, key=priority_key):
        time_str = f"До {task['time']}" if task['time'] != "Немає обмежень" else "Немає обмежень"
        print(f"🟢 {time_str} ({task['priority']}) — {task['text']}")
