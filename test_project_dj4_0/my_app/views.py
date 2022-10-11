from .tables import Client_Table
from django_tables2 import SingleTableView
from .models import Clients


class Client_ListView(SingleTableView):
    model = Clients
    table_class = Client_Table
    template_name = "my_app_main/client_list.html"
