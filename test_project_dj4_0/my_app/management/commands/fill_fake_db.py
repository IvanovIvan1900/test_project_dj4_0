# https://docs.djangoproject.com/en/4.0/howto/custom-management-commands/
from django.core.management.base import BaseCommand
from tests.fixtures.factory import ClientFactory


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument(
                            '--count',
                            type=int,
                            default=30,
                            help='count element, default 30',)

    def handle(self, *args, **options):
        ClientFactory.create_batch(options.get('count'))
        # for poll_id in options['poll_ids']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)
        #     poll.opened = False
        #     poll.save()
        # self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))