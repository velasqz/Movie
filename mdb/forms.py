from django import forms
from django.core.exceptions import ValidationError
from mdb.models import MovieRate


class SimpleForm(forms.ModelForm):
    rate = forms.IntegerField()

    class Meta:
        model = MovieRate
        fields = ('rate', 'movie')

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SimpleForm, self).__init__(*args, **kwargs)

    def clean(self):
        data = super(SimpleForm, self).clean()
        movie = data.get('movie')
        if MovieRate.objects.filter(user=self.user, movie=movie).exists():
            raise ValidationError(f'Movie rate with user {self.user.username} and movie {movie.title} already exists')
        return data

    def save(self, commit=True):
        instance = super(SimpleForm, self).save(commit=False)
        instance.user = self.user
        instance.save()
        return instance