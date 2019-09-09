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
    majors = [
        (0, 'Accounting'), (1, 'Acting'), (2, 'Advertising'), (3, 'Aerospace Engineering'),
        (4, 'Aerospace Engineering'), (5, 'African and African Diaspora Studies'), (6, 'American Studies'),
        (7, 'Anthropology'), (8, 'Applied Learning and Development'), (9, 'Architectural Engineering'),
        (10, 'Architectural Engineering'), (11, 'Architectural Studies'), (12, 'Architecture'),
        (13, 'Architecture/Architectural Engineering*'), (14, 'Art History'),
        (15, 'Arts and Entertainment Technologies'), (16, 'Asian Cultures and Languages'), (17, 'Asian Studies'),
        (18, 'Astronomy'), (19, 'Athletic Training'), (20, 'Biochemistry'), (21, 'Biology'),
        (22, 'Biomedical Engineering'), (23, 'Biomedical Engineering'), (24, 'Canfield Business Honors Program'),
        (25, 'Chemical Engineering'), (26, 'Chemical Engineering'), (27, 'Chemistry'), (28, 'Civil Engineering'),
        (29, 'Civil Engineering'), (30, 'Classical Languages'), (31, 'Classical Studies'),
        (32, 'Communication and Leadership'), (33, 'Communication Sciences and Disorders'),
        (34, 'Communication Studies'), (35, 'Computational Engineering'), (36, 'Computational Engineering'),
        (37, 'Computer Science'), (38, 'Dance'), (39, 'Dance Studies'), (40, 'Design'), (41, 'Economics'),
        (42, 'Electrical and Computer Engineering'), (43, 'Electrical and Computer Engineering'), (44, 'English'),
        (45, 'Environmental Engineering'), (46, 'Environmental Engineering'),
        (47, 'Environmental Science (Biological Sciences)'), (48, 'Environmental Science (Geographical Sciences)'),
        (49, 'Ethnic Studies'), (50, 'European Studies'), (51, 'Finance'), (52, 'French'), (53, 'Geography'),
        (54, 'Geosystems Engineering and Hydrogeology**'), (55, 'Geosystems Engineering and Hydrogeology**'),
        (56, 'German'), (57, 'German, Scandinavian and Dutch Studies'), (58, 'Government'), (59, 'Health and Society'),
        (60, 'History'), (61, 'Human Development and Family Sciences'), (62, 'Human Dimensions of Organizations'),
        (63, 'Humanities'), (64, 'Iberian and Latin American Languages and Cultures'), (65, 'Interior Design'),
        (66, 'International Business'), (67, 'International Relations and Global Studies'), (68, 'Italian'),
        (69, 'Jazz'), (70, 'Jewish Studies'), (71, 'Journalism'), (72, 'Kinesiology and Health Education'),
        (73, 'Latin American Studies'), (74, 'Linguistics'), (75, 'Management'), (76, 'Management Information Systems'),
        (77, 'Marketing'), (78, 'Mathematics'), (79, 'Mechanical Engineering'), (80, 'Mechanical Engineering'),
        (81, 'Medical Laboratory Science'), (82, 'Middle Eastern Languages and Cultures'),
        (83, 'Middle Eastern Studies'), (84, 'Music (B.A.)'), (85, 'Music Composition (B.A. or B.M.)'),
        (86, 'Music Performance'), (87, 'Music Studies'), (88, 'Neuroscience'), (89, 'Nursing'), (90, 'Nutrition'),
        (91, 'Petroleum Engineering'), (92, 'Petroleum Engineering'), (93, 'Pharmacy'), (94, 'Philosophy'),
        (95, 'Physics'), (96, 'Plan II Honors Program'), (97, 'Pre-Pharmacy'), (98, 'Psychology'),
        (99, 'Public Health'), (100, 'Public Relations'), (101, 'Radio-Television-Film'), (102, 'Religious Studies'),
        (103, 'Rhetoric and Writing'), (104, 'Russian, East European and Eurasian Studies'),
        (105, 'Science and Technology Management'), (106, 'Social Work'), (107, 'Sociology'), (108, 'Studio Art'),
        (109, 'Supply Chain Management'), (110, 'Sustainability Studies'), (111, 'Textiles and Apparel'),
        (112, 'Theatre and Dance'), (113, 'Theatre Studies'), (114, 'Undeclared'), (115, 'Undeclared (Communication)'),
        (116, 'Undeclared (Liberal Arts)'), (117, 'Undeclared (Natural Sciences)'), (118, 'Urban Studies'),
        (119, 'Visual Art Studies'), (120, 'Womenâ€™s and Gender Studies'),
    ]
    major = models.CharField(null=False, max_length=40, choices=majors, default = 114)
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
