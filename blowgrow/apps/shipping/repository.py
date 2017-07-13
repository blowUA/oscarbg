# apps/shipping/repository.py

from oscar.apps.shipping import repository, methods
#from oscar.apps.shipping import methods


class Repository(repository.Repository):
    methods = [
        methods.SelfPickup(),
        methods.Courier(),
    ]