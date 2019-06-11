from django.apps import AppConfig


class mdbConfig(AppConfig):
    name = 'mdb'
    verbose_name = 'Django Movie Database'

    def ready(self):
        import mdb.signals
