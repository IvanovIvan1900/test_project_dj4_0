from django.db import models

# Create your models here.


class Client(models.Model):

    name = models.CharField(
        max_length=200, unique=True, verbose_name="Название клиента"
    )
    email = models.EmailField(verbose_name="e-mail", default="")

    class Meta:
        verbose_name_plural = "Клиенты"
        verbose_name = "Клиент"
        ordering = ["-name"]
        db_table = 'clients'

    def __str__(self) -> str:
        return f"Name: {self.name}"


class Task(models.Model):
    name = models.CharField(max_length=200)
    client = models.ForeignKey(Client, verbose_name="Клиент", on_delete=models.CASCADE)

    class Meta:
        db_table = 'tasks'

    def __str__(self) -> str:
        return super().__str__()
