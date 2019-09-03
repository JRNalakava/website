import gspread

from django.contrib.auth.models import User
from django.core.management import BaseCommand
from oauth2client.service_account import ServiceAccountCredentials


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        # use credentials to create a client to interact with the Google Drive API
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(credentials)

        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        sheet = client.open("Alpha Kappa Psi contact list fall 2019").sheet1

        # Extract and print all of the values
        matrix = sheet.get_all_values()
        matrix = matrix[2:-1]
        for list_var in matrix:
            last_name = list_var[0]
            first_name = list_var[1]
            major = list_var[2]
            school_year = list_var[3]

            if list_var[3] == 'Freshman':
                school_year = 0
            if list_var[3] == 'Sophomore':
                school_year = 1
            if list_var[3] == 'Junior':
                school_year = 2
            if list_var[3] == 'Senior':
                school_year = 3
            if list_var[3] == 'Graduate':
                school_year = 4

            pledge_class = list_var[4]
            phone_num = list_var[5]
            email = list_var[6]
            self.stdout.write(first_name, ending='')
            username = first_name.lower() + "_" + last_name
            password = 'texasIotaTemp19'
            user = User.objects.create_user(username=username, email=email, password=password, first_name = first_name, last_name = last_name)

            user.save()
