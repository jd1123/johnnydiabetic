from django import template
from johnnydiabetic.settings import SECURE_FILE_URL
import os

register = template.Library()

@register.simple_tag(takes_context=True)
def secure_file(context, filename = None , class_string = None):
    html_string = ''
    if context['user_authenticated']:
        if filename:
            no_ext = filename.split('.')[0]
            html_string += "<img "
            
            if class_string:
                html_string += "class=" + class_string + " "
            
            html_string += "src='" + os.path.join(SECURE_FILE_URL, filename) + "' alt='" +no_ext + "'>"
            
    return html_string

@register.simple_tag(takes_context=True)
def img_link(context, filename = None):
    html_string = ''
    if filename:
        html_string += "<img src='/static/img/" + filename + "'>"
    return html_string