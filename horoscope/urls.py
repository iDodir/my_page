from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')

urlpatterns = [
    path('', views.index),
    path('type/', views.get_all_types),
    path('<my_date:sign_zodiac>/', views.get_my_date_converters),
    path('<int:month>/<int:day>/', views.get_info_about_date),
    path('type/<str:my_type>/', views.get_type, name='types-name'),
    path('<yyyy:sign_zodiac>/', views.get_yyyy_converters),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<my_float:sign_zodiac>/', views.get_my_float_converters),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope-name'),
]
