from my_app.models import Client
import pytest


@pytest.mark.django_db
def test_create_30_clients_in_db(client_factory: Client):
    list_of_clients = client_factory.create_batch(30)
    list_from_db = Client.objects.all()
    func_sort = lambda x: x.name
    assert len(list_of_clients) == len(list_from_db)
    for elem_db, elem_data in zip(sorted(list_from_db, key=func_sort), sorted(list_of_clients, key=func_sort)):
        assert elem_db == elem_data


@pytest.mark.django_db
def test_create_30_clients_in_memory(client_factory: Client):
    list_of_clients = client_factory.build_batch(30)
    list_from_db = Client.objects.all()
    assert len(list_of_clients) == 30
    assert len(list_from_db) == 0
