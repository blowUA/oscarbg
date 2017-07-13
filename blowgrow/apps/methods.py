# apps/shipping/methods.py

from decimal import Decimal as D
from django.utils.translation import ugettext_lazy as _
from oscar.apps.shipping import methods


class SelfPickup(methods.Free):
    code = 'self-pickup'
    name = _('Self pickup')


class Courier(methods.FixedPrice):
    code = 'courier'
    name = _('Courier shipping')

    charge_excl_tax = D('350.00')
    charge_incl_tax = D('350.00')