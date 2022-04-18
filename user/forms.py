from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password =forms.CharField(label="Parola", widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="Kullanıcı Adı")
    password = forms.CharField(max_length=20, label="Parola", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label="Parolayı Doğrula", widget=forms.PasswordInput)
    
    #password ile confirm aynı mı bunu kontrol etmek için clean methodunu kullanıyoruz.
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm: #password ve confirm alanları doldurulmuş mu
            raise forms.ValidationError("Parolalar Eşleşmiyor") #raise ile exception fırlatıyoruz.
        
        #Sözlük oluşturuyoruz.
        values = {
            "username" : username,
            "password" : password
        }
        return values
