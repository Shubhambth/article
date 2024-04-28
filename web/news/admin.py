from django.contrib import admin
from .models import Category,Users,News,ContactData,AdminPost 

admin.site.register(Category)
admin.site.register(Users)
admin.site.register(News)
admin.site.register(ContactData)
admin.site.register(AdminPost)
