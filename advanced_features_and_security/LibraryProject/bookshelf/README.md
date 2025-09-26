# Permissions & Groups Setup

## Custom Permissions
Defined in `Book` model:
- can_view → allows viewing books
- can_create → allows creating books
- can_edit → allows editing books
- can_delete → allows deleting books

## Groups
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: all permissions

## Usage
Views are protected with `@permission_required`.
Assign users to groups via Django Admin → Groups.

# Security Features Implemented

1. **Django Settings**
   - DEBUG disabled in production
   - XSS, MIME-sniffing, and clickjacking protections enabled
   - Secure cookies and HTTPS enforced
   - Content Security Policy (CSP) via `django-csp`

2. **Templates**
   - All forms include `{% csrf_token %}` for CSRF protection

3. **Views**
   - All database queries use Django ORM (no raw SQL)
   - User inputs validated and sanitized with Django forms

4. **Testing**
   - Verified CSRF token present in forms
   - Checked headers: CSP, X-Frame-Options, X-Content-Type-Options
   - Attempted SQL injection in search field → safely blocked
