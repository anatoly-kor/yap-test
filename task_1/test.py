import re
import pytest

def test_make_divider_of_exist_not_empty():
    try:
        from . import precode
    except IndentationError:
        assert False, 'Кажется вы забыли написать код'
    except NameError:
        assert False, 'Лучше не менять название функции "make_divider_of", иначе что будут вызывать следующие функции "print"?'

def test_division_operation_exist_not_empty():
    try:
        from .precode import make_divider_of
        divider = make_divider_of(2)
        divider(10)
    except IndentationError:
        assert False, 'Кажется вы забыли написать код'
    except NameError:
        assert False, 'Если вы поменяли название внутренней функции, то возможно ее же должна возвращать внешняя?'

def test_division_operation_make_division(user_code):
    re_pattern = re.compile('return divisible / divider')
    assert re_pattern.findall(user_code), 'Может стоит делить что-то на что-то?*spoiler alert*'


def test_output(output):
    assert '5.0 4.0 2.0' in output, 'Принты возвращаются какие то неправильные значения.'
