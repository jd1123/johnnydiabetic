from django import template
from johnnydiabetic.settings import SECURE_FILE_URL
import os

register = template.Library()


@register.simple_tag(takes_context=True)
def file_url(context, filename=None):
    if filename:
        return os.path.join(SECURE_FILE_URL, filename)
    else:
        return "#"


@register.simple_tag(takes_context=True)
def secure_file(context, filename=None, alt_text=None, class_string=None):

    html_string = ''
    if context['user_authenticated']:
        if filename:
            html_string += "<img "

            if class_string:
                html_string += "class=" + class_string + " "

            html_string += "src='" + os.path.join(SECURE_FILE_URL, filename)

            if alt_text:
                html_string += "' alt='" + alt_text

            html_string += "'>"

    return html_string


@register.simple_tag(takes_context=True)
def secure_tn(context, filename=None, alt_text=None, class_string=None):
    html_string = ''
    if context['user_authenticated']:
        if filename:
            filename = 'tn' + filename

            html_string += "<img "

            if class_string:
                html_string += "class=" + class_string + " "

            fileURL = os.path.join(SECURE_FILE_URL, 'thumbs')
            html_string += "src='" + os.path.join(fileURL, filename)

            if alt_text:
                html_string += "' alt='" + alt_text

            html_string += "'>"

    return html_string


@register.simple_tag(takes_context=True)
def img_link(context, filename=None):
    html_string = ''
    if filename:
        html_string += "<img src='/static/img/" + filename + "'>"
    return html_string
