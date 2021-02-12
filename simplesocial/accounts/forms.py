from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

    class Meta():
        #username, email, password1, password2 (to verify password) are builtin attributes for UserCreationForm
        fields = ('username','email','password1','password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label='Display Name' #setting up the lable for username field in thr user UserCreationForm
        self.fields['email'].label='Email Id'
        self.fields['password1'].lable='Password'
        self.fields['password2'].lable='Confirm Password'
