 
from django.http import HttpResponse
 
from .models import Test
 

def tests(request):
    test1 = Test(name='last')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")
   