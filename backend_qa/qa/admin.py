from django.contrib import admin

# Register your models here.
from qa.models.user import User

admin.site.register(User)
