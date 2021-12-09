from django.db import models
from django.utils.translation import gettext_lazy as _


class Department(models.Model):
    name = models.CharField(_('Name of department'), max_length=255)
    floor = models.IntegerField(_('Floor of the department'))

    class Meta:
        verbose_name = _('department')
        verbose_name_plural = _('departments')

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(_('Name of Programming Language'), max_length=255)

    class Meta:
        verbose_name = _('language')
        verbose_name_plural = _('languages')

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(_('First name'), max_length=255)
    last_name = models.CharField(_('Last name'), max_length=255)
    age = models.PositiveSmallIntegerField(_('Age'))
    department = models.ForeignKey(
        Department,
        verbose_name=_('Department of Employee'),
        related_name='employees',
        on_delete=models.CASCADE
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_('Language of Employee'),
        related_name='employees',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('employee')
        verbose_name_plural = _('employees')

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
