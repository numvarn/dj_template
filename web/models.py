from django.db import models

# Create your models here.


CAT_CHOICES = [
    (1, 'News'),
    (2, 'Advertise'),
    (3, 'Blog')
]


class Blog(models.Model):
    """Model definition for Blog."""

    # TODO: Define fields here
    title = models.CharField(max_length=250)
    content = models.TextField()
    category = models.IntegerField(choices=CAT_CHOICES)
    date_created = models.DateTimeField(auto_created=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Blog."""

        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        """Unicode representation of Blog."""
        pass
