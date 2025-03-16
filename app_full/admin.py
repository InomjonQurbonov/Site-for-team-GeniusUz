from django.contrib import admin
import app_full.models as models


class AdminConnections(admin.ModelAdmin):
    list_display = ['id', 'username', 'user_email']
    search_fields = ['id', 'username']
    list_filter = ['username',]


class AdminWorks(admin.ModelAdmin):
    list_display = ['id', 'work_title', 'worker']
    list_filter = ['work_title', 'worker']
    search_fields = ['id', 'work_title', 'worker', 'work_info']


class AdminWorkers(admin.ModelAdmin):
    list_display = ['id', 'worker_name', 'worker_phone', 'worker_telegram']
    list_filter = ['worker_name',]
    search_fields = ['id', 'worker_name', 'worker_phone', 'worker_telegram', 'worker_info']

class AdminTariffs(admin.ModelAdmin):
    list_display = ['id', 'tariffs_title', 'tariffs_price']
    list_filter = ['tariffs_price',]
    search_fields = ['id', 'tariffs_title', 'tariffs_price', 'tariffs_info']

admin.site.register(models.Connections, AdminConnections)
admin.site.register(models.Works, AdminWorks)
admin.site.register(models.OurWorkers, AdminWorkers)
admin.site.register(models.OurTariffs, AdminTariffs)
