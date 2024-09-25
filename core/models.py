from django.db import models

# Create your models here.
           
class MovieManager(models.Manager):
    def all_with_related_persons(self):
        qs=self.get_queryset()
        qs=qs.select_related(
            'director'
        )
        
        qs=qs.prefetch_related(
            'writers',
            'actors'
        )
        return qs 
    
    
class Movie(models.Model): 
   # image_url=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    not_rated=0
    rated_G=1
    rated_PG=2
    rated_R=3
    ratings=(
        (not_rated, 'NR - Not Rated'),
        (rated_G, 'G - General Audiences'),
        (rated_PG, 'PG - Parental GuidanceSuggested'),
        (rated_R, 'R - Restricted'),
    )
    title=models.CharField(max_length=140)
    plot=models.TextField()
    year=models.PositiveIntegerField()
    rating=models.IntegerField(choices=ratings, 
                               default=not_rated)
    runtime=models.PositiveIntegerField()
    website=models.URLField(blank=True)
    
    
    objects=MovieManager()
    
    #This is to provide ordering of information
    class Meta:
        ordering = ('-year', 'title')
        
        
    director=models.ForeignKey(
        to='Person',
        on_delete=models.SET_NULL,
        related_name='directed',
        null=True,
        blank=True,
    )
    
    writers=models.ManyToManyField(
        to='Person',
        related_name='writing_credits',
        blank=True
    )
    
    actors=models.ManyToManyField(
        to='Person',
        through='Role',
        related_name='acting_credits',
        blank=True
    )
    
        
    def __str__(self):
        return '{} ({})'.format(self.title, self.year)


class PersonManager(models.Manager):
    def all_with_prefetch_movies(self):
        qs=self.get_queryset()
        return qs.prefetch_related(
            'directed',
            'writing_credits',
            'role_set_movie'
        )
        
        
   
   
   
class Person(models.Model):
       
    first_name=models.CharField(max_length=140)
    last_name=models.CharField(max_length=140)
    born=models.DateField()
    died=models.DateField(null=True, blank=True)
    
    
    objects=PersonManager()
    
    
    class Meta:    
            ordering = ('last_name', 'first_name')
            
    
    def __str__(self):
        if self.died:
            return '{}, {} {{} - {}}'.format(
                self.last_name, 
                self.first_name,
                self.born, 
                self.died
            )
            
            
        return   '{}, {} {{} - {}}'.format(
                self.last_name, 
                self.first_name,
                self.born, 
                self.died
            )
        
        
        
class Role(models.Model):
    movie=models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    person=models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=140)
    
    def __str__(self) -> str:
        return "{} {} {}".format(self.movie_id, self.person_id, self.name)


    class Meta:
        unique_together=('movie', 'person', 'name')
        
           
           
