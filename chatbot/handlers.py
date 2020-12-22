#!/usr/bin/env python3
import re


re_city = re.compile(r'^[\w\-\s]{3,40}$')
re_date = re.compile(r'^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$')
re_phone_number = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]') #re.findall(r'\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4}')


def handler_city_dep(text, context):
    match = re.match(re_city, text)
    if match:
        context['city_dep'] = text
        return True
    else:
        return False


def handler_city_arr(text, context):
    match = re.match(re_city, text)
    if match:
        context['city_arr'] = text
        return True
    else:
        return False


def handler_date(text, context):
    matches = re.findall(re_date, text)
    if len(matches) > 0:
        context['handler_date'] = matches[0]
        return True
    else:
        return False


def handler_flight(text, context):
    matches = re.findall(re_date, text)
    if len(matches) > 0:
        context['flight'] = matches[0]
        return True
    else:
        return False


def handler_phone_number(text, context):
    matches = re.findall(re_phone_number, text)
    if len(matches) > 0:
        context['phone_number'] = matches[0]
        return True
    else:
        return False
