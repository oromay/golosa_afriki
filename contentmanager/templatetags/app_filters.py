import re, math, datetime
from django import template
from django.utils.html import strip_tags

register = template.Library()

@register.filter(name='get_time_to_read')

def get_time_to_read(html_string):
    word_string = strip_tags(html_string)
    matching_words = re.findall(r'\w+', word_string)
    count = len(matching_words)
    read_time_min = math.ceil(count/150.0)
    read_time = str(datetime.timedelta(minutes=read_time_min))
    return("%s мин." % read_time_min)
