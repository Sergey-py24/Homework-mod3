# пишем письма


def send_email (message, recipient, sender = 'chuva@yandex.ru'):
    a = recipient.find('@') >= 0 and recipient.endswith((".com", ".ru", ".net"))
    b = sender.find('@') >= 0 and sender.endswith((".com", ".ru", ".net"))
    if a == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    if b == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
        return
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        return
    if sender == "chuva@yandex.ru":
         print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'Нестандартный отправитель,письмо отправлено с адреса {sender} на адрес {recipient}')










send_email('You won a million', 'sa@gmail.com')
send_email('С НОВЫМ ГОДОМ!','nik@yandex.ru','ded_moroz@ya.net')
send_email('Выучил уроки?','chuva@yandex.net', 'chuva@yandex.net')
send_email('Go to party!','chuvachoc@ya.net','vika@rambler.usa')