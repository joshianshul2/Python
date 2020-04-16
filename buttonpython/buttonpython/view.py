from django.shortcuts import render

def button(request):
  return render(request,home.html)
def output(request):
  import requests
  data=requests.get("http://reqres.in/api/users")
  print(data.text)
  return render(request,'home.html',{'data':data})
