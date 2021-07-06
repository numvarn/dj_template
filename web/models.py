from django.db import models

CATEGORY_CHOICES = [
    (1, 'ข่าวประกาศ'),
    (2, 'โฆษณา'),
    (3, 'บันทึก'),
]

PREFIX_CHOICES = [
    (1, 'นาย'),
    (2, 'นางสาว'),
    (3, 'นาง')
]

# Create your models here.


class Blog(models.Model):
    """Model definition for Blog."""

    # TODO: Define fields here
    title = models.CharField(max_length=255)
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=1)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Blog."""

        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        """Unicode representation of Blog."""
        return self.title


class Author(models.Model):
    """Model definition for Author."""

    # TODO: Define fields here
    prefix = models.IntegerField(choices=PREFIX_CHOICES)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField()

    class Meta:
        """Meta definition for Author."""

        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        """Unicode representation of Author."""
        return self.first_name + " " + self.last_name
