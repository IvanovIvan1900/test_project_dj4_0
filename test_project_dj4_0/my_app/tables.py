from .models import Client
import django_tables2 as tables


class Client_Table(tables.Table):
    class Meta:
        model = Client
        # template_name = "django_tables2/bootstrap.html"
        fields = ("name", "email")
        attrs = {"class": "table table-striped table-bordered",
                 "thead": {"class": "thead-light"}}
