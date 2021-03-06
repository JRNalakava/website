# Generated by Django 2.2.4 on 2019-09-10 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rush', '0022_auto_20190909_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='rushee',
            name='attended_info_session',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='rushee',
            name='major',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Accounting'), (1, 'Acting'), (2, 'Advertising'), (3, 'Aerospace Engineering'), (4, 'Aerospace Engineering'), (5, 'African and African Diaspora Studies'), (6, 'American Studies'), (7, 'Anthropology'), (8, 'Applied Learning and Development'), (9, 'Architectural Engineering'), (10, 'Architectural Engineering'), (11, 'Architectural Studies'), (12, 'Architecture'), (13, 'Architecture/Architectural Engineering*'), (14, 'Art History'), (15, 'Arts and Entertainment Technologies'), (16, 'Asian Cultures and Languages'), (17, 'Asian Studies'), (18, 'Astronomy'), (19, 'Athletic Training'), (20, 'Biochemistry'), (21, 'Biology'), (22, 'Biomedical Engineering'), (23, 'Biomedical Engineering'), (24, 'Canfield Business Honors Program'), (25, 'Chemical Engineering'), (26, 'Chemical Engineering'), (27, 'Chemistry'), (28, 'Civil Engineering'), (29, 'Civil Engineering'), (30, 'Classical Languages'), (31, 'Classical Studies'), (32, 'Communication and Leadership'), (33, 'Communication Sciences and Disorders'), (34, 'Communication Studies'), (35, 'Computational Engineering'), (36, 'Computational Engineering'), (37, 'Computer Science'), (38, 'Dance'), (39, 'Dance Studies'), (40, 'Design'), (41, 'Economics'), (42, 'Electrical and Computer Engineering'), (43, 'Electrical and Computer Engineering'), (44, 'English'), (45, 'Environmental Engineering'), (46, 'Environmental Engineering'), (47, 'Environmental Science (Biological Sciences)'), (48, 'Environmental Science (Geographical Sciences)'), (49, 'Ethnic Studies'), (50, 'European Studies'), (51, 'Finance'), (52, 'French'), (53, 'Geography'), (54, 'Geosystems Engineering and Hydrogeology**'), (55, 'Geosystems Engineering and Hydrogeology**'), (56, 'German'), (57, 'German, Scandinavian and Dutch Studies'), (58, 'Government'), (59, 'Health and Society'), (60, 'History'), (61, 'Human Development and Family Sciences'), (62, 'Human Dimensions of Organizations'), (63, 'Humanities'), (64, 'Iberian and Latin American Languages and Cultures'), (65, 'Interior Design'), (66, 'International Business'), (67, 'International Relations and Global Studies'), (68, 'Italian'), (69, 'Jazz'), (70, 'Jewish Studies'), (71, 'Journalism'), (72, 'Kinesiology and Health Education'), (73, 'Latin American Studies'), (74, 'Linguistics'), (75, 'Management'), (76, 'Management Information Systems'), (77, 'Marketing'), (78, 'Mathematics'), (79, 'Mechanical Engineering'), (80, 'Mechanical Engineering'), (81, 'Medical Laboratory Science'), (82, 'Middle Eastern Languages and Cultures'), (83, 'Middle Eastern Studies'), (84, 'Music (B.A.)'), (85, 'Music Composition (B.A. or B.M.)'), (86, 'Music Performance'), (87, 'Music Studies'), (88, 'Neuroscience'), (89, 'Nursing'), (90, 'Nutrition'), (91, 'Petroleum Engineering'), (92, 'Petroleum Engineering'), (93, 'Pharmacy'), (94, 'Philosophy'), (95, 'Physics'), (96, 'Plan II Honors Program'), (97, 'Pre-Pharmacy'), (98, 'Psychology'), (99, 'Public Health'), (100, 'Public Relations'), (101, 'Radio-Television-Film'), (102, 'Religious Studies'), (103, 'Rhetoric and Writing'), (104, 'Russian, East European and Eurasian Studies'), (105, 'Science and Technology Management'), (106, 'Social Work'), (107, 'Sociology'), (108, 'Studio Art'), (109, 'Supply Chain Management'), (110, 'Sustainability Studies'), (111, 'Textiles and Apparel'), (112, 'Theatre and Dance'), (113, 'Theatre Studies'), (114, 'Undeclared'), (115, 'Undeclared (Communication)'), (116, 'Undeclared (Liberal Arts)'), (117, 'Undeclared (Natural Sciences)'), (118, 'Urban Studies'), (119, 'Unspecified Business'), (120, 'Visual Art Studies'), (121, "Women's and Gender Studies")], default=114),
        ),
        migrations.AlterField(
            model_name='rushee',
            name='random_id',
            field=models.IntegerField(default=121),
        ),
        migrations.AlterField(
            model_name='rushee',
            name='username',
            field=models.CharField(default='username826', max_length=100),
        ),
    ]
