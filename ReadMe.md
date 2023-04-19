### Django Project
#### MPOP Reverse II (Ryann Kim Sesgundo)
---

### Packages
**Virtual Environment**
```Bash
pip install virtualenv
```

**Django**
```Bash
pip install django
```
---
### Introduction
> Please, before you install these packages, kindly explore the entire documentation of this repository.
---
### How to start
> First thing is you need to install the `Virtual Environment` or `Virtualenv` on your device `pip install virtualenv`. Then after you install the *Virtual Environment*, you need to add your virtual environment on your project, just type to your terminal `virtualenv venv`. The most common name of your environment is `venv`, if you want to have `collaborators`, `venv` is the best name because it is universal. Next is activate the script by executing this to your terminal:
```Bash
.\venv\Scripts\activate
```
>And lastly, if you want to finish or deactivate the virtual environmane, just type:
```Bash
deactivate
```
> to your terminal.
---
### What is the purpose of using Virtual Environment
> It is to avoid the different errors you may have to your entire device, sprcially some data might be deleted. So the `Virtual Environment` is a way for you to protect your device, it creates a viretual storage or emulation of your device.
---
### Start a Django Project
> Please note that if you start a project, you need first to activate the `Virtual Environment`. So first thing is you need to install django to your device `pip install django` and after you executed it, you may now create a new project. To create a project, kindly execute this to your terminal:
```Bash
django-admin startproject ProjectName
```
> Then you may see a new folder which is `ProjectName (if you use the same name from this tutorial)`. Inside of that folder, there's also another folder, same name as the `ProjectName`. It is the main of your website or program. You may also see the `manage.py` inside of your `PeojectName`.
---
### Start an App or Component
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
### Add some views
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
### How to connect
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
### How to run the project
> To run this project, kindly execute this to your terminal
```Bash
python manage.py runserver
```
> Then you will see a link `http://127.0.0.1:8000`, click that and go to the url. You may see that your website doesn't look like what you did, the thing you need to do is to go to the url: `http://127.0.0.1:8000/hello/index/` to see the results.
