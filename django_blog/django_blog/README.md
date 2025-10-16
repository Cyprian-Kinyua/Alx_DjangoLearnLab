# 📝 Django Blog Project

A full-featured **Django Blog Application** developed as a step-by-step learning project.  
This project integrates key Django concepts — from basic setup and authentication to advanced features like commenting, tagging, and search functionality.

---

## 🚀 Overview

The Django Blog Project demonstrates how to build a modern, interactive blogging platform using Django’s robust features and best practices.

It enables:

- User authentication and profile management
- Full CRUD (Create, Read, Update, Delete) operations for blog posts
- Commenting system with user-specific permissions
- Tagging and categorization using `django-taggit`
- Keyword-based search functionality
- Clean, responsive templates styled with Bootstrap

---

## 🧠 Learning Objectives

This project consolidates essential Django skills and concepts, including:

- Django project and app structure
- Model-View-Template (MVT) pattern
- Authentication and user management
- Form handling and validation
- Class-based views and URL routing
- Static files and template inheritance
- Relationships between models (One-to-Many, Many-to-Many)
- Integration of third-party packages (`django-taggit`)
- Query filtering with `Q` objects
- Clean code organization and modular development

---

## 🏗️ Project Tasks and Features

### **Task 1 – Project Setup & Basic Blog**

Set up the Django project and implemented the foundational blog system.  
Features include:

- Post model with title, content, author, timestamps
- CRUD operations via class-based views
- Templates for post listing and detail display
- URL routing for intuitive navigation

**Key Concepts:** Django setup, models, migrations, CBVs, templates, URLs.

---

### **Task 2 – User Authentication**

Added user registration, login, logout, and profile management.  
Features include:

- Secure user authentication using Django’s built-in system
- Restricted access to post creation, editing, and deletion
- Template-level conditional rendering based on user state

**Key Concepts:** Authentication views, `LoginRequiredMixin`, `UserPassesTestMixin`, session handling.

---

### **Task 3 – Template Structure & Static Files**

Improved the frontend layout and organization.  
Features include:

- Centralized `base.html` with template inheritance
- Navigation bar and responsive design using Bootstrap
- Static files management for CSS and images

**Key Concepts:** `{% load static %}`, Bootstrap integration, clean template hierarchy.

---

### **Task 4 – Comment System**

Enhanced interactivity by allowing users to comment on posts.  
Features include:

- Comment model linked to posts and users
- Add, edit, and delete functionality for comments
- Permissions ensuring only authors can modify their comments
- Inline comment forms integrated in post details

**Key Concepts:** Related models, form handling, class-based views, conditional permissions.

---

### **Task 5 – Tagging & Search Functionality**

Introduced tagging and keyword-based post search.  
Features include:

- Post tagging using the `django-taggit` library
- Many-to-many association between posts and tags
- Filtered post listings by tag
- Search bar enabling keyword lookups across titles, content, and tags

**Key Concepts:** `django-taggit`, tag-based filtering, search queries using `Q` objects.

---

## ⚙️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default)
- **Authentication:** Django built-in user model
- **Tagging:** [django-taggit](https://django-taggit.readthedocs.io/en/latest/)
- **Search:** Django ORM with `Q` object filtering

---

## 📁 Project Structure

django_blog/
│
├── blog/
│ ├── migrations/
│ ├── templates/blog/
│ ├── static/blog/
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── urls.py
│ └── admin.py
│
├── django_blog/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── README.md

---

## 🧪 Testing

Each feature was tested for:

- Functional correctness (CRUD and navigation)
- Permission control (author-only actions)
- Security (CSRF protection and password handling)
- Integration (smooth navigation between pages)

---

## 🔐 Security Measures

- Passwords stored using Django’s hashing algorithm
- CSRF protection for all POST requests
- Access restricted via `LoginRequiredMixin` and `UserPassesTestMixin`
- Validation and sanitization of user input through Django forms

---

## 📖 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/django_blog.git
   cd django_blog
   ```
2. **Set up a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Start the server**

```bash
python manage.py runserver

```

6. **Access the app**
