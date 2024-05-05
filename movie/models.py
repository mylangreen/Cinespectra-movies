from django.db import models

# Create your models here.


SINGLE = 'Single'
SEASONAL = 'Seasonal'

type_choices = [
    (SINGLE , 'Single'),
    (SEASONAL , 'Seasonal')
]



class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
        


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    img_url = models.URLField(max_length=250)
    video_url = models.URLField(max_length=250,blank=True,null=True)
    iframe_code = models.TextField()
    genre = models.ManyToManyField(Category)
    slug = models.SlugField(blank=True,null=True)
    added_at = models.DateField(auto_now_add=True)
    is_trending = models.BooleanField(default=False)
    hot = models.BooleanField(default=False)
    is_upcoming = models.BooleanField(default=False)
    type = models.CharField(max_length=100,choices=type_choices,default=SINGLE)
    rate = models.FloatField(null=True,blank=True)



    def __str__(self):
        return self.title

class Cast(models.Model):
    img_url = models.URLField(max_length=500)
    name    = models.CharField(max_length=200)
    role   = models.CharField(max_length=200)
    movie = models.ManyToManyField(Movie,related_name='cast')

    def __str__(self):
        return self.name
    
class MovieRequest(models.Model):
    title = models.CharField(max_length=50)
    name  = models.CharField(max_length=50)

    def __str__(self):
        return self.title  


class Season(models.Model):
    number = models.IntegerField(null=True,blank=True)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='seasons')
    
    def __str__(self):
        return f"{self.movie.title} - Season{self.number}"

class Episode(models.Model):
    number = models.IntegerField(null=True,blank=True)
    season = models.ForeignKey(Season,on_delete=models.CASCADE,related_name='episodes')    
    link = models.URLField(max_length=200,null=True,blank=True)
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(max_length=200,null=True,blank=True,)
    def __str__(self) :
        return f"{self.season.movie.title} - Season {self.season.number} - Episode {self.number}"



    
