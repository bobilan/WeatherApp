from django import template

register = template.Library()


@register.filter(name='uppercase')
def uppercase_filter(value):
    return value.upper()
