import logging


from django.core.management import BaseCommand, CommandParser
from apps.contacts.services import generate_contact

from apps.contacts import models


class Command(BaseCommand):
    help = "Experimental"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")


    def handle(self, *args, **options):
        self.logger.info(f"Experemental")

