from django import template
import datetime
import time
import pytz
from datetime import date, timedelta

register = template.Library()# Create your models here.

@register.filter(name='cumple')
def myBirthday(val):
    hoy= datetime.datetime.now()
    cumple=val.replace(year=hoy.year,tzinfo=pytz.timezone('America/Managua'))
# Right way!
    hoy = pytz.timezone('America/Managua').localize(hoy)


    if cumple > hoy:
        return cumple
    else:
    	y=hoy.year
    	y=y+1
        cumple=cumple.replace(year=y)
        return cumple