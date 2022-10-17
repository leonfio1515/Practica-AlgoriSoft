from django.forms import *
from .models import *

class CategoryForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs["class"] = "form-control"
        #     form.field.widget.attrs["autocomplete"] = "off"
        # self.fields["name"].widget.attrs["autofocus"] = True


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

