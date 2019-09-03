import django
from cloudinary.models import CloudinaryField
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from rush.models import Rushee


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(default="John", max_length=20)
    last_name = models.CharField(default="Doe", max_length=20)
    email = models.CharField(default="utakpsi@gmail.com", max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    votes = models.ManyToManyField(Rushee, blank=True)

    image = CloudinaryField(
        "Image",
        default='https://res.cloudinary.com/texasakpsi/image/upload/c_thumb,w_200,g_face/v1566281324/profile_pics/blank-profile-picture_twrtwg.png',
        overwrite=True,
        resource_type="image",
        transformation={"quality": "auto:eco"},
        format="jpg",
        folder='profile_pics',
        use_filename=True,
        unique_filename=False,
    )
    img_src = models.URLField(null=True, blank=True)

    philanthropy_req = models.IntegerField(default='0')
    professional_req = models.IntegerField(default='0')
    tech_req = models.IntegerField(default='0')
    financial_req = models.BooleanField(default=False)

    pledge_class = models.CharField(max_length=5, blank=False)

    FRESHMAN = 0
    SOPHOMORE = 1
    JUNIOR = 2
    SENIOR = 3
    GRADUATE = 4
    COLLEGE_YEAR = ((FRESHMAN, "Freshman"), (SOPHOMORE, "Sophomore"), (JUNIOR, "Junior"), (SENIOR, "Senior"), (GRADUATE, "Graduate"))
    college_year_selection = models.PositiveSmallIntegerField(choices=COLLEGE_YEAR, null=False, blank=False, default=0)

    isPhilDirector = models.BooleanField(default=False)
    isProfDirector = models.BooleanField(default=False)
    isTechDirector = models.BooleanField(default=False)
    isPresident = models.BooleanField(default=False)
    isVP = models.BooleanField(default=False)
    isSocialDirector = models.BooleanField(default=False)

    def is_exec(self):
        if self.isVP:
            return True
        if self.isProfDirector:
            return True
        if self.isTechDirector:
            return True
        if self.isSocialDirector:
            return True
        if self.isPresident:
            return True
        if self.isPhilDirector:
            return True
        return False

    def __str__(self):
        return self.user.get_full_name()

    def get_college_year(self):
        try:
            return self.COLLEGE_YEAR[self.college_year_selection][1]
        except Exception:
            return "N/A"

    def set_first_name(self, name):
        self.user.first_name = name
        self.first_name = name

    def set_last_name(self, name):
        self.user.last_name = name
        self.last_name = name

    def set_email(self, email):
        self.user.email = email
        self.email = email

    def clear_exec_position(self):
        self.isPhilDirector = False
        self.isProfDirector = False
        self.isTechDirector = False
        self.isPresident =False
        self.isVP = False
        self.isSocialDirector = False
        create_or_update_user_profile(instance=self, created=True)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name, email=instance.email)
    instance.profile.save()


# Model for Posts
class Post(models.Model):
    text = models.TextField(null=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.TextField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title + ", by " + self.author.get_full_name() + " on " + self.created_date.strftime("%m/%d/%Y, %H:%M:%S")


# Model for dates
class Date(models.Model):
    description = models.CharField(max_length=150, null=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.date.strftime("%m/%d/%Y, %H:%M:%S") + ": " + self.description
