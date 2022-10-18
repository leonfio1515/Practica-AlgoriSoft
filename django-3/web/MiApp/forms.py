from django.forms import *
from .models import *

class CategoryForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            'name': TextInput(
                attrs = {
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'desc': Textarea(
                attrs = {
                    'placeholder': 'Ingrese un nombre',
                    'rows': 3,
                    'cols': 3,
                }
            ),            
        }
        exclude = ["user_updated", "user_creation"]

    def save(self, commit=True):
        data= {}
        form=super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class ClientForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["names"].widget.attrs["autofocus"] = True

        class Meta:
            model = Client
            fields = "__all__"
            widgets = {
                "names":TextInput(
                    attrs={
                        "placeholder":"Ingrese sus nombres"
                    }
                ),
                "surnames":TextInput(
                    attrs={
                        "placeholder":"Ingrese sus apellidos"
                    }
                ),
                "DNI":TextInput(
                    attrs={
                        "placeholder":"Ingrese sus dni"
                    }
                ),
                "date_birthday":DateInput(format="%Y-%m-%d",
                    attrs={
                        "value": datetime.now().strftime("%Y-%m-%d")
                    }
                ),
                "address":TextInput(
                    attrs={
                        "placeholder":"Ingrese su direccion"
                    }
                ),
                "gender":Select()
                    }
            exclude = ["user_updated","user_creation"]

    def save(self,commit=True):
        data={}
        form=super()
        try:
            if form.is_valid():
                form.save()
            else:
                data["error"] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

