include time
use parserBank
include query

write => 'Привет!\nЭто программа прогноза погоды на Equilibrium\n'

write => 'Введи названия города: '
string city := scan()
dict info := get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=412efa8f683561e258840d1a03be4644',bad)
string info2 := 'В городе ' + city.title() + ' '
write => info2 + str(info['main']['temp'] - 273.15) + ' градуса по цельсию'
