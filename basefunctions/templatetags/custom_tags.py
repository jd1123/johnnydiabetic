from django import template
from johnnydiabetic.settings import SECURE_FILE_URL
import os

register = template.Library()

@register.simple_tag(takes_context=True)
def secure_file(context, filename = None , class_string = None):
    html_string = ''
    if context['user_authenticated']:
        if filename:
            html_string += "<img "
            
            if class_string:
                html_string += "class=" + class_string + " "
            
            html_string += "src='" + os.path.join(SECURE_FILE_URL, filename) + "'>"
            
    return html_string