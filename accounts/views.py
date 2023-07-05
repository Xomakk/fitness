from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View


@login_required
def buy(request):
    print(request.GET.get('program', None))
    return render(request, template_name="accounts/buy.html")


@login_required
def profile(request):
    return render(request, template_name="accounts/profile.html")
