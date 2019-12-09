from django import template

register = template.Library()

@register.filter
def humanize(value): # Only one argument.
    """Converts underscores into spaces"""
    return value.replace("_", " ")