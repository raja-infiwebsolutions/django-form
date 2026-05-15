# Django User Form Project

## Project Overview

This project is a simple Django application where users can submit their information through a form. The form collects details like:

- Name
- Email
- Phone Number
- Address
- City
- Message

The submitted data is stored in the database using Django models.

---

# Features

- User-friendly form page
- Form validation
- Store user data in database
- Django Admin support
- Clean project structure
- CSRF protection enabled

---

# Technologies Used

- Python
- Django
- SQLite (default database)
- HTML
- Bootstrap (optional for styling)

---

# Project Structure

```bash
django_form_project/
│
├── manage.py
├── db.sqlite3
│
├── django_form_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── userform/
│   ├── migrations/
│   ├── templates/
│   │   └── form.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
```

---

# Step 1: Create Django Project

```bash
django-admin startproject django_form_project
cd django_form_project
```

---

# Step 2: Create Application

```bash
python manage.py startapp userform
```

---

# Step 3: Add App in settings.py

```python
INSTALLED_APPS = [
    ...
    'userform',
]
```

---

# Step 4: Create Model

## models.py

```python
from django.db import models

class UserFormData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
```

---

# Step 5: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# Step 6: Create Django Form

## forms.py

```python
from django import forms
from .models import UserFormData

class UserForm(forms.ModelForm):
    class Meta:
        model = UserFormData
        fields = '__all__'
```

---

# Step 7: Create View

## views.py

```python
from django.shortcuts import render, redirect
from .forms import UserForm

def user_form_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/success/')
    else:
        form = UserForm()

    return render(request, 'form.html', {'form': form})
```

---

# Step 8: Create URLs

## userform/urls.py

```python
from django.urls import path
from .views import user_form_view

urlpatterns = [
    path('', user_form_view, name='user_form'),
]
```

---

# Step 9: Main URL Configuration

## django_form_project/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userform.urls')),
]
```

---

# Step 10: Create HTML Template

## templates/form.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>User Form</title>
</head>
<body>

    <h2>User Information Form</h2>

    <form method="POST">
        {% csrf_token %}

        {{ form.as_p }}

        <button type="submit">Submit</button>
    </form>

</body>
</html>
```

---

# Step 11: Register Model in Admin

## admin.py

```python
from django.contrib import admin
from .models import UserFormData

admin.site.register(UserFormData)
```

---

# Step 12: Create Superuser

```bash
python manage.py createsuperuser
```

---

# Step 13: Run Server

```bash
python manage.py runserver
```

---

# Output

- User visits the form page
- Fills details
- Clicks submit
- Data gets stored in database
- Admin can view data from Django Admin Panel

---

# Future Improvements

- Add Bootstrap UI
- Add success message
- Add email notifications
- Add file upload
- Add REST API
- Add AJAX form submission
- Add phone validation

---

# Example Fields

| Field Name | Type |
|------------|------|
| Name | Text |
| Email | Email |
| Phone | Number |
| Address | TextArea |
| City | Text |
| Message | TextArea |

---

# Conclusion

This Django project is useful for:

- Contact forms
- Lead collection
- Registration forms
- Inquiry forms
- Basic CRM systems

It is beginner-friendly and follows Django best practices for forms and database handling.
