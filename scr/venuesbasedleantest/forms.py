from django import forms


class SuggestACollegeForm(forms.Form):
    title = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'id': 'hide-me'}))
    name = forms.CharField(
        max_length=255,
        label="Your name",
        widget=forms.TextInput(attrs={'placeholder': 'Required but, yes, it can be a made up name!'}))
    email = forms.EmailField(
        max_length=255,
        label="Your email address",
        widget=forms.TextInput(attrs={'placeholder': 'Required and real please.'}))
    college = forms.CharField(
        max_length=255,
        label="Your college",
        widget=forms.TextInput(attrs={'placeholder': 'Name of the college you are suggesting'}))

    def clean(self):
        data = super(SuggestACollegeForm, self).clean()
        title = data['title']
        if title:
            raise forms.ValidationError("You are a robot :)")
        return data