import datetime
from slugify import slugify
from transliterate import translit


def ruslugify(smth):
    return slugify(translit(smth, 'ru', reversed=True))


def days_left(y,m,d, with_a_word):
    deadline = datetime.date(y,m,d)
    today = datetime.date.today()
    days_left = str(deadline - today).split(' ')[0]
    if int(days_left[-1])>4 or int(days_left[-1])==0 or 10< int(days_left) <15:
        word = "дней"
        verb = 'осталось'
    elif 1<int(days_left[-1])<5:
        word = "дня"
        verb = 'осталось'
    else:
        word = "день"
        verb = 'остался'
    if with_a_word:
        return (verb + ' ' + days_left + ' ' + word)
    else:
        return days_left
