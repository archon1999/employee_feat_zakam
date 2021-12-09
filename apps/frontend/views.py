from django.shortcuts import render
from django import views


class IndexView(views.View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name, {})
