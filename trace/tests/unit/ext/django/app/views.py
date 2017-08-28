# Copyright 2017, OpenCensus Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.http import HttpResponse
from django.shortcuts import render

from .forms import HelloForm
import time

def home(request):
    time.sleep(1)
    return render(request, 'home.html')

def greetings(request):
    time.sleep(1)
    if request.method == 'POST':
        form = HelloForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['fname']
            last_name = form.cleaned_data['lname']
            return HttpResponse(
                "Hello, {} {}".format(first_name, last_name))
        else:
            return render(request, 'home.html')

    return render(request, 'home.html')

def health_check(request):
    return HttpResponse("ok", status=200)

def get_request_header(request):
    return HttpResponse(request.META.get('HTTP_X_CLOUD_TRACE_CONTEXT'))