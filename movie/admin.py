from django.contrib import admin
from .models import Category,Movie,Cast,MovieRequest,Season,Episode

# Register your models here.
admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Cast)
admin.site.register(MovieRequest)
admin.site.register(Season)
admin.site.register(Episode)

