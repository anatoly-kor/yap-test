
import re
import pytest


def test_cache_args_exist_not_empty():
    try:
        from .precode import cache_args
    except AttributeError:
        assert False, 'Кажется вы забыли написать необходимую функцию'
    except IndentationError:
        assert False, 'Напишите код внутри самой функции'


def test_cache_args_have_dict(user_code):
    re_pattern_dict = re.compile('\w+ = ({}|dict\(\))')
    assert re_pattern_dict.findall(user_code), 'Посмотрите подсказку'

def test_cache_args_return(user_code):
    re_pattern_return = re.compile('return \w+\[\w+\]|return \w+\.get\(.+\)')
    assert re_pattern_return.findall(user_code), 'Возвращать необходимо закешированное значение'

def test_output(output):
    assert 'Время выполнения функции: 1.0 с. 2 Время выполнения функции: 0.0 с. 2 Время выполнения функции: 1.0 с. 4 Время выполнения функции: 0.0 с. 4 Время выполнения функции: 0.0 с. 4' in output
