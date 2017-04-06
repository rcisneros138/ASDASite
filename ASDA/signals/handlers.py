from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
from django.dispatch import receiver


@receiver(valid_ipn_received)
def show_me_the_money(sender, **kwargs):
    """Do things here upon a valid IPN message received"""


@receiver(invalid_ipn_received)
def do_not_show_me_the_money(sender, **kwargs):
    """Do things here upon an invalid IPN message received"""
