from django.contrib import admin
from amtesting_app.models import Topic
from amtesting_app.models import WebPage
from amtesting_app.models import AccessRecord
# Register your models here.

admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(AccessRecord)
