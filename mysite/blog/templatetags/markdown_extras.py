#adds markdown ability in blog

from django import template
from django.template.defaultfilters import stringfilter

from django.utils.safestring import mark_safe
import markdown as md

register=template.Library()


@register.filter(is_safe=True)
@stringfilter

#figured out codehilite error. its not setting the class to .codehilite
def markdown(value):
    extras=['extra','codehilite']
    return mark_safe(md.markdown(value,extensions=extras))