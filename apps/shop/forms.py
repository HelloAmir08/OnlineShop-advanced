from django import forms
from .models import Review



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['username', 'comment', 'rating', 'email']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if self.user and self.user.is_authenticated:
            self.fields['email'].required = False

    def clean(self):
        cleaned_data = super().clean()

        if not self.user or not self.user.is_authenticated:
            if not cleaned_data.get('email'):
                self.add_error('email', 'This field is required.')

        return cleaned_data
