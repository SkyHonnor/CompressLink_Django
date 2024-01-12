from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import *

from .forms import *

from datetime import datetime

import random as rd

from django.conf import settings

alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
# Create your views here.
def index(request):
    form = RedirectionTableForm()
    return render(request, 'index.html', {'form': form})


def redirection(request, code):
    url = RedirectionTable.objects.filter(coderedirection=code).first()

    if url:

        url.datederniereutilisation = datetime.now()
        url.nombreutilisation = url.nombreutilisation + 1

        url.save()

        return redirect(url.urlredirection)
    else:
        return HttpResponse('Not found')
    
def createlink(request):
    if request.method == 'POST':
        form = RedirectionTableForm(request.POST)
        if form.is_valid():

            dejaurl = RedirectionTable.objects.filter(urlredirection=form.cleaned_data['urlredirection']).first()

            code = ''

            if dejaurl:
                code = dejaurl.coderedirection
            else:
                redirection = RedirectionTable()

                codeverif = True
                while(codeverif):
                    code = ''.join(rd.choices(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"), k = 6))
                    if not RedirectionTable.objects.filter(coderedirection=code).first():
                        codeverif = False

                redirection.coderedirection = code
                redirection.urlredirection = form.cleaned_data['urlredirection']
                redirection.save()

            url = settings.IP + '/' + code
            return render(request, 'result.html', context={'url': url })
    else:
        form = RedirectionTableForm()

    return redirect('index')

