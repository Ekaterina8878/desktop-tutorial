def send_email(message , recipient, sender = 'university.help@gmail.com'):

    def valid (email):
        return('@' in email) and (email.endswith(('.com', '.ru', '.net')))
    if not valid (sender) or not valid (recipient):
        print(f'Невозможно отправить письмо с адресата {sender} на адрес {recipient}')
        return
    if sender == recipient:
        print('Нельзя отправить письмо самому себе! ')
        return
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса <sender> на адрес <recipient>')
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')







