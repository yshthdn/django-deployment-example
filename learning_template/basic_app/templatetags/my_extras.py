from django import template

register=template.Library()

@register.filter(name='cutt')
def cutt(value, arg):
    """
    This cut's out all value of args from the string
    """
    return value.replace(arg,'')

# register.filter('cutt',cutt)
