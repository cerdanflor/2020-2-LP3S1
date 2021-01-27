from django import forms

class FormArticulo(forms.Form):
    titulo = forms.CharField(
        label="Titulo",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el título',
                'class': 'titulo_form_articulo'
            }
        )
    )

    contenido = forms.CharField(
        label="Contenido",
        widget=forms.Textarea        
    )
    contenido.widget.attrs.update({
        'placeholder': 'Ingrese el contenido del artículo',
        'class': 'contenido_form_articulo',
        'id':'contenido_form'
    })

    opciones_publicado = [
        (1,'Si'),
        (0,'No'),
    ]
    publicado = forms.TypedChoiceField(
        label="¿Publicado?",
        choices=opciones_publicado
    )