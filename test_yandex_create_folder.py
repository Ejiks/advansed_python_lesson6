import pytest

from yandex_create_folder import create_folder, list_folder

def test_create_folder():
    assert create_folder('helo word') == 201

def test_list_folder():
    assert list_folder() == {'name': 'helo wolrd'}