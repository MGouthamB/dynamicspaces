from django import template

register = template.Library()

@register.filter
def split(value, delimiter=" "):
    values = value.split(delimiter)
    return values if value!='' else None