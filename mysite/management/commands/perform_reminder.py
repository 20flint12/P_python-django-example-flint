
from django.core.management.base import BaseCommand, CommandError

import mysite.email_ASR as email


class Command(BaseCommand):
    # help = 'Closes the specified poll for voting'
    help = 'perform_reminder manualy'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('poll_id', nargs='+', type=int)

        # Named (optional) arguments
        parser.add_argument('--delete',
            action='store_true',
            dest='delete',
            default=False,
            help='Delete poll instead of closing it')

    def handle(self, *args, **options):

        for poll_id in options['poll_id']:
            email.email_reminder()

            # try:
            #     # poll = Poll.objects.get(pk=poll_id)
            # except Poll.DoesNotExist:
            #     # raise CommandError('Poll "%s" does not exist' % poll_id)
            #
            # poll.opened = False
            # poll.save()

        self.stdout.write(self.style.SUCCESS('Successfully closed poll'))

        # ...
        if options['delete']:
            poll.delete()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll'))

        # ...
