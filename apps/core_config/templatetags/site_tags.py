from django import template

from ..models import Config

register = template.Library()

@register.simple_tag
def name_site():
    config = Config.objects.filter().last()
   
    if config:
        return config.name
    return "Nome - longo"
    