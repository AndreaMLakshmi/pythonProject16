from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from django.views import View
from django.views import View
from .forms import ContactForm

import json

import datetime
import os
import json

def home(request):
    return render(request, 'home.html')

AUTH_TOKEN="042081c872f8ecd903390df216659966286d74eb"

def authenticate(token):
    if token == AUTH_TOKEN:
        return True
    else:
        return False

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        print(name, email)
    form = ContactForm()
    return render(request, 'form.html', {'form': form})

from django.views.decorators.csrf import csrf_exempt

#@require_http_methods(["GET"],)
#def get_current_server_time(request):
#    return HttpResponse(datetime.datetime.now())

@csrf_exempt
@require_http_methods(["POST"],)
def upload_file(request):
    file = request.FILES['text']
    with open(file.name, 'wb') as dst:
        for chunk in file.chunks():
            dst.write(chunk)
        return HttpResponse(status=200)

@require_http_methods(["HEAD"])
def check_connection(request):
    response = HttpResponse(status=200)
    response['Server_Status'] = 'Up'
    response['Up_time'] = os.popen('uptime -p').read()[:-1]
    return response
import json
@csrf_exempt

@require_http_methods(["PUT"])
def save_json_to_file(request):
    json.loads
    data = json.loads(request.body)
    json_object = json.dumps(data, indent=4)

    with open("JSON_Data.json", "a") as f:
        f.write(json_object)

    return HttpResponse(status=200)

import os
@csrf_exempt
@require_http_methods(["DELETE"],)
def delete_filecurl(request):
    try:
        os.remove(request.body)
        return HttpResponse(status=200)
    except OSError:
        return HttpResponse(status=500)

import os
@csrf_exempt
@require_http_methods(["DELETE"],)
def delete_file(request):
    data = json.loads(request.body)
    try:
        os.remove('My_Files/' + data['file_name'])
        return HttpResponse(status=200)
    except OSError:
        return HttpResponse(status=500)


@csrf_exempt
@require_http_methods(["PATCH"])
def update_file(request):
    data = json.loads(request.body)
    with open('records.txt', 'a') as f:
        f.write(data['updates'])
        return HttpResponse(status=200)

from django.http import HttpResponse
from django.views import View
import json
class AddViewcurl(View):
    def get(self, request):
        inputstring = str(request.body)
        inputlist = inputstring.split(",")
        num01 = float(inputlist[1])
        num02 = float(inputlist[2])
        return HttpResponse(num01 + num02)

class AddView(View):
    def get(self, request):
        if not authenticate(request.headers['Auth-Token']):
            return HttpResponse(status=403)

        num01 = float(json.loads(request.body)['num01'])
        num02 = float(json.loads(request.body)['num02'])
        return HttpResponse(num01 + num02)

    def post(self, request, *args, **kwargs):
        if not authenticate(request.headers['Authorization']):
            return HttpResponse(status=403)
        num01 = float(request.POST['num01'])
        num02 = float(request.POST['num02'])
        return HttpResponse(num01 + num02)


class SubView(View):
    def get(self, request):
        if not authenticate(request.headers['Auth-Token']):
            return HttpResponse(status=403)
        num01 = float(json.loads(request.body)['num01'])
        num02 = float(json.loads(request.body)['num02'])
        return HttpResponse(num01 - num02)

    def post(self, request, *args, **kwargs):
        if not authenticate(request.headers['Authorization']):
            return HttpResponse(status=403)
        num01 = float(request.POST['num01'])
        num02 = float(request.POST['num02'])
        return HttpResponse(num01 - num02)


class DivView(View):
    def get(self, request):
        if not authenticate(request.headers['Auth-Token']):
            return HttpResponse(status=403)
        num01 = float(json.loads(request.body)['num01'])
        num02 = float(json.loads(request.body)['num02'])
        if num02 == 0.0:
            return HttpResponse("Cannot divide by 0")
        else:
            return HttpResponse(num01 / num02)

    def post(self, request, *args, **kwargs):
        if not authenticate(request.headers['Authorization']):
            return HttpResponse(status=403)
        num01 = float(request.POST['num01'])
        num02 = float(request.POST['num02'])
        if num02 == 0.0:
            return HttpResponse("Cannot divide by 0")
        else:
            return HttpResponse(num01 / num02)

class MultiView(View):
    def get(self, request):
        if not authenticate(request.headers['Auth-Token']):
            return HttpResponse(status=403)
        num01 = float(json.loads(request.body)['num01'])
        num02 = float(json.loads(request.body)['num02'])
        return HttpResponse(num01 * num02)

    def post(self, request, *args, **kwargs):
        if not authenticate(request.headers['Authorization']):
            return HttpResponse(status=403)
        num01 = float(request.POST['num01'])
        num02 = float(request.POST['num02'])
        return HttpResponse(num01 * num02)
