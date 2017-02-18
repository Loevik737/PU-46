from django.db import models


#creating a model for Users as an example, this wil not be used, but is an example for how
#to use models. This model wil be created as a table in the dabase
class User(models.Model):

    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,
    )

    email = models.EmailField()

    phone = models.CharField(max_length=12,default='000000000000')

    def __str__(self):

        return ' '.join([
            self.first_name,
            self.last_name,
            self.email,
            self.phone,
        ])
