from django import forms
from .models import chaiVarity

class chaiVarityForm(forms.Form):
    chai_variety = forms.ModelChoiceField(
        queryset=chaiVarity.objects.all(), 
        label="Select Chai Variety",
        widget=forms.Select(attrs={
            'class': 'w-full bg-gray-50 border border-gray-300 text-gray-900 text-md rounded-xl focus:ring-orange-500 focus:border-orange-500 block p-3 shadow-sm transition duration-200 ease-in-out', 
        })
    )
