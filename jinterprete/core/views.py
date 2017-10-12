# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import pytesseract
try:
    import Image
except ImportError:
    from PIL import Image
import os
from .forms import InterpreteForm


def index(request):
    '''
    template = loader.get_template('core/index.html')
    context = {}

    return HttpResponse(template.render(context, request))
    '''
    if request.method == 'POST':
        form = InterpreteForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            f = request.FILES['interprete_file']
            print(f)
            handle_uploaded_file(f)
            img = Image.open('name.jpg')
            bg = Image.new("RGB", img.size, (255, 255, 255))
            bg.paste(img, img)
            text = pytesseract.image_to_string(bg)
            print(text)
            return render(request, 'core/index.html', {'result': text})
    else:
        form = InterpreteForm()
    return render(request, 'core/index.html', {'form': form})


def handle_uploaded_file(f):
    with open('name.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)