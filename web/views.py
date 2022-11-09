from multiprocessing import context
from re import template
from unicodedata import category
from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (View, CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView)
from .models import *
from django.db.models import F
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.contrib.auth import logout as django_logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
#from next_prev import next_in_order, prev_in_order
from django.db.models import Count

from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q
from django.utils.decorators import method_decorator
from accounts.decorators import student_required
from django.contrib.auth.decorators import login_required
import random
import string
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.template.loader import render_to_string, get_template
from accounts.models import *



from django.conf import settings
from django.http.response import Http404
from django.core.mail import send_mail, BadHeaderError, EmailMessage


def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))






def Index(request):
    
    return render(request, "index.html")

