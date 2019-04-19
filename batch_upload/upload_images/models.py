from django.db import models
from db.base_model import BaseModel
from upload_images.enums import *
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Profile(BaseModel):
    gender_choices = ((k, v) for k, v in GENDER_CHOICE.items())
    name = models.CharField(max_length=20, verbose_name='名字')
    gender = models.SmallIntegerField(default=MALE, choices=gender_choices, verbose_name='性别')
    photo = models.ImageField(upload_to='photos', verbose_name='肖像')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = _('用户画像')