from django.forms import ModelForm
from .models import *
from crispy_forms.layout import Layout, Row, Column,Submit,Button,HTML,Hidden
from crispy_forms.helper import FormHelper
from django import forms

class PostForm(ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Post
        exclude = ['post_id','status','created_at','created_by','is_deleted','modified_date','modified_by','deleted_date','deleted_by']

