from django.contrib import admin

from .models import *

admin.site.register(Template)
admin.site.register(Question)
admin.site.register(Request)
admin.site.register(Revision)
admin.site.register(Answer)
admin.site.register(Comment)
