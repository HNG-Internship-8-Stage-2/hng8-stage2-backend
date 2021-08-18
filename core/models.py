from django.db import models


class Contact(models.Model):
	name = models.CharField(max_length=60)
	email_address = models.EmailField()
	message = models.TextField()

	def __str__(self):
		return f'{self.name} - {self.message}'
