from django import template

register = template.Library()

@register.filter(name='amcut')
def amcut(value,arg):
    """
    THIS CUTS value

    """
    return value.replace(arg,'')


#register.filter('cut',cut)
