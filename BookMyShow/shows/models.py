from django.db import models
from datetime import date
from django.contrib.auth.models import User




# Create your models here.



class Movies(models.Model):
    moviename=models.CharField(max_length=50)
    image=models.ImageField(upload_to='uploads/movies',default='')
    coverimage=models.ImageField(upload_to='uploads/coverimages',default='')
    description=models.CharField(max_length=500)
    directors = models.CharField(max_length=200)
    genre=models.CharField(max_length=50)
    actors=models.CharField(max_length=200)
    crew=models.CharField(max_length=200,default='')
    movie_format=models.CharField(max_length=30,default='')
    duration=models.CharField(max_length=20,default='')
    language=models.CharField(max_length=30,default='')
    cerificate=models.CharField(max_length=20,default='')
    release_date =  models.DateField(default=date.today())

    def __str__(self):
        return self.moviename


class Crew(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE,related_name='crew_members')
    name = models.CharField(max_length=255)
    image=models.ImageField(upload_to='uploads/crews',default='')
    role = models.CharField(max_length=100)  # e.g., Director, Writer, Producer

    def __str__(self):
        return f"{self.name} ({self.role}) for {self.movie.moviename}"

class Cast(models.Model):
    movie=models.ForeignKey(Movies, on_delete=models.CASCADE,related_name='cast_members')  
    name = models.CharField(max_length=255)
    image=models.ImageField(upload_to='uploads/casts',default='')
    role = models.CharField(max_length=100)  

    def __str__(self):
        return f"{self.name} ({self.role}) for {self.movie.moviename}"    

class Theater(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.name} - {self.city}"


class ShowTiming(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='showtimings')
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, related_name='showtimings')
    time = models.DateTimeField()
    language = models.CharField(max_length=50, default='Hindi')  # Language of the movie

    def __str__(self):
        return f"{self.movie.moviename} at {self.theater.name} on {self.time}"



class Seat(models.Model):
    SEAT_STATUSES = [
        ('available', 'Available'),
        ('booked', 'Booked'),
        ('selected', 'Selected'),
        ('bestseller', 'Bestseller'),
    ]

    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, related_name='seats')
    row = models.CharField(max_length=1)  # A, B, C, etc.
    number = models.IntegerField()  # Seat number in the row
    seat_type = models.CharField(max_length=50, default='Regular')  # Sofa, Premium, etc.
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Rs. 200, Rs. 150
    status = models.CharField(max_length=10, choices=SEAT_STATUSES, default='available')

    def __str__(self):
        return f"Seat {self.row}{self.number} in {self.theater.name}"


class Booking(models.Model):
    show_timing = models.ForeignKey(ShowTiming, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate booking with a user
    seats = models.ManyToManyField(Seat)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.show_timing.movie.moviename} at {self.show_timing.theater.name}"