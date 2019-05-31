from re import search


def is_rus_text(text=''):
        template = r'[а-я0-9 .,-_!?<>{}\[\]()]*'
        text = text.lower()  # Приведение текста к одному регистру
        parse = search(template, text)  # Поиск строки по шаблону
        # parse будет искать все вхождения руских букв, цифр и знаков препинания из шаблона
        # если найденный текст совпадает с длиной исходного текста - исходный текст
        return len(text) == parse.end()  # полностью русский

def test1():
        if assert (is_rus_text('Привет') == True):
                print('Тест №1 пройден!')
        else:
                print('Тест №1 не пройден!')
def test2():
        if assert (is_rus_text('Чо как?))0)') == True):
                print('Тест №2 пройден!')
        else:
                print('Тест №2 не пройден!')
def test3():
        if assert (is_rus_text('How do u do?') == False):
                print('Тест №3 пройден!')
        else:
                print('Тест №3 не пройден!')
def test4():
        if assert (is_rus_text('あなたは蓮の花') == False):
                print('Тест №4 пройден!')
        else:
                print('Тест №4 не пройден!')
def test5():
        if assert (is_rus_text(' ') == True):
                print('Тест №5 пройден!')
        else:
                print('Тест №5 не пройден!')
def test6():
        if assert (is_rus_text(r'Люб, лю п0куш\\\ать') == True):
                print('Тест №6 пройден!')
        else:
                print('Тест №6 не пройден!')
