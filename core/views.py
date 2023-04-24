from django.views.generic import View
from django.shortcuts import render

class homeview(View):
    def get(self, request, *agrs, **kagrs):
        return render(request, "index.html",{})