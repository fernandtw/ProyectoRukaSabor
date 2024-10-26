from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Perfil



@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)
    else:
        # Asegúrate de que el perfil existe antes de intentar guardarlo
        if not hasattr(instance, 'perfil'):
            Perfil.objects.create(usuario=instance)  # Crea un perfil si no existe
        else:
            instance.perfil.save()  # Guarda el perfil existente