import datetime
import random

from django.db import models

TOKEN_VALIDITY_TIME = 10000

TOKEN_STRING_LENGTH = 30

class User(models.Model):
    email = models.EmailField(primary_key = True)
    name = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

    def is_token_valid(self, token):
        time_difference_ms = (datetime.datetime.now() - token.last_used).seconds * 1000
        if (TOKEN_VALIDITY_TIME > time_difference_ms):
            return True
        return False

    def create_update_token(self):
        current_token = None
        try:
            current_token = self.token
        except Exception:
            token = Token()
            token.user = self
            token.set_token()

            current_token = token
        current_token.update_token()

    
class Token(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    last_used = models.DateTimeField(auto_now = True)
    token_string = models.CharField(max_length = 100, primary_key = True)

    def set_token(self):
        token_allowable_chars_index = list(range(ord('a'), ord('z'))) + list(range(ord('A'), ord('Z'))) + list(range(ord('0'), ord('9')))

        token_string = ''
        for i in range(TOKEN_STRING_LENGTH):
            token_string += chr(random.choice(token_allowable_chars_index))

        self.token_string = token_string
    
    def update_token(self):
        self.save()

