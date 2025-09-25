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