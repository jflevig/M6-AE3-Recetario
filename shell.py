from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from eventos.models import Evento

content_type = ContentType.objects.get_for_model(Evento)

permiso_add = Permission.objects.get(content_type=content_type, codename='add_evento')
permiso_change = Permission.objects.get(content_type=content_type, codename='change_evento')
permiso_delete = Permission.objects.get(content_type=content_type, codename='delete_evento')
permiso_view = Permission.objects.get(content_type=content_type, codename='view_evento') 

# Grupo: Administradores (Tienen todos los permisos CRUD)
admin_group, created_admin = Group.objects.get_or_create(name='Administradores')
admin_group.permissions.set([permiso_add, permiso_change, permiso_delete, permiso_view])
if created_admin:
    print("Creado y configurado el grupo: Administradores")
else:
    print("Actualizado el grupo: Administradores")

# Grupo: Organizadores (Pueden añadir, cambiar y ver, pero no borrar)
organizador_group, created_organizador = Group.objects.get_or_create(name='Organizadores')
organizador_group.permissions.set([permiso_add, permiso_change, permiso_view])
if created_organizador:
    print("Creado y configurado el grupo: Organizadores")
else:
    print("Actualizado el grupo: Organizadores")

# Grupo: Asistentes (Solo pueden ver)
asistente_group, created_asistente = Group.objects.get_or_create(name='Asistentes')
asistente_group.permissions.set([permiso_view])
if created_asistente:
    print("Creado y configurado el grupo: Asistentes")
else:
    print("Actualizado el grupo: Asistentes")

print("\n¡Configuración de grupos y permisos completada con éxito!")

#######################################################################
from django.contrib.auth.models import User, Group

user1 = User.objects.create_user(username="elena", password="1234")
user2 = User.objects.create_user(username="juana", password="1234")
user3 = User.objects.create_user(username="pedrito", password="1234")

# Asignar a grupos
admin_group = Group.objects.get(name='Administradores')
organizador_group = Group.objects.get(name='Organizadores')
asistente_group = Group.objects.get(name='Asistentes')

user1.groups.add(admin_group)      # Elena es admin
user2.groups.add(organizador_group)  # Juana es organizadora
user3.groups.add(asistente_group) # Pedrito es asistente

