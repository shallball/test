from django.db import models


class Movie(models.Model):
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    directors = models.CharField(db_column='Directors', max_length=40)  # Field name made lowercase.
    stars = models.CharField(db_column='Stars', max_length=40)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=20)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=10)  # Field name made lowercase.
    rate = models.CharField(db_column='Rate', max_length=10)  # Field name made lowercase.
    runtime = models.CharField(db_column='Runtime', max_length=20)  # Field name made lowercase.
    ticket = models.CharField(db_column='Ticket', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Movie'