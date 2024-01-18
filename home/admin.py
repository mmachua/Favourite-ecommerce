from django.contrib import admin
from .models import Homeimage
from .models import Post

# Register your models here.
#admin.site.register(Comment)

admin.site.register(Post)
admin.site.register(Homeimage)