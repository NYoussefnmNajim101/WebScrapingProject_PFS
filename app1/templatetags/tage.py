from django import template
register = template.Library()

@register.simple_tag
def setvar(val=None):
  val+=1
  return val
