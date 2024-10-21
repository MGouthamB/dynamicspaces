from django import template
import re

register = template.Library()

@register.filter
def split(value, delimiter=" "):
    values = value.split(delimiter)
    return values if value!='' else None

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter(name='strip_pnbsp')
def strip_pnbsp(value):
    value = re.sub(r'<p>(&nbsp;|\s)*</p>', '', value)
    value = re.sub(r'style="*"', '', value)
    return re.sub(r'<p>(&nbsp;|\s)*</p>', '', value)