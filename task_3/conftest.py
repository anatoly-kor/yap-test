import subprocess
from pathlib import Path

import pytest

BASE_DIR = Path(__file__).resolve().parent

@pytest.fixture(scope='module')
def user_code():
    with open(BASE_DIR / 'precode.py', 'r') as f:
        return f.read()

@pytest.fixture(scope='module')
def output():
    proc = subprocess.Popen(['python', BASE_DIR / 'precode.py'], stdout=subprocess.PIPE)
    out = proc.communicate()[0].decode('utf-8')
    return ' '.join([i for i in out.split('\n') if i])
