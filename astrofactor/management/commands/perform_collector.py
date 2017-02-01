
from django.core.management.base import BaseCommand, CommandError

import records.views as vs


class Command(BaseCommand):
    # help = 'Closes the specified poll for voting'
    help = 'perform_collector manualy'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('collect_id', nargs='+', type=int)

        # Named (optional) arguments
        parser.add_argument('--delete',
            action='store_true',
            dest='delete',
            default=False,
            help='Help: perform_collector')

    def handle(self, *args, **options):

        for poll_id in options['collect_id']:

            vs.weather_collect()

        self.stdout.write(self.style.SUCCESS('Successfully weather collected'))

        # ...
        if options['delete']:
            pass
            # poll.delete()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll'))
