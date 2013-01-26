from django.contrib import admin
from demo.apps.ventas.models import cliente,producto

# Registramos  los  modelos de ventas
admin.site.register(cliente)
admin.site.register(producto)