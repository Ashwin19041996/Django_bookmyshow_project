# Generated by Django 4.2.16 on 2024-09-10 14:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shows', '0005_theater_alter_movies_release_date_showtiming'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='release_date',
            field=models.DateField(default=datetime.date(2024, 9, 10)),
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.CharField(max_length=1)),
                ('number', models.IntegerField()),
                ('seat_type', models.CharField(default='Regular', max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('available', 'Available'), ('booked', 'Booked'), ('selected', 'Selected'), ('bestseller', 'Bestseller')], default='available', max_length=10)),
                ('theater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='shows.theater')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_at', models.DateTimeField(auto_now_add=True)),
                ('seats', models.ManyToManyField(to='shows.seat')),
                ('show_timing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shows.showtiming')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
