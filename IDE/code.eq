include query
string name := scan()
write => get('http://equilibriumweb.pythonanywhere.com/api',{'code': name})

