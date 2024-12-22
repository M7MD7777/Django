from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Feedback,Category,Product,NewItem,TrendItem,Offer

class RegisterForm(UserCreationForm):
    address = forms.CharField(max_length=255, required=True)
    phone_number = forms.CharField(max_length=20, required=True)


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'address', 'phone_number', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['username'].validators = []     

    

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                address=self.cleaned_data['address'],
                phone_number=self.cleaned_data['phone_number']
            )
        return user
    

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields=['text']

     
class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'description', 'parent_category','image']

class ProductForm(forms.ModelForm):

    class Meta:
        model=Product
        fields = ['name','description','price','category','image']   

class NewItemForm(forms.ModelForm):

    class Meta:
        model=NewItem
        fields = ['product']  

class TrendItemForm(forms.ModelForm):
    
    class Meta:
        model=TrendItem
        fields=['product']
                  

class OfferForm(forms.ModelForm):
    
    class Meta:
        model=Offer 
        fields=['product','discount']                 