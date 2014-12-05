from django.contrib import admin

from sample_datas.models import TableData

# Register your models here.
class TableDataAdmin(admin.ModelAdmin):
    pass

admin.site.register(TableData, TableDataAdmin)
