from django import template

register = template.Library()


@register.filter(name='addclass')
def addclass(value, arg):
    print(type(value))
    print(value.name)
    return value.as_widget(attrs={'class': arg, 'placeholder': value.name})
