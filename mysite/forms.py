from crispy_forms.layout import Field
from django import forms

from .models import Profile


class ContactForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["user", "isPhilDirector", "isPresident", "isProfDirector", "isSocialDirector",
                   "isTechDirector", "isVP", "user_id", "votes"]
        localized_fields = ('birth_date',)
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'E-mail',
            'pledge_class': 'Pledge Class',
            'img_src': 'Image Source',
            'birth_date': 'Birth Date',
            'professional_req': 'Professional Requirement',
            'philanthropy_req': "Philanthropy Requirement",
            'tech_req': 'Tech Requirement',
            'financial_req': 'Financial Requirement (Dues)',
            'college_year_selection': 'Year in College',
            'image': 'Profile Picture'
        }


class CustomCheckbox(Field):
    template = 'templates/website/components/fields/custom_checkbox.html'
