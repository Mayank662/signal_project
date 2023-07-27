from django.db.models.signals import post_save
from django.dispatch import receiver
from app1.models import Model3

# creating the basic signal function which get triggered upon saving the Model3 object
@receiver(post_save, sender=Model3)
def demo_signal(sender, instance, created, **kwargs):
    if created:
        # can perform n number of operations here
        # for demo just printing a statement
        print(f"Generated through signal")
