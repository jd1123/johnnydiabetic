from django import template
from johnnydiabetic.settings import SECURE_FILE_URL
import os

register = template.Library()

@register.simple_tag
def secure_file(filename):
    if filename:
        return os.path.join(SECURE_FILE_URL, filename) 
    else:
        return ''