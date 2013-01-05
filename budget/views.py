# Create your views here.
import os, hashlib
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django import forms

class UploadFileForm(forms.Form):
    file  = forms.FileField()

def handle_uploaded_file(f):
    with open('./mint/mint/uploads/transaction.csv', 'wb+') as destination:
        for chunk in f.readlines():
		destination.write(chunk)
		m = hashlib.md5()
		transaction = Transaction.objects.create(key = m.update(chunk))
		print chunk.split(',')

def home(request):
	return render_to_response('index.html', RequestContext(request))

def upload_file(request):
    transactions = Transaction.objects.all()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/upload/')

    return render_to_response('upload.html', { 'transactions' : transactions }, RequestContext(request))
