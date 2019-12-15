from django import template

register = template.Library()

@register.filter
def divide(A, B):
    return round(A / B * 100, 2)

@register.filter
def exists(A):
    return A.meeting is not None
