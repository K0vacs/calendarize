from django import template

register = template.Library()

@register.filter
def humanize(value):
    """Converts underscores into spaces"""
    return value.replace("_", " ")