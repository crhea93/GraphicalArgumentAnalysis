from django.db import models

# Create your models here.
class Link(models.Model):
    starting_block = models.IntegerField(default=0)
    ending_block = models.IntegerField(default=0)
    creator = models.CharField(max_length=100,default='')
    num = models.IntegerField(default=0)
    start_x = models.FloatField(default=0)
    start_y = models.FloatField(default=0)
    end_x = models.FloatField(default=0)
    end_y = models.FloatField(default=0)
    warrant = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return str(self.num)

    def update(self, form_info):
        if self._state.adding:
            # If instance doesn't exist!
            raise self.DoesNotExist
        for field, value in form_info.items():
            # Let's get updating
            setattr(self, field, value)
        # And finally save
        self.save(update_fields=list(form_info.keys()))