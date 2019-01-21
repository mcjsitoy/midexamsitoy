from django.db import models





# Create your models here.
class Position(models.Model):

    content = models.TextField(max_length = 200)
    description = models.TextField(max_length = 200)


class Candidate(models.Model):
        firstname = models.CharField(max_length =100)
        lastname = models.CharField(max_length =100)
        position = models.ForeignKey(Position, on_delete = models.CASCADE, related_name = 'positions', null=True, blank=True)

        birthdate = models.DateTimeField('birthday')

        platform = models.TextField(max_length = 200)


        def __str__(self):
            return self.firstname




class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete = models.CASCADE, related_name = 'candidates', null=True, blank=True)
    vote_datetime = models.DateTimeField(auto_now_add=True, blank=True)
