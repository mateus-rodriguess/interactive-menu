from django import template

from ..models import Config

register = template.Library()

@register.simple_tag
def name_site():
    config = Config.objects.filter().last()
    return config.name

    