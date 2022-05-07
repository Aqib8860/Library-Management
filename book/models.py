from django.db import models

# Create your models here.


BOOK_CATEGORY = (
    ("Health", "Health"),
    ("Technology", "Technology"),
    ("Games", "Games"),
    ("Meetups", "Meetups"),
    ("Music", "Music"),
    ("Art", "Art"),
    ("Food", "Food"),
    ("Business", "Business"),
    ("Sports", "Sports"),
)

STATUS = (
	("Available", "Available"),
	("Borrowed", "Borrowed"),

)


class Book(models.Model):
	title = models.CharField(max_length=80)
	author = models.CharField(max_length=80)
	category = models.CharField(max_length=20, choices=BOOK_CATEGORY)
	description = models.TextField()
	date_added = models.DateField(auto_now_add=True)
	status = models.CharField(max_length=20, choices=STATUS)

	def __str__(self):
		return str(self.title)


class Borrowed(models.Model):
	user_id = models.ForeignKey('user.User', on_delete=models.PROTECT)
	book_id = models.ForeignKey(Book, on_delete=models.PROTECT)
	date = models.DateField(auto_now_add=True)
	for_days = models.PositiveIntegerField()
	returned = models.BooleanField(default=False)
