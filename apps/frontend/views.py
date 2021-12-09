from django.shortcuts import render
from django import views
from django.http.response import JsonResponse

from apps.backend.models import Employee, Department, Language
from apps.frontend.forms import EmployeeAddForm


class IndexView(views.View):
    template_name = 'index.html'

    def get(self, request):
        employees = Employee.objects.all()
        name_tags = list(Employee.objects.all().values_list('first_name',
                                                            flat=True))
        deparments = Department.objects.all()
        languages = Language.objects.all()
        return render(request, self.template_name, {
            'employees': employees,
            'name_tags': name_tags,
            'departments': deparments,
            'languages': languages,
        })


class EmployeeAddView(views.View):

    def post(self, request):
        form = EmployeeAddForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            department_id = form.cleaned_data['department']
            department = Department.objects.get(id=department_id)
            language_id = form.cleaned_data['language']
            language = Language.objects.get(id=language_id)
            employee = Employee.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                department=department,
                language=language,
            )
            return JsonResponse({'success': True, 'id': employee.id,
                                 'department': department.name,
                                 'language': language.name})
        else:
            return JsonResponse({'success': False})
