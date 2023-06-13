from django import template

register = template.Library()

@register.filter()
def format_name(value):
    arr = value.split("_")
    display = arr[0] + " " + str(int(arr[1]) + 1)
    return display