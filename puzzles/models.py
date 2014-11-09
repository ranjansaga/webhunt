from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User



# Create your models here.

class Questions(models.Model):
    description = models.TextField()
    level = models.IntegerField(null=True)
    image = models.FileField(upload_to='question_image',blank=True)
    answer = models.CharField(max_length=100)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.description)

        super(Questions, self).save(*args, **kwargs)

    
class Score(models.Model):
    user = models.ForeignKey(User)
    time = models.CharField(max_length=30)
    level = models.CharField(max_length=30)