from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from user.models import Nachid


class HomePageView(View):
    def get(self, request):
        all_nachid = Nachid.objects.all()
        context = {'nachid': all_nachid}
        return render(request, 'home_page.html', context)