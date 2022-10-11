from django.db import models

# Create your models here.


class Clients(models.Model):

    name = models.CharField(
        max_length=200, unique=True, verbose_name="Название клиента"
    )
    email = models.EmailField(verbose_name="e-mail", default="")

    class Meta:
        verbose_name_plural = "Клиенты"
        verbose_name = "Клиент"
        ordering = ["-name"]

    def __str__(self) -> str:
        return f"Name: {self.name}"


class Tasks(models.Model):
    name = models.CharField(max_length=200)
    client = models.ForeignKey(Clients, verbose_name="Клиент", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()
