from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# -------------------------------
# Car Make Model
# -------------------------------
class CarMake(models.Model):
    name = models.CharField(max_length=100)  # Name of the car make
    description = models.TextField()         # Description of the car make
    country = models.CharField(max_length=100, blank=True, null=True)  # Optional
    established_year = models.IntegerField(
        blank=True, null=True,
        validators=[MinValueValidator(1886), MaxValueValidator(now().year)]
    )  # Optional: year car make was established

    def __str__(self):
        return self.name


# -------------------------------
# Car Model
# -------------------------------
class CarModel(models.Model):
    # Link each model to a car make (Many-to-One)
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')

    dealer_id = models.IntegerField()  # Dealer ID from Cloudant database
    name = models.CharField(max_length=100)  # Name of the car model

    # Choices for car type
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    HATCHBACK = 'Hatchback'
    COUPE = 'Coupe'
    CAR_TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (HATCHBACK, 'Hatchback'),
        (COUPE, 'Coupe'),
    ]
    car_type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES, default=SEDAN)

    year = models.IntegerField(
        validators=[MinValueValidator(2015), MaxValueValidator(2023)]
    )

    # Optional fields
    color = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.make.name} {self.name} ({self.year})"
