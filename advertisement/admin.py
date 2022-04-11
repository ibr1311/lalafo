from django.contrib import admin

# Register your models here.
from advertisement.models import Category, Advertisement

admin.site.register(Category)
admin.site.register(Advertisement)