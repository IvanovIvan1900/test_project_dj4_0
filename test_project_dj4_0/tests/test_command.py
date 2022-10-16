# https://docs.djangoproject.com/en/4.0/topics/testing/tools/#topics-testing-management-commands
from io import StringIO
from django.core.management import call_command
import pytest
from my_app.models import Client


@pytest.mark.django_db
def test_command_fill_fake_db_wichout_argument():
    defautl_conn = 30
    out = StringIO()
    call_command('fill_fake_db', stdout=out)
    list_of_db = Client.objects.all()
    assert len(list_of_db) == defautl_conn
    # self.assertIn('Expected output', out.getvalue())


@pytest.mark.django_db
def test_command_fill_fake_db_wich_count():
    count_value = 40
    out = StringIO()
    call_command('fill_fake_db', count=count_value, stdout=out)
    list_of_db = Client.objects.all()
    assert len(list_of_db) == count_value
