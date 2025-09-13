from django.db import migrations

def create_groups_and_permissions(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    
    # Get permissions for Book model
    permissions = Permission.objects.filter(codename__in=['can_view', 'can_create', 'can_edit', 'can_delete'])
    
    # Create groups
    editors, _ = Group.objects.get_or_create(name='Editors')
    viewers, _ = Group.objects.get_or_create(name='Viewers')
    admins, _ = Group.objects.get_or_create(name='Admins')
    
    # Assign permissions
    editors.permissions.set(permissions.filter(codename__in=['can_create', 'can_edit']))
    viewers.permissions.set(permissions.filter(codename='can_view'))
    admins.permissions.set(permissions)  # all permissions

class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0002_alter_book_options'),
        ('auth', '0012_alter_user_first_name_max_length'),  # ensure auth app is migrated first
    ]

    operations = [
        migrations.RunPython(create_groups_and_permissions),
    ]
