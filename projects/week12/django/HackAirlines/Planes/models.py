from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Plane(models.Model):
    name = models.CharField(max_length=200, default='Hack Plane', unique=True)
    capacity = models.IntegerField()
    crew = models.IntegerField()

    def __str__(self):
        return 'Plane {name}'.format(name=self.name)

class Flight(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    passengers = models.IntegerField()
    max_passengers = models.IntegerField()
    from_dest = models.CharField(max_length=100)
    to_dest = models.CharField(max_length=100)

    plane = models.ForeignKey(
        'Plane',
        on_delete=models.CASCADE,
        related_name='flights'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='flights'
    )


    def __str__(self):
        return f'Fligh for {self.user.email} from {self.from_dest} to {self.to_dest}'


class FlightReservation(models.Model):
    passenger = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reservation'
    )
    flight = models.ForeignKey(
        Flight,
        on_delete=models.CASCADE,
        related_name='reservations'
    )
    seat = models.CharField(max_length=5)
    price = models.DecimalField(max_digits=5, decimal_places=2)
