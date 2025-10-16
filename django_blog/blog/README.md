## 🧩 Django Blog — User Authentication System

### 📘 Overview

This section of the Django Blog Project implements a comprehensive user authentication system that allows users to register, log in, log out, and manage their profiles.
It builds upon the foundational blog setup completed in Task 1.

Django provides robust authentication and authorization mechanisms out of the box, which we leverage and extend for this project.
In this implementation, we use both Django’s built-in authentication views and custom forms and views to support user registration and profile management.

### 🧠 Key Concepts and Learning Points

| Concept                   | Explanation                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------------------- |
| **Authentication**        | Confirms a user’s identity (e.g., login/logout).                                                |
| **Authorization**         | Determines what a user is allowed to do (e.g., edit their own posts).                           |
| **Django Auth Framework** | Provides models, forms, and views for handling users securely.                                  |
| **User Model**            | Represents the `User` entity in Django, containing fields like `username`, `email`, `password`. |
| **UserCreationForm**      | A built-in Django form that simplifies user registration securely with password hashing.        |
| **CSRF Protection**       | Django automatically protects forms against Cross-Site Request Forgery attacks using tokens.    |
| **LoginRequiredMixin**    | A class-based view mixin that restricts view access to authenticated users only.                |

## Blog CRUD with proper permissions

This section implements full CRUD functionality for blog posts.

### Features

- View all posts (public)
- View single post (public)
- Create, edit, delete (only for authenticated authors)
- Secure access control using LoginRequiredMixin and UserPassesTestMixin

### How to Test

1. Log in as a registered user.
2. Create a post at /posts/new/
3. Edit or delete your own posts.
4. Log out and confirm restricted actions are blocked.

### 🗨️ Comment Functionality

**_What’s added:_**

`Comment` model with timestamps and link to Post and User.

`CommentForm` with validation.

`add_comment` view for creation and CBVs for update/delete.

**Templates:** embedded comment list + create form in post_detail.html; separate edit/delete templates.

**URL patterns** to create, update, delete comments.

**_How to use:_**

**Visit a post;** authenticated users can write comments on the same page.

**Authors** can edit/delete their own comments via the links shown beside their comments.

**_Permissions:_**

**Create:** logged-in users only.

**Edit/Delete:** only the original comment author.

### 🏷️ Tagging & Search Features

Each post can have one or more tags (e.g., django, backend, python).

Tags can be added when creating or editing a post, separated by commas.

Tags appear under each post and link to a page showing related posts.

The search bar allows searching by title, content, or tags.

Example URLs:

/tags/django/ → all posts tagged “django”

/search/?q=api → all posts containing “api”
