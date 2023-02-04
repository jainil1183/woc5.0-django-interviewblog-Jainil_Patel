from django.template.defaulttags import register

from django import template

from bs4 import BeautifulSoup

register = template.Library()

@register.filter
def cleanhtml(string):
    return BeautifulSoup(string,features='html.parser').text
