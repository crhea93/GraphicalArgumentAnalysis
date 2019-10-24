from django.db import models
from django_mysql.models import ListCharField
# Create your models here.

class Block(models.Model):
    title = models.CharField(
        max_length=200,
        default='',
        blank=False
    )
    x_pos = models.FloatField(default=0.0, blank=False)
    y_pos = models.FloatField(default=0.0, blank=False)
    num = models.FloatField(default=0, blank=True)
    creator = models.CharField(max_length=100, default='')
    links = ListCharField(
        base_field=models.CharField(max_length=3),
        size=150,
        max_length=(150 * 3 * 10),
        blank=True
    )


    def __str__(self):
        return self.title

    def update(self, form_info):
        print(form_info)
        if self._state.adding:
            # If instance doesn't exist!
            raise self.DoesNotExist
        for field, value in form_info.items():
            # Let's get updating
            setattr(self, field, value)
        # And finally save
        self.save(update_fields=list(form_info.keys()))