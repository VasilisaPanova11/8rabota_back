from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy


# Create your models here.
class Material(models.Model):
    title = models.CharField(_("Название"), max_length=255, blank=False)
    description = models.CharField(_("Описание"), max_length=255, blank=False)
    cost = models.IntegerField(_("Цена"), blank=False)

    def get_absolute_url(self):
        return reverse_lazy("shop:mat-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title.__str__()

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"


class Sell(models.Model):
    count = models.IntegerField(_("Количество"), blank=False)
    name = models.CharField(_("Имя покупателя"), max_length=255, blank=False)
    surname = models.CharField(_("Фамилия покупателя"), max_length=255, blank=False)
    city = models.CharField(_("Город"), max_length=255, blank=False)
    country = models.CharField(_("Страна"), max_length=255, blank=False)
    mat = models.ForeignKey(
        Material, verbose_name=_("Материал"), on_delete=models.CASCADE, blank=False
    )

    class Meta:
        verbose_name = "Продажа"
        verbose_name_plural = "Продажи"


class Chart(models.Model):
    image = models.ImageField(_("График"), upload_to="charts/", blank=False)

    class Meta:
        verbose_name = "График"
        verbose_name_plural = "Графики"


class File(models.Model):
    name = models.CharField(_("Название"), max_length=255, blank=False, unique=True)
    file = models.FileField(_("Файл"), upload_to="uploads/", blank=False)

    class Meta:
        verbose_name = "PDF файл"
        verbose_name_plural = "PDF файлы"

    def get_absolute_url(self):
        return reverse_lazy("shop:file-download", kwargs={"name": self.name})

    def __str__(self):
        return self.name.__str__()
