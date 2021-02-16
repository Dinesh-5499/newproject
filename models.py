from django.db import models

from django.forms.fields import ChoiceField

# Create your models here.
class Camera(models.Model):
    choice_set_stream = [
        ('Yes','Yes'),
        ('No','No'),
    ]
    choice_set_group = [
        ('Cenamatic','Cenamatic'),
        ('Action','Action'),
        ('Macro','Macro'),
        ('Drone','Drone'),
        ('PointToShoot','Point To Shoot'),
        ('Personal','Personal')
    ]


    cam_url = models.URLField(max_length=100)
    cam_model = models.CharField(max_length=100)
    stream_status = models.CharField(max_length=100,choices=choice_set_stream,default='Yes')
    created_at = models.DateField()
    cam_name = models.CharField(max_length=200)
    cam_user = models.CharField(max_length=200)
    cam_group = models.CharField(max_length=200,choices=choice_set_group,default='Cenamatic')

    def __str__(self):
        return self.cam_name
