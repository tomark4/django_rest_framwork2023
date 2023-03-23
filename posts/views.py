from django.views import View
from django.http import HttpResponse
from django.shortcuts import render

class Home(View):
  def get(self, request):
    name = "Peter Parker"
    age = 40
    skills  = ['django','react','mysql']
    return render(request, 'posts/home.html', context={
      'name': name, 
      'age': age, 
      'skills':skills,
      'position': 'Developer'
    })

