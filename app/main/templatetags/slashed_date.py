from django import template
import datetime

register = template.Library()

@register.filter
def slashed_date(value):
    """Converts dates with YYYY-MM-DD to DD/MM/YYYY"""
    return datetime.datetime.strptime(value, "%Y-%m-%d").strftime("%d/%m/%Y")