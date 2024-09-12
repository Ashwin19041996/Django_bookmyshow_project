from django.shortcuts import render,redirect,HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



# Create your views here.

def index(request):
    return render(request,'index.html')

def movies(request):
    movies = Movies.objects.all()
    for movie in movies:
     print(movie.description)
    return render(request,'movies.html',{'movies':movies})    

def movie_detail(request,id):
    movie=Movies.objects.get(id=id)
    movieobject=Movies.objects.filter(id=id)
    casts=Cast.objects.filter(movie_id=id)
    crews=Crew.objects.filter(movie_id=id)
    
    
    
    return render(request,'movies_detail.html',{'movie': movieobject[0],'casts':casts,'crews':crews})

def theatre_select(request,id):
    movie = Movies.objects.get(id=id)
    
    
    show_timings = ShowTiming.objects.filter(movie_id=movie.id)
    print(show_timings)
    print(movie)
   
   
    
    
    theaters = {}
    for show in show_timings:
        if show.theater.name not in theaters:
            theaters[show.theater.name] = []
        theaters[show.theater.name].append(show)
        print(show.id)
        # print(show.theater.location)
   
            
    return render(request,'theatre_select.html',{'theaters':theaters,'movie':movie})

  

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1!=password2:
            return HttpResponse('your password doesnot match')
        else:

            my_user=User.objects.create_user(uname,email,password1)
            my_user.save()
            return redirect('login')

        print(uname,email,password1,password2)

    return render(request,'signup.html')

def user_login(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=uname,password=password)
        if user is not None:
            login(request,user)
            return redirect('/movies')
        else:
            return HttpResponse('username or password incorrect')    
        print(uname,password)
    return render(request,'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')   


def seat_layout(request,showtiming_id):
    show_timing = ShowTiming.objects.get(id=showtiming_id)
    # print(show_timing)
    movie=Movies.objects.filter(id=show_timing.movie_id)
    
    seats = Seat.objects.filter(theater=show_timing.theater).order_by('row', 'number')
    # print(movie[0].moviename)
    
    

    if request.method == 'POST':
        selected_seat_ids = request.POST.getlist('selected_seats')
        # selected_seat_ids = request.POST.get('selected_seats', '').split(',')
        # selected_seat_ids = [seat_id for seat_id in selected_seat_ids if seat_id] 
        # selected_seats = Seat.objects.filter(id__in=selected_seat_ids, status='available')
        print(selected_seat_ids)

        # if selected_seats:
        #     # Create a new booking associated with the logged-in user
        #     booking = Booking.objects.create(show_timing=show_timing, user=request.user)
        #     booking.seats.set(selected_seats)

        #     # Update the seat status to 'booked'
        #     selected_seats.update(status='booked')

        #     return redirect(f'/bookings/{booking.id}/')

    # # Organize seats by row for easier display
    seat_layout = {}
    for seat in seats:
        if seat.row not in seat_layout:
            seat_layout[seat.row] = []
        seat_layout[seat.row].append(seat)
        
    

    context = {
        'show_timing': show_timing,
        'seat_layout': seat_layout,
        'movie':movie[0]
    }
    return render(request,'seat_layout.html',context)
    # return render(request, 'seat_layout.html', context)    