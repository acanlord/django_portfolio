from django.db import models


# Create A Blog models
# Title
# Pub_date
# Body
#Image

# Add the Blog app to the settings


# Create a migration


# Migrate


# Add to admin


class Blog(models.Model):
    title = models.Charfield(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/') 
