
from django.http import HttpResponse

# Create your views here.
def hello(request):
  
  num_visits = request.session.get('num_visits', 0) + 1
  request.session['num_visits'] = num_visits 
  if num_visits > 4 : del(request.session['num_visits'])
  
  print(request.COOKIES)
  oldval = request.COOKIES.get('dj4e_cookie', None)
  print(f"Previous session cookie: {oldval}")  

  cookie_key = 'dj4e_cookie'
  cookie_value = '27ec7e21'
  resp = HttpResponse(f'view count={str(num_visits)}')
  resp.set_cookie(cookie_key, cookie_value, max_age=1000)
  return resp
