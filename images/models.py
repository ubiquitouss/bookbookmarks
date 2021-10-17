from django.db import models
from django.conf import settings
# this line is to generate slug field automatically
from django.utils.text import slugify

class Image(models.Model):
    #This is a foreign key field because it specifies a one-to-many relationship: a user 
    #can post multiple images, but each image is posted by a single user
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='images_created',
            on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True,db_index=True)

    #You will need a many-to-many relationship in this case because a user might 
    #like multiple images and each image can be liked by multiple users.
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                    related_name='images_liked',
                    blank=True)

    def __str__(self):
        return self.title
    #automatic generate slug fielsd
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)