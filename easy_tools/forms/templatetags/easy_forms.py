from django.utils.safestring import mark_safe
from django.conf import settings
from django import template
register = template.Library()


@register.simple_tag
def include_forms_css():
    includes = [
        'https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/themes/smoothness/jquery-ui.css',
        settings.STATIC_URL + 'css/jquery/pqselect.min.css',
        settings.STATIC_URL + 'css/jquery/pqselect.material.dev.css',
    ]

    template = map(lambda x: '<link href="{0}" rel="stylesheet">'.format(x), includes)
    return mark_safe('\n'.join(template))


@register.simple_tag
def include_forms_js():
    includes = [
        'https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js',
        settings.STATIC_URL + 'js/jquery/pqselect.min.js',
    ]

    template = map(lambda x: '<script src="{0}"></script>'.format(x), includes)
    return mark_safe('\n'.join(template))


@register.simple_tag
def multiple_select_as_tags(select_id):
    script_tpl = '<script type="text/javascript">' + \
        '$("#%s").pqSelect({multiplePlaceholder: "Select options",' % select_id + \
        'checkbox: true, maxDisplay: 10}).pqSelect();</script>'
    return mark_safe(script_tpl)
