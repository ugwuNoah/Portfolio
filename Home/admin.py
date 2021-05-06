from django.contrib import admin
from .models import MyWork, WhatImGoodAt


class MyWorkAdmin(admin.ModelAdmin):
    list_display = ('title',)

class WhatImGoodAtAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(MyWork,MyWorkAdmin)
admin.site.register(WhatImGoodAt, WhatImGoodAtAdmin )
