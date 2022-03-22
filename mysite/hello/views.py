
from django.http import HttpResponse

# Create your views here.
def hello(request):
  print(request.COOKIES)
  oldval = request.COOKIES.get('dj4e_cookie', None)
  print(f"Previous session cookie: {oldval}")
  
  resp = HttpResponse('You set the cookie!')
  resp.set_cookie('dj4e_cookie', '27ec7e21', max_age=1000)
  return resp
