
from django.http import HttpResponse

# Create your views here.
def hello(request):
  cookie_key = 'dj4e_cookie'
  cookie_value = '27ec7e21'

  print(request.COOKIES)
  oldval = request.COOKIES.get('dj4e_cookie', None)
  print(f"Previous session cookie: {oldval}")
  
  resp = HttpResponse(f'You set the cookie {cookie_key}:{cookie_value}')
  resp.set_cookie(cookie_key, cookie_value, max_age=1000)
  return resp
