### DJango Practice
#### MPOP Reverse II(Ryann Kim Sesgundo)
---
> This is just a simple Django program learned from [CodeWithMosh](https://www.youtube.com/watch?v=rHux0gMZ3Eg)
---
### Packages needed
1. Install PIP Env
```Bash
pip install pipenv
```

2. Install Django
```Bash
pip install django
```
or
```Bash
pipenv install django
```
---
### How to start
1. Create a new project
```Bash
django-admin startproject [projectname] .
```
> [projectname] must be the name of your project or web application. Use . to create the template in the current directory, although it is optional.
Example:
```Bash
django-admin startproject myapp
```

2. Create views
```Bash
python manage.py startapp playground
```
> Playground is the place where you can do some modifications and configurations for frontend of your web application

3. Configure views
* Go to [views.py](playground/views.py)
* Create a new file inside of the playground named urls.py
* follow this code or go to [urls.py](playground/urls.py)
```Python
from django.urls import path # imports path from django.urls
from . import views # calls the views.py in the current directory

# use urlspatterns all in lowercase
# use this pattern of path
# path('start url ends with /", include views function here without ())
# visit url like domain/test/
urlpatterns = [
	path('test/', views.anything)
]
```
* Go to urls.py inside of your project name (myapp/urls.py)
* Inside of that urls.py just import include from django.urls
```Python
from django.urls import includes
```
* Next is to include it thru path just like this
```Python
from django.urls import path, includes

# Include urls.py from playground folder
urlpatterns = [
	path('test/', include('playgroung.urls'))
]
```
* If ever you didn't follow, just go to [urls.py](chatapp/urls.py) for more.

4. Create templates
* First create a folder named templates inside of playground and create an html file anything you want (ex: indx.html)
* Next is go to your views.py inside of playground folder and use render just like this:
```Python
from django.shortcuts import render

def returnHTML(req):
	# 2 parameters, requests: req and html file
	return render(req, 'index.html')
```
* You may also add some return data like this
```Python
from django.shortcuts import render

def returnHTMLWithReturnData(req):
	# 3 parameters, requests: req and html file and a dictionary
	return render(req, 'index.html', { 'name': 'kimmy' })
```
* Then goto your html and use the AngularJS like coding:
```HTML

<h1>{{name}}</h1>

```
* You may also use the condition like:
```HTML
{% if name %}
<h1>{{name}}</h1>
{% else %}
<h1>Who you</h1>
{% endif %}
```
* You may see my code of [views.py](playground/views.py) and [HTML](playground/templates/index.html)
---
### Run a server
> Just execute `python manage.py runserver` to start, and visit `http://127.0.0.1:8000/` to your browser.
---
### Disclamer
> This project is created analyzed and develop while watching the tutorial attached to this documentation. If you want to study about this, just to to the link.n Credits to Mash for his youtube tutorial.