from django import forms

# CHOICES = [
#     ("male", "MALE"),
#     ("female", "male"),
# ]

CHOICES = [
    "male"
]

class AddForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=64) #, widget=forms.Textarea(attrs={"class":"form-sml"}))
    last_name = forms.CharField(label="Last Name", max_length=64)
    email = forms.EmailField(label="Email", max_length=64)
    gpa = forms.FloatField(label="GPA", max_value=10.0, min_value=0.0)
    subject = forms.CharField( max_length=65, required=False)
    gender = forms.CharField( max_length=65, required=False)

    # gender = forms.ChoiceField( choices=["male", "femla"], required=False)
    # gender = forms.CharField(max_length=100, choices=CHOICES, null=True)

    # forms.CharField(max_length=65, forms.ChoiceField(, choices=[CHOICES], required=False))

    # def clean(self):
    #     cleaned_data = super().clean()
    #     first_name = cleaned_data.get("first_name")
    #     last_name = cleaned_data.get("last_name")
    #     email = cleaned_data.get("email")
    #     gpa = cleaned_data.get("gpa")
    #     subject = cleaned_data.get("subject")
        

    #     if not first_name and not last_name and not email and not gpa and not subject:
    #         raise forms.ValidationError("You have to write something!")
        
    # widgets = [
        
    # ]