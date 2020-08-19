# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Movie(models.Model):
    id = models.AutoField(blank=True, null=True)
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
