
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    course = forms.ChoiceField(
        choices=[
            ("ABELS", "ABELS"),
            ("BSA", "BSA"),
            ("BSAIS", "BSAIS"),
            ("BSE", "BSE"),
            ("BSIT", "BSIT"),
            ("BSPA", "BSPA"),
            ("BSSW", "BSSW"),
            ("BTVTEd", "BTVTEd"),
            ("DHRS", "DHRS"),
        ]
    )

    year_level = forms.ChoiceField(
        choices=[
            ("1st Year", "1st Year"),
            ("2nd Year", "2nd Year"),
            ("3rd Year", "3rd Year"),
            ("4th Year", "4th Year"),
        ]
    )

    class Meta:
        model = Student

        fields = [
            "student_number",
            "full_name",
            "birth_date",
            "email",
            "contact_number",
            "address",
            "course",
            "year_level",
            "section",

            # Father's Information
            "father_name",
            "father_occupation",
            "father_contact",

            # Mother's Information
            "mother_name",
            "mother_occupation",
            "mother_contact",
        ]

        widgets = {
            "birth_date": forms.DateInput(
                attrs={"type": "date"}
            ),
            "address": forms.Textarea(
                attrs={"rows": 3}
            ),
        }
