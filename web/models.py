import uuid
from django.db import models
from email.policy import default

# Create your models here.


class Tecnologia(models.Model):
    tecnologia_uuid = models.UUIDField()
    nombre = models.CharField(max_length=64)
    descripcion = models.TextField()
    ver_mas = models.CharField(max_length=64)
    image_url = models.URLField()
    nombre_libro_1 = models.CharField(max_length=64, default=0)
    libro_1 = models.URLField(default=0)
    nombre_libro_2 = models.CharField(max_length=64, default=0)
    libro_2 = models.URLField(default=0)
    nombre_libro_3 = models.CharField(max_length=64, default=0)
    libro_3 = models.URLField(default=0)
    is_private = models.BooleanField(default=True)


class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
