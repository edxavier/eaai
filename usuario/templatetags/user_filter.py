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

@register.filter(name='file_format')
def file_format(val,pattron):
    FORMATS = (".jpg","jpeg","pdf","rar","zip","doc","docx","gif","png","wav","txt","log","mp4","ptt","xls","pttx","xlsx","mp3")
    res = val.__str__().split(pattron)
    format = res[-1]
    if format in FORMATS:
        return  format
    else:
        return "unknow"


@register.filter(name='split')
def file_format(val,pattron):
    return val.__str__().split(pattron)

@register.filter(name='file_type')
def file_format_split(format):
    IMGS = (".jpg",".jpeg",".gif",".png",)
    AUDIO = (".wav",".mp3",".wma")
    VIDEO = (".avi",".mp4",".mpeg")
    print "valor de format "+format
    if format in IMGS:
        return  "image"
    elif format in AUDIO:
        return "audio"
    elif format in VIDEO:
        return "video"
    else:
        return "file"