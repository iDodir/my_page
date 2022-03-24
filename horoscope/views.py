from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

types = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'libra', 'pisces'],
}


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    data = {
        'description': description,
        'sign': sign_zodiac,
        'zodiacs': zodiac_dict,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)


def index(request):
    zodiacs = list(zodiac_dict)
    context = {
        'zodiacs': zodiacs,
        'zodiac_dict': {},
    }
    return render(request, 'horoscope/index.html', context=context)


def get_all_types(request):
    response = '<ul>'
    for my_type in list(types):
        redirect_path = reverse('types-name', args=[my_type])
        response += f"<li><a href='{redirect_path}'>{my_type.title()}</a></li>"
    response += '</ul>'
    return HttpResponse(response)


def get_type(request, my_type: str):
    response = '<ul>'
    for item in types[my_type]:
        redirect_path = reverse('horoscope-name', args=[item])
        response += f"<li><a href='{redirect_path}'>{item.title()}</a></li>"
    response += '</ul>'
    return HttpResponse(response)


def day_of_year(month: int, day: int):
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    assert 1 <= month <= 12
    assert 1 <= day <= days_in_months[month - 1]
    result = (sum(days_in_months[:month - 1]) + day - 79 + 365) % 365
    if result:
        return result
    return 365


def get_info_about_date(request, month: int, day: int):
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    assert 1 <= month <= 12
    assert 1 <= day <= days_in_months[month - 1]
    zodiac_days = [31, 62, 93, 124, 154, 187, 217, 247, 277, 306, 336, 365]
    count = 0
    for i in zodiac_days:
        if i < day_of_year(month, day):
            count += 1
    redirect_path = reverse('horoscope-name', args=[count + 1])
    return HttpResponseRedirect(redirect_path)


def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали число из 4х цифр - {sign_zodiac}.')


def get_my_float_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали вещественное число - {sign_zodiac}.')


def get_my_date_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали дату - {sign_zodiac}.')
