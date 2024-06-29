from django.contrib import admin
from .models import Categoria, Producto
from .models import *

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrdenItem)
admin.site.register(ShippingAddress)