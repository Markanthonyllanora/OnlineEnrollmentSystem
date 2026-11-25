
from django.db import models


class Student(models.Model):

    YEAR_CHOICES = [
        ("1st Year", "1st Year"),
        ("2nd Year", "2nd Year"),
        ("3rd Year", "3rd Year"),
        ("4th Year", "4th Year"),
    ]

    # STUDENT INFORMATION
    student_number = models.CharField(
        max_length=30,
        unique=True
    )

    full_name = models.CharField(max_length=150)

    course = models.CharField(max_length=150)

    year_level = models.CharField(
        max_length=20,
        choices=YEAR_CHOICES
    )

    section = models.CharField(max_length=50)

    email = models.EmailField(blank=True)

    contact_number = models.CharField(
        max_length=20,
        blank=True
    )

    birth_date = models.DateField(
        null=True,
        blank=True
    )

    address = models.TextField(blank=True)

    # FAMILY BACKGROUND - FATHER
    father_name = models.CharField(
        max_length=150,
        blank=True
    )

    father_occupation = models.CharField(
        max_length=150,
        blank=True
    )

    father_contact = models.CharField(
        max_length=20,
        blank=True
    )

    # FAMILY BACKGROUND - MOTHER
    mother_name = models.CharField(
        max_length=150,
        blank=True
    )

    mother_occupation = models.CharField(
        max_length=150,
        blank=True
    )

    mother_contact = models.CharField(
        max_length=20,
        blank=True
    )

    

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
