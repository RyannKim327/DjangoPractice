### Django Project
#### MPOP Reverse II (Ryann Kim Sesgundo)
---
| Table of Contents | Table of Contents |
| --- | --- |
| [Packages](#packages) | [Introduction](#intro) |
| [How to start](#venv) | [What is the purpose of using Virtual Environment](#importance-of-venv) |
| [Create a requirements.txt](#create-req) | [Install packages from requirements.txt](#install-req) |
| [Start a Django Project](#startproject) | [Start an App or Component](#startapp) |
| [Add some views](#addviews) | [How to connect](#connect) |
| [How to run the project](#runserver) | [How to add Templates](#templates) |
| [How to set Static Files](#static) | [Create a super user or admin](#admin-superuser) |
| [Models or Databases](#models) | [Make Migrations](#makemigrations) |
| [Database to Admin](#db2admin) | [Other say](#final) |

| CRUD Section | |
| --- | --- |
| [Add Data](#add_data) |  |

---
<h3 id="packages">Packages</h3>

**Virtual Environment**
```Bash
pip install virtualenv
```

***Once the virtual environment is enabled***
**Django**
```Bash
pip install django
```

> Before you get started, kindly read [These get to start tutorial](#venv)

---
<h3 id="intro">Introduction</h3>

> Please, before you install these packages, kindly explore the entire documentation of this repository.
---
<h3 id="venv">How to start</h3>

> First thing is you need to install the `Virtual Environment` or `Virtualenv` on your device `pip install virtualenv`. Then after you install the *Virtual Environment*, you need to add your virtual environment on your project, just type to your terminal `virtualenv venv`. The most common name of your environment is `venv`, if you want to have `collaborators`, `venv` is the best name because it is universal. Next is activate the script by executing this to your terminal:
```Bash
.\venv\Scripts\activate
```
> Then you may now start installing Django. Also, once you've already created `venv` you don't need to create another one, just activate and start running the package with `python manage.py runserver`. *Always take note* that, *you must install venv aligned with your DjangoProject*, it will create conflicts to your program. And lastly, if you want to finish or deactivate the virtual environmant, just type:
```Bash
deactivate
```
> to your terminal.
---
<h3 id="importance-of-venv">What is the purpose of using Virtual Environment</h3>

> It is to avoid the different errors you may have to your entire device, sprcially some data might be deleted. So the `Virtual Environment` is a way for you to protect your device, it creates a viretual storage or emulation of your device.
---
<h3 id="create-req">Create a requirements.txt</h3>

> This file includes all the package you installed in your virtual environment or what we call `venv`. The code below is a terminal script you need to execute to automatically generate a `requirements.txt`.
```Bash
pip freeze > requirements.txt
```
---
<h3 id="install-req">Install packages from requirements.txt</h3>

> Before you install these packages from requirements.txt, you've must activate the `virtual environment` first. To activate, just go to these [section](#venv)
```Bash
pip install -r requirements.txt
```
---
<h3 id="startproject">Start a Django Project</h3>

> Please note that if you start a project, you need first to activate the `Virtual Environment`. So first thing is you need to install django to your device `pip install django` and after you executed it, you may now create a new project. To create a project, kindly execute this to your terminal:
```Bash
django-admin startproject ProjectName
```
> Then you may see a new folder which is `ProjectName (if you use the same name from this tutorial)`. Inside of that folder, there's also another folder, same name as the `ProjectName`. It is the main of your website or program. You may also see the `manage.py` inside of your `PeojectName`.
---
<h3 id="startapp">Start an App or Component</h3>

> To start an app or component on django, you've must need to go to your project name, by simply using:
```Bash
cd ProjectName
```
> Once you've executerd this you may now start creating a new app or component. To create one, just use this sample format:
```Bash
django-admin startapp ProjectApp
```
> Take this as a note, you must not use the AppName, same as the ProjectName, it will having a conflict, since they were going to create some files and new directories.
---
<h3 id="addviews">Add some views</h3>

> So you see the views.py inside of your `ProjectApp`, just go there and create a new function in python like this:
```Python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def a(request):
	return HttpResponse("<h3>Hello World</h3>")
```
> The defaule code inside of your views.py is:
```Python
from django.shortcuts import render

# Create your views here.

```
> You may also use html files, but it is later on our documentation
---
<h3 id="connect">How to connect</h3>

> To connect the app to your project, you need first to create a new file in your `PeojectApp` and name it `urls.py`. It is generalized, you don't need to use `url.py`, it may cause error, so it must be `urls.py`. Inside of `urls.py, add these code:
```Python
form django.http import path

urlpatterns = [

]
```
> In this code, the urlpatterns must not be a different variable, it may also turns into an error. next is you need to unclude your function form your views.py by using this code:
```Python
from django.http import path
from . import views

urlpatterns = [
	path('index/', views.a)
]
```
> The `a` is the function inside of your views.py, kindly change it if ever that you use other function name. Next one is go to your main of your project which is the `ProjectName` folder or the same name as your Project, and paste this to `urls.py`
```Python
"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('hello/', include("DjangoApp.urls"))
]
```
> The default code of this file is:
```Python
"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
	path('admin/', admin.site.urls),
]

```
> You may also use it as the landing page of the website, by latting the path as '' or look like this format: `path('', include("DjangoApp.urls"))`, same as the urls.py of your `ProjectApp`, just clear the path name. Then go to the settings.py and inside of `INSTALLEDAPPS` just add a new string same as the ProjectApp. Here's the example of before and after code:

**Before**
```Python

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
]
```
**After**
```Python

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	'DjangoApp',
]
```
---
<h3 id="runserver">How to run the project</h3>

> To run this project, kindly execute this to your terminal
```Bash
python manage.py runserver
```
> Then you will see a link `http://127.0.0.1:8000`, click that and go to the url. You may see that your website doesn't look like what you did, the thing you need to do is to go to the url: `http://127.0.0.1:8000/hello/index/` to see the results.

---
<h3 id="templates">How to add Templates</h3>

> First is you need to create a folder name `templates` inside of your `ProjectApp`. Inside of it, create a sample html, for example `index.html`. Next is go to your `views.py` inside of your `ProjectrApp`, and add this is the comparison of code on your file.

**Before**
```Python

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def a(request):
	return HttpResponse("<h3>Hello World</h3>")

```
**After**
```Python

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def a(request):
	return HttpResponse("<h3>Hello World</h3>")

def b(request):
	return render(request, 'index.html')
```
> ***Note***: You may still change the function name based on what you want, I use a and b functions because I'm lazy to think some variable names. Now, after you've done that, go to your `urls.py` inside of your `ProjectApp` and add this inside of your `urlpatterns`
```Python
path('html/', views.b)
```
> So meaning to say, it may looks like this now.
```Python

from django.http import path
from . import views

urlpatterns = [
	path('index/', views.a)
	path('html/', views.b)
]
```
---
<h3 id="static">How to set Static Files</h3>

> So I actually forgot how, that's why I tried some trial and errors, and now, it works. First is you need to create a new folder, outside of your `ProjectApp`, but inside of your `ProjectName`, and named it `static`. In this name, Django will easily recognized the folder name. Next is create some resources there like your css. After you add your resources there, go to your html file, inside of the `template` folder on your `ProjectApp`, and add this line to the top of the code on in line one:
```Django
{% load static %}
```
> The sample use of static in including some resources such as image is like this
```Django
<link rel="stylesheet" type="text/css" href="{% static '/css/my.css' %}">
<img src="{% static '/img/my.png' %}">
```
> The first line is for css, while the another line is for images, same with audios and videos, the `/css/` and `/img/` signifies as the folder name inside of the static folder. Next one is go to the `settings.py` inside of `ProjectName` or what we call the main. Look for the `STATIC_URL` and add this lines under of it.
```Python
STATICFILES_URLS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'static'
```
> This line will help Django to look for static folder faster.
---
<h3 id="admin-superuser">Create a super user or admin</h3>

> The one of the requirements for a system is to have a database, and to create a specific database, we need to create an admin account or what we called super user. To create a `super user`, we need first to `migrate` the Django Project by executing this command to your terminal.
```Bash
python manage.py migrate
```
> And it gives you some information, after it says a successful message, execute this to your terminal:
```Bash
python manage.py createsuperuser
```
> And once you've execute this, you need to fill up some forms, such as username, email and passwords.
---
<h3 id="models">Database</h3>

> Here's a way for you to create a database here in Django, but before you create a database, you need first to have a [Super User](#admin-superuser). Then follow these steps. First is you need to go to your `models.py` inside of your `Project App` which is also our [component](#startapp). You may see these code:
```Python
from django.db import models

# Create your models here.
```
> Here's where you need to go through. Create a class, which represents as your table name, so if you want to creata a table name called `user` use user as class name, just like this example.
```Python
from django.db import models

# Create your models here.
class user(models.Model):
	# Then add some column name here such as
	username = models.CharField(max_length=25)
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=100)
```
> To understand this code, here's the sample result if this in `SQL`
```SQL
CREATE TABLE user(
	username VARCHAR(30),
	email VARCHAR(50),
	password VARCHAR(100),
)
```
> In addition, you may also use the defaults in Django for password by importing forms from django and using of forms.PasswordInput, here's the example
```Python
from django.db import models
from django import forms
# Create your models here.
class user(models.Model):
	# Then add some column name here such as
	username = models.CharField(max_length=25)
	email = models.CharField(max_length=50, widget=forms.PasswordInput)
	password = models.CharField(max_length=100)
```
> Next is, you need to include the model into your djangoapp, just go to admin.py and add `admin.site.register(yourmodel)` Here's the example

``` Python
# From these code
from django.contrib import admin
# Register your models here.

# ------------------------------- #

# To this code
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(user)

```
---
<h3 id="makemigrations">Make Migrations</h3>

> `makemigrations` in Django is use to packaging up all the models in Django. Models defines as the database in Django. So after you create a models in python which can be found [here](#models), you need to execute it so that your database will be updated too.
```Bash
python manage.py makemigrations
```
---
<h3 id="db2admin">Database to admin</h3>

> So, for you who want to see the database clear, just go to `http://127.0.0.1:8080/admin/` or to your localhost admin, and login your credentials used in [superuser](#admin-superuser). Then you may now see the tables existed, as well as the data you have.
---
<h3 id="add_data">Add Data</h3>

> Since we use the [`user` Models](#models) here's the sample how do we going to add data 
with Django. In views.py. add these things inside, but not in literal, meaning read the comments where the code need to be inserter.

``` python
# In imports
from .models import user

# In the part of defs example is
def addUser(req):
	user.objects.create(username="Your username", email="sample@email.com", password="sample password")

```
> Take note that the parameters used here must be the data or columns you added on your Models

---

<h3 id="final">Other say</h3>

> This program is not yet finish, I still in a way of learning, that's why I've done this like day by day. Big thanks to `Mr. Leonard Andrew Mesiera` for helping us to learn this framework and providing some time to teach us. Also on [CodeWithMosh](https://www.youtube.com/watch?v=rHux0gMZ3Eg)'s youtube channel.
