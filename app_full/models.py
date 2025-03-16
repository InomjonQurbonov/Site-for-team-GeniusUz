from django.db import models

class Connections(models.Model):
    username = models.CharField(max_length=100)
    user_email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'connections'
        verbose_name = 'Connections'
        verbose_name_plural = 'Connections'

class OurWorkers(models.Model):
    worker_name = models.CharField(max_length=150, null=True, blank=True)
    worker_image = models.ImageField(upload_to='img/workers/', blank=True, null=True)
    worker_info = models.TextField(blank=True, null=True)
    worker_phone = models.CharField(max_length=13, blank=True, null=True)
    worker_telegram = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.worker_name

    class Meta:
        db_table = 'workers'
        verbose_name = 'Workers'
        verbose_name_plural = 'Workers'


class Works(models.Model):
    work_title = models.CharField(max_length=250, null=True, blank=True)
    worker = models.ForeignKey(OurWorkers, on_delete=models.CASCADE, null=True, blank=True)
    work_info = models.TextField(blank=True, null=True)
    work_images = models.ImageField('img/works/%Y/%m/%d', blank=True, null=True)
    work_files = models.FileField('files/works_files/', blank=True, null=True)

    def __str__(self):
        return self.work_title
    
    class Meta:
        db_table = 'works'
        verbose_name = 'Works'
        verbose_name_plural = 'Works'


class OurTariffs(models.Model):
    tariffs_title = models.CharField(max_length=150, blank=True, null=True)
    tariffs_info = models.TextField(blank=True, null=True)
    tariffs_price = models.CharField(max_length=100, blank=True, null=True)
    tariffs_image = models.ImageField('img/tariffs/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return self.tariffs_title

    class Meta:
        db_table = 'tariffs'
        verbose_name = 'Tariffs'
        verbose_name_plural = 'Tariffs'
