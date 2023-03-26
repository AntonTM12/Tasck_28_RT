"""Действующие данные для авторизации в системе"""
from faker import Faker
import string




"""Фейковые данные для авторизации в системе"""
fake_ru = Faker('ru_RU')
fake_firstname = fake_ru.first_name()
fake_lastname = fake_ru.last_name()
fake_phone = fake_ru.phone_number()
fake = Faker()
fake_password = fake.password()
fake_login = fake.user_name()
fake_email = fake.email()


valid_phone = '+7 951 486-01-02'
valid_login = 'rtkid_1679671456582'
valid_password = 'Jfw-5DG-iH7-jY8'
invalid_ls = '0123456781345'




valid_email = 'mt8gj8x6tuk@bheps.com'
valid_pass_reg = '4(0UnPoZ*c'


def generate_string_rus(n):
    return 'б' * n


def generate_string_en(n):
    return 'x' * n


def english_chars():
    return 'qwertyuiopasdfghjklzxcvbnm'


def russian_chars():
    return 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'


def chinese_chars():    # 20 популярных китайских иероглифов
    return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
    return f'{string.punctuation}'
