from django.db import models

class Publisher(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state_province=models.CharField(max_length=30)
    country=models.CharField(max_length=50)
    website=models.URLField()
    def __str__(self):
        return self.name

    class Admin:
        pass


class Author(models.Model):
    salutation=models.CharField(max_length=10)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    headshot=models.ImageField(upload_to='/home/zmj/python/sblog/sblog1/tmp')
    def __str__(self):
        return self.first_name
    
    class Admin:
        pass

class Book(models.Model):
    title=models.CharField(max_length=100)
    authors=models.ManyToManyField(Author)
    publisher=models.ForeignKey(Publisher)
    publication_date=models.DateField()
    def __str__(self):
        return self.title

    class Admin:
        #pass
        list_display=('title','publisher','publication_date')
        list_filter=('publisher','publication_date')
        ordering=('-publication_date',)
        search_fields=('title',)
# Create your models here.
