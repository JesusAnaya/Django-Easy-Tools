from django.db import models
from django import forms
from easy_tools.forms.widgets import MultiSelectWidgetAsTags


class ManyToManyFieldAsTags(models.ManyToManyField):
    def formfield(self, **kwargs):
        defaults = {'widget': MultiSelectWidgetAsTags}
        defaults.update(kwargs)
        return super(ManyToManyFieldAsTags, self).formfield(**defaults)


class ModelMultipleChoiceFieldAsTags(forms.ModelMultipleChoiceField):
    def __init__(self, *args, **kwargs):
        kwargs['widget'] = MultiSelectWidgetAsTags
        super(ModelMultipleChoiceFieldAsTags, self).__init__(*args, **kwargs)
