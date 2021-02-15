import re
import pytest

testdata = [
    {
        'name': 'Граф Дракула',
        'address': '221B Baker Street',
        'phone': '8-800-535-35-35',
        'birthday': '1500.06.06'
    }
]

@pytest.mark.parametrize('testdata', testdata)
def test_show_contact_exist_not_empty(testdata, capsys):
    try:
        from .precode import Contact
        Contact(**testdata).show_contact()
    except AttributeError:
        assert False, 'Кажется вы забыли написать необходимую функцию'
    except IndentationError:
        assert False, 'Напишите код внутри самой функции'

    captured = capsys.readouterr()
    assert 'Граф Дракула — адрес: 221B Baker Street, телефон: 8-800-535-35-35, день рождения: 1500.06.06' in captured.out 


def test_show_contact_output(output):
    assert 'Создаём новый контакт Михаил Булгаков Создаём новый контакт Владимир Маяковский Михаил Булгаков — адрес: Россия, Москва, Большая Пироговская, дом 35б, кв. 6, телефон: 2-03-27, день рождения: 15.05.1891 Владимир Маяковский — адрес: Россия, Москва, Лубянский проезд, д. 3, кв. 12, телефон: 73-88, день рождения: 19.07.1893' in output


def test_name_func_show_contact(user_code):
    re_pattern = re.compile('def show_contact\(self\):')
    assert re_pattern.findall(user_code), 'Проверьте имя и агрументы написанного метода.'


def test_body_show_contact_minor(user_code):
    re_pattern_name = re.compile('{self.name}')
    re_pattern_address = re.compile('адрес: {self.address}')
    re_pattern_phone = re.compile('телефон: {self.phone}')
    re_pattern_birthday = re.compile('день рождения: {self.birthday}')
    assert re_pattern_name.findall(user_code), 'В прошлой функции print_contact мы выводили имя, давай тут оставим также. '
    assert re_pattern_address.findall(user_code), 'В прошлой функции print_contact мы выводили адрес, давай тут оставим также. '
    assert re_pattern_phone.findall(user_code), 'В прошлой функции print_contact мы выводили номер телефона, давай тут оставим также. '
    assert re_pattern_birthday.findall(user_code), 'В прошлой функции print_contact мы выводили день рождения, давай тут оставим также. '


def test_body_show_contact_major(user_code):
    re_pattern = re.compile('print\(f\"{self.name} — адрес: {self.address}, телефон: {self.phone}, день рождения: {self.birthday}\"\)')
    assert re_pattern.findall(user_code), 'Присмотрись поближе к телу функции. Там что то не так.'
    

def test_print_contact_was_removed(user_code):
    re_pattern_def = re.compile('def print_contact\(\):\n')
    re_pattern_body = re.compile('print\(f\"{(mike|vlad).name} — адрес: {(mike|vlad).address}, телефон: {(mike|vlad).phone}, день рождения: {(mike|vlad).birthday}\"\)')
    assert re_pattern_def.findall(user_code) == [], 'Вы забыли удалить старый код'
    assert re_pattern_body.findall(user_code) == [],  'Вы забыли удалить старый код'

def test_call_method(user_code):
    re_pattern_mike = re.compile('mike.show_contact\(\)')
    re_pattern_vlad = re.compile('vlad.show_contact\(\)')
    assert re_pattern_mike.findall(user_code), 'Вы забыли вызвать наш новый метод у объекта mike'
    assert re_pattern_vlad.findall(user_code), 'Вы забыли вызвать наш новый метод у объекта vlad'
