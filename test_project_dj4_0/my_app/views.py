from .tables import Client_Table
from django_tables2 import SingleTableView
from .models import Client


class Client_ListView(SingleTableView):
    model = Client
    table_class = Client_Table
    template_name = "my_app_main/client_list.html"
