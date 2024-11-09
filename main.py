def send_email(message, recipient, sender="university.help@gmail.com"):
    # Проверка на совпадение адресов
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return

    # Проверка на корректность адресов электронной почты
    if "@" not in sender or not (recipient.endswith(".com") or recipient.endswith(".ru") or recipient.endswith(".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return



    # Проверка для выводимого сообщения
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

# Пример использования функции
send_email("С днём рождения!", "friend@example.com")  
send_email("С днём рождения!", "friend@example.com", sender ="custom.sender@gmail.com")  # Нестандартный отправитель
send_email("С днём рождения!", "friend@example.com", sender ="university.help@gmail.com")  # Стандартный отправитель
send_email("С днём рождения!", "friendexample.com")  # Некорректный адрес получателя
send_email("С днём рождения!", "friend@example.com", sender="custom.sender@gmail.com")  # Нестандартный отправитель
send_email("С днём рождения!", "university.help@gmail.com", sender="un.help@gmail.com")  # Сам себе
