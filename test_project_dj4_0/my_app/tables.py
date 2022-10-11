import django_tables2 as tables
from .models import Clients


class Client_Table(tables.Table):
    class Meta:
        model = Clients
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "email")
