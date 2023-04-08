# import requires modules
from geopy.geocoders import Nominatim  # Подключаем библиотеку

locations_latitude_and_longitude = []
location_no_duplicates = []
locations_latitude_and_longitude_cinema = []
location_no_duplicates_cinema = []
locations_latitude_and_longitude_restaurant = []
location_no_duplicates_restaurant = []


# # address we need to locate
# loc = 'Gomel'
#
# # finding the location
# location = geocode(loc, provider="nominatim", user_agent='my_request')
# #
# point = location.geometry.iloc[0]
# print('Name: ' + loc)
# print('complete address: ' + location.address.iloc[0])
# print('longitude: {} '.format(point.x))
# print('latitude: {} '.format(point.y))

geolocator = Nominatim(user_agent="Testess") #Указываем название приложения (так нужно, да)
address = str(input('Введите адрес: \n')) #Получаем интересующий нас адрес
location = geolocator.geocode(address) #Создаем переменную, которая состоит из нужного нам адреса
print(location) #Выводим результат: адрес в полном виде
print(location.latitude, location.longitude)
# 52.4321132 31.0005449

# Перевод в широту и долготу для кофе

# Перевод в широту и долготу для кинотеатров


# Перевод в широту и долготу для ресторанов

