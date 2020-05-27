from django.core.management.base import BaseCommand
from fullthrottle_test_app.models import *

import random
import datetime
import string


class Command(BaseCommand):
    def get_user_data(self):
        name = ''.join(random.choices(string.ascii_lowercase, k=10))
        id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        timezones = ["America/Los_Angeles", "Asia/Kolkata"]
        timezone = timezones[random.randint(0, 1)]
        return {'id': id, 'name': name.capitalize(), 'timezone': timezone}

    def generate_dates(self, start, count):
        count -= 1
        timestamps = []
        temp = []
        while count >= 0:
            s = start + datetime.timedelta(minutes=random.randrange(60))
            # temp.append(datetime.datetime.strftime(s, "%b %d %Y  %H:%M %p"))
            temp.append(s)
            if len(temp) == 2:
                timestamps.append(temp)
                temp = []
            count -= 1
        return timestamps

    def get_activity(self):
        day, month, year = random.randint(1, 28), random.randint(1, 12), random.randint(2015, 2019)
        hour, minute = random.randint(1, 12), random.randint(0, 59)
        meridians = ['AM', 'PM']
        date = datetime.datetime.strptime(f'{month} {day} {year}  {hour}:{minute} {meridians[random.randint(0, 1)]}',
                                          "%m %d %Y  %H:%S %p")
        return self.generate_dates(date, 6)

    def add_arguments(self, parser):
        parser.add_argument(
            'number_of_users',
            type=int,
            help="Number of users to be added in the database."
        )
        parser.add_argument(
            '--append',
            action='store_true',
            dest='append_to_existing',
            default=False,
            help="Append new record to exiting record."
        )

    def handle(self, *args, **options):
        records = []
        activity_records = []
        count = options['number_of_users']

        for _ in range(count):
            user_data = self.get_user_data()
            periods = self.get_activity()
            # print(periods)
            kwargs_user = {
                'name': user_data['name'],
                'id': user_data['id'],
                'timezone': user_data['timezone']
            }

            for i in range(3):
                kwargs_period = {
                    'u_id': user_data['id'],
                    'start_time': periods[i][0],
                    'end_time': periods[i][1]
                }
                record = ActivityPeriod(**kwargs_period)
                activity_records.append(record)

            record = User(**kwargs_user)
            records.append(record)
        if not options['append_to_existing']:
            User.objects.all().delete()
            ActivityPeriod.objects.all().delete()
            self.stdout.write(self.style.SUCCESS("Previous Records Deleted!!"))

        User.objects.bulk_create(records)
        ActivityPeriod.objects.bulk_create(activity_records)
        self.stdout.write(self.style.SUCCESS("Added new values to the models!!"))

