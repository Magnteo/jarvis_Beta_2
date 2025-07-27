import re
import os

phone_txt = "file_txt\\Phone_nambers.txt"


def load_contacts(file):
    return phone_numbers(file)


def phone_numbers(file):
    contacts = {}
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as files:
            for line in files:
                if "," in line:
                    name, phone = line.strip().split(",")
                    contacts[name] = phone
    return contacts


def save_contacts(file, contacts):
    with open(file, "w", encoding="utf-8") as files:
        for name, phone in contacts.items():  # тут .items()
            files.write(f"{name},{phone}\n")


contacts = phone_numbers(phone_txt)


def normalize_phone(phone_number):
    pattern = r"[^\d,+]"
    clean_number = re.sub(pattern, "", phone_number)
    if clean_number.startswith("+"):
        numbers_finished = clean_number
    elif clean_number.startswith("380"):
        numbers_finished = "+" + clean_number
    elif clean_number.startswith("0"):
        numbers_finished = "+38" + clean_number
    else:
        numbers_finished = ""
    return numbers_finished


def add_contact(args, contacts):
    name, phone = args
    phone = normalize_phone(phone)
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    phone = normalize_phone(phone)
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


def show_all(args, contacts):
    if not contacts:
        return "No contacts found"
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()


def handle_contact_commands(text, contacts, file):
    if "додати контакт" in text:
        parts = text.split()
        if len(parts) >= 4:
            name = parts[2]
            phone = parts[3]
            res = add_contact([name, phone], contacts)
            save_contacts(file, contacts)
            return res
        else:
            return "Будь ласка, скажи контакт і номер."

    elif "зміни контакт" in text:
        parts = text.split()
        if len(parts) >= 4:
            name = parts[2]
            phone = parts[3]
            res = change_contact([name, phone], contacts)
            save_contacts(file, contacts)
            return res
        else:
            return "Будь ласка, скажи контакт і новий номер."

    elif "покажи контакт" in text:
        parts = text.split()
        if len(parts) >= 3:
            name = parts[2]
            return show_phone([name], contacts)
        else:
            return "Будь ласка, скажи ім'я контакту."

    elif "покажи всі контакти" in text:
        return show_all([], contacts)

    return None


contacts = load_contacts(phone_txt)
