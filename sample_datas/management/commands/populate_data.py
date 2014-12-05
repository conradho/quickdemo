from django.core.management.base import BaseCommand, CommandError
from sample_datas.models import TableData

class Command(BaseCommand):
    def handle(self, *args, **xargs):
        TableData.objects.create(data_1='abc',
                                 data_2='def')
        TableData.objects.create(data_1='123',
                                 data_2='456')
