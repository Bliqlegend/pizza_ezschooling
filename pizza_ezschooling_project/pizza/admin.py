from django.contrib import admin

from .models import Pizza, Size, Toppings,Types, UserForm, UserSize, UserToppings

admin.site.register(Pizza)
admin.site.register(Size)
admin.site.register(Toppings)
admin.site.register(Types)
admin.site.register(UserSize)
admin.site.register(UserToppings)



