from django import template
import datetime

register = template.Library()

@register.filter
def slashed_date(value):
    """Converts dates with YYYY-MM-DD to DD/MM/YYYY"""

    try: 
        date = datetime.datetime.strptime(value, "%Y-%m-%d").strftime("%d/%m/%Y")
    except:    
        date = datetime.date.today().strftime("%d/%m/%Y")

    return date

@register.filter
def dashed_date(value):
    """Converts dates with YYYY-MM-DD to DD/MM/YYYY"""

    try: 
        date = datetime.datetime.strptime(value, "%d/%m/%Y").strftime("%d-%m-%Y")
    except:    
        date = datetime.date.today().strftime("%d-%m-%Y")

    return date

@register.filter
def text_date(value):
    """Converts dates with dd B YYYY to DD/MM/YYYY"""

    try: 
        date = datetime.date.today().strftime("%d-%m-%Y")
    except:    
        date = "Sorry and error has occured with your date."
        
    return date

@register.filter
def minus_date(value):
    """Converts dates with dd B YYYY to DD/MM/YYYY"""

    try: 
        value = datetime.datetime.strptime(value, "%d %B %Y")
        day = datetime.timedelta(1)
        new_date = value - day
        date = new_date.strftime("%d-%m-%Y")
    except:    
        date = datetime.date.today().strftime("%d-%m-%Y")
        
    return date

@register.filter
def plus_date(value):
    """Converts dates with dd B YYYY to DD/MM/YYYY"""

    try: 
        value = datetime.datetime.strptime(value, "%d %B %Y")
        day = datetime.timedelta(1)
        new_date = value + day     
        date = new_date.strftime("%d-%m-%Y")
    except:    
        date = datetime.date.today().strftime("%d-%m-%Y")
        
    return date