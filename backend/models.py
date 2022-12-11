from django.db import models

ADMIN_REGISTRATION = []

def admin_register(cls):
    ADMIN_REGISTRATION.append(cls)
    return cls 

@admin_register
class Create(models.Model):
    name = models.CharField(max_length=256)
    start_time = models.TimeField( blank=True)
    end_time = models.TimeField( blank=True)
    start_price = models.CharField(max_length=256,blank=True)

    def __str__(self):
        return "{0}({1})".format(self.__class__.__name__, self.name) 






















