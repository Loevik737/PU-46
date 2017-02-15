from django.db import models


class Contact(models.Model):

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
