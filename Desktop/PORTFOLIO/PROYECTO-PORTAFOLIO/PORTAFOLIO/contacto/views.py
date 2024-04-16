from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

from .forms import CustomContactForm
from django.contrib import messages


def contacto(request):
    if request.method == 'POST':
        form = CustomContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            
            template = render_to_string('contacto/email_template.html', {
                'nombre': nombre,
                'email': email,
                'mensaje': mensaje,
            })
            
            email = EmailMessage(
                'Asunto del correo',
                template,
                settings.EMAIL_HOST_USER,
                ['rommibu79@gmail.com']
            )
            
            email.fail_silently = False
            email.send()
            
            messages.success(request, 'Recibiré tu mensaje')
            return redirect('agradecimiento')
    else:
        form = CustomContactForm()
    
    return render(request, 'contacto/contacto.html', {'form': form})
