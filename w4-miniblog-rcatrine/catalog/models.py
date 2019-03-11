from django.db import models
# Create your models here.
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique blog instances

class Blog(models.Model):
    """Model representing a blog (but not a specific entry of a blog)."""
    title = models.CharField(max_length=200)

    # Foreign Key used because blog can only have one author, but authors can have multiple blogs
    # Blogger as a string rather than object because it hasn't been declared yet in the file
    blogger = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    
    summary = models.TextField(max_length=1000, help_text='Enter a blog entry')

    # ManyToManyField used because genre can contain many blogs.
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this blog."""
        return reverse('blog-detail', args=[str(self.id)])

class BlogInstance(models.Model):
    """Model representing a specific blog."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular blog across whole library')
    blog = models.ForeignKey('Blog', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)

    status = models.CharField(
        max_length=1,
        blank=True,
    )

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.blog.title})'

class Blogger(models.Model):
    """Model representing a blogger."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']
    
    def get_absolute_url(self):
        """Returns the url to access a particular blogger instance."""
        return reverse('blogger-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'