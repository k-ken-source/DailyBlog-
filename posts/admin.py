from django.contrib import admin
from .models import Post,Category,Comments,PostView

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comments)
#admin.site.register(PostView)

