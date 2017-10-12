# -*- coding: utf-8 -*-
from django.shortcuts import render
import pytesseract
try:
    import Image
except ImportError:
    from PIL import Image
from .forms import InterpreteForm
import os
from django.conf import settings


def index(request):
    if request.method == 'POST':
        form = InterpreteForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            f = request.FILES['interprete_file']
            file_return = handle_uploaded_file(f)
            img = Image.open(file_return)
            # bg = Image.new("RGB", img.size, (255, 255, 255))
            # bg.paste(img, img)
            # text = pytesseract.image_to_string(bg)
            language = form.cleaned_data['language']
            text = pytesseract.image_to_string(img, lang=language)
            print(text)
            file_return = os.path.abspath(file_return)
            print(file_return)
            return render(request, 'core/index.html', {'result': text,
                                                       'reload': True,
                                                       'image_path': file_return})
    else:
        form = InterpreteForm()
    return render(request, 'core/index.html', {'form': form, 'reload': False})


def handle_uploaded_file(f):
    file_return = os.path.join(settings.MEDIA_ROOT, 'image_to_string.jpg')

    with open(file_return, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return file_return