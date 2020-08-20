from django import forms

from product import models


class ReviewForm(forms.ModelForm):

    class Meta:
        model = models.Review
        exclude = ('author', 'product', )