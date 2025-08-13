from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            # Quitar los textos de ayuda predeterminados
            self.fields[fieldname].help_text = None
            # Agregar clases de Bootstrap para estilo
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})
