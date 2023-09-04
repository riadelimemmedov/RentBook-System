#

#! Django function and methods
from django import forms



#*AuthorForms
class AuthorForm(forms.ModelForm):
    def clean(self):
        birth_date = self.cleaned_data['birth_date']
        died_date = self.cleaned_data['died_date']
    
        if birth_date and died_date:
            if died_date.year <= birth_date.year:
                splited_date_birth = str(birth_date).split('-')
                splited_date_died = str(died_date).split('-')
                for i in range(0,len(splited_date_birth)):
                    isvalid = self.check_date(int(splited_date_birth[i]),int(splited_date_died[i]))
                    if isvalid == False:
                        raise forms.ValidationError({'died_date':'Died date must be high birth date'})       
        else:
            pass

    def check_date(self,field_value_birth,field_value_died):
        if int(field_value_birth) > int(field_value_died):
            return False