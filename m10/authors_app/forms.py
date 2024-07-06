from django.forms import ModelForm, CharField, TextInput
from .models import Tag,Author,Quote


class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    
    class Meta:
        model = Tag
        fields = ['name']


class AuthorForm(ModelForm):
    fullname=CharField(min_length=5,max_length=100,required=True,widget=TextInput())

    class Meta:
        model=Author
        fields=['fullname']
        exclude=['born_date','born_location','description']


class QuoteForm(ModelForm):
    quote=CharField(min_length=5,max_length=255,required=True,widget=TextInput())

    class Meta:
        model=Quote
        fields=['quote']
        exclude=['tags','author']