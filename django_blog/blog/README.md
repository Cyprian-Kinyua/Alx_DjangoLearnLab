🧩 Django Blog — User Authentication System
📘 Overview

This section of the Django Blog Project implements a comprehensive user authentication system that allows users to register, log in, log out, and manage their profiles.
It builds upon the foundational blog setup completed in Task 1.

Django provides robust authentication and authorization mechanisms out of the box, which we leverage and extend for this project.
In this implementation, we use both Django’s built-in authentication views and custom forms and views to support user registration and profile management.

🧠 Key Concepts and Learning Points
| Concept | Explanation |
| ------------------------- | --------------------------------- |
| **Authentication** | Confirms a user’s identity (e.g., login/logout). |
| **Authorization** | Determines what a user is allowed to do (e.g., edit their own posts). |
| **Django Auth Framework** | Provides models, forms, and views for handling users securely. |
| **User Model** | Represents the `User` entity in Django, containing fields like `username`, `email`, `password`. |
| **UserCreationForm** | A built-in Django form that simplifies user registration securely with password hashing. |
| **CSRF Protection** | Django automatically protects forms against Cross-Site Request Forgery attacks using tokens. |
| **LoginRequiredMixin** | A class-based view mixin that restricts view access to authenticated users only. |
