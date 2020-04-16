import webbrowser
new=2;
url= "https://www.google.com"
x=int(input("enter a no \n"))
f=1
while(x>0):
      f=f*x
      x=x-1

print(f)

webbrowser.open(url,new=new);
url= "https://www.facebook.com"
webbrowser.open(url,new=new);

