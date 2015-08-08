from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe


class MultiSelectWidgetAsTags(forms.SelectMultiple):
    class Media:
        css = {
            'all': (
                'https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/themes/smoothness/jquery-ui.css',
                settings.STATIC_URL + 'css/jquery/pqselect.min.css',
                settings.STATIC_URL + 'css/jquery/pqselect.material.dev.css',
            )
        }
        js = (
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js',
            settings.STATIC_URL + 'js/jquery/pqselect.min.js',
        )

    def render(self, name, value, attrs=None):
        rendered = super(MultiSelectWidgetAsTags, self).render(name, value, attrs)
        script_tpl = u'''<script type="text/javascript">
            $("#{0}_id").pqSelect({
                multiplePlaceholder: 'Select Countries',
                checkbox: true,
                maxDisplay: 10
            }).pqSelect( 'open' );
        </script>
        '''
        return '' #rendered + mark_safe(script_tpl.format(name))
