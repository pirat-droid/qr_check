from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class TasksModel(models.Model):
    """Модель задач"""
    inventory_number = models.CharField(max_length=50,
                                        db_index=True,
                                        verbose_name='Инвентарный номер')
    address = models.CharField(max_length=150,
                               verbose_name='Адрес')
    name = models.CharField(max_length=150,
                            db_index=True,
                            verbose_name='Название')
    executor = models.ForeignKey(User,
                                 on_delete=models.PROTECT,
                                 verbose_name='Исполнитель')
    text = models.TextField(verbose_name='Описание установки')
    date_create = models.DateTimeField(auto_now_add=True,
                                       verbose_name='Время создания')
    date_update = models.DateTimeField(auto_now=True,
                                       verbose_name='Время изменения')
    image = models.ImageField(upload_to='оборудование',
                              verbose_name='Путь хранения')
    status = models.BooleanField(default=None,
                                 verbose_name='Статус',
                                 null=True)
    qr = models.ImageField(upload_to='qr',
                           verbose_name='QR code')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ['date_create']

    def get_absolute_url(self):
        return reverse('task', kwargs={'pk': self.pk})


class ImageModel(models.Model):
    """Модель фото"""
    task = models.ForeignKey(TasksModel,
                             on_delete=models.CASCADE,
                             verbose_name='Фото')
    image = models.ImageField(upload_to='check',
                              verbose_name='Путь хранения')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

    def __str__(self):
        return self.task.name


class CheckListModel(models.Model):
    """Модель CheckList"""
    task = models.ForeignKey(TasksModel,
                             on_delete=models.CASCADE,
                             verbose_name='Чек лист')
    name = models.CharField(max_length=150,
                            db_index=True,
                            verbose_name='Название')
    check = models.BooleanField(default=None,
                                null=True,
                                verbose_name='Проверка')

    class Meta:
        verbose_name = 'Check list'
        verbose_name_plural = 'Check list'

    def __str__(self):
        return self.name
