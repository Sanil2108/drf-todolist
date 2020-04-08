from django.db import models

class User(models.Model):
    email = models.EmailField(primary_key = True)
    name = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)


TOKEN_VALIDITY_TIME = 10000
class Token(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    last_used = models.DateField(auto_now = True)

    # def is_valid(self):

