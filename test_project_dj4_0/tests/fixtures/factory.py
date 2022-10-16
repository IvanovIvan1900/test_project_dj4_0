import factory
from mimesis_factory import MimesisField
from my_app.models import Client
from pytest_factoryboy import register


@register
class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client
        django_get_or_create = ('name',)
    name = MimesisField('username')
    email = MimesisField('email')


# register(ClientFactory, "my_client_factory")
