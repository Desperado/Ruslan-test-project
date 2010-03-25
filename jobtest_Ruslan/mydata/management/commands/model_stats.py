from django.core.management.base import NoArgsCommand
from django.db.models.loading import get_models


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        """Prints all models in project and how many objects
        of each model is present in database
        """
        for model in get_models():
            print "%s.%s - objects in database %s" % (model._meta.app_label,
                                model._meta.module_name,
                                model.objects.count())
