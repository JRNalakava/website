import datetime
from random import random

from cloudinary.models import CloudinaryField
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    question = models.TextField()

    def __str__(self):
        return self.question


# Create your models here.
class Rushee(models.Model):
    first_name = models.CharField(null=False, max_length=20)
    last_name = models.CharField(null=False, max_length=40)
    email = models.EmailField(null=False)
    phone_num = models.CharField(null=False, max_length=10)
    submitted_form = models.BooleanField(default=False)
    date_of_application = models.DateTimeField(default=datetime.datetime.now)
    responses = models.TextField(default='')
    random_id = models.IntegerField(default=int(1000*random()))
    username = models.CharField(max_length=100, default='username'+str((int(1000*random()))))
    yes_votes = models.PositiveIntegerField(default=0)
    no_votes = models.PositiveIntegerField(default=0)
    voters = models.ManyToManyField('mysite.Profile', blank=True)
    FRESHMAN = 0
    SOPHOMORE = 1
    JUNIOR = 2
    SENIOR = 3
    GRADUATE = 4
    COLLEGE_YEAR = (
    (FRESHMAN, "Freshman"), (SOPHOMORE, "Sophomore"), (JUNIOR, "Junior"), (SENIOR, "Senior"), (GRADUATE, "Graduate"))
    college_year_selection = models.PositiveSmallIntegerField(choices=COLLEGE_YEAR, null=False, blank=False, default=0)

    image = CloudinaryField(
        "Image",
        default='https://res.cloudinary.com/texasakpsi/image/upload/c_thumb,w_200,g_face/v1566281324/profile_pics/blank-profile-picture_twrtwg.png',
        overwrite=True,
        resource_type="image",
        transformation={"quality": "auto:eco"},
        format="jpg",
        folder='rushees',
        use_filename=True,
        unique_filename=False,
    )

    def get_college_year(self):
        try:
            return self.COLLEGE_YEAR[self.college_year_selection][1]
        except Exception:
            return "N/A"

    def __str__(self):
        return self.first_name + " " + self.last_name + " (" + str(self.random_id) + ")"

    def set_username(self):
        self.username = self.first_name[0].lower() + "" + self.last_name + "_" + str(self.random_id)


class RushComment(models.Model):
    comment_text = models.TextField(null=False, default='')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rushee = models.ForeignKey(to=Rushee, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.author.first_name + ": " + self.comment_text + " - " + self.rushee.first_name + " " + self.rushee.last_name
