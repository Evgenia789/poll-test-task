from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    """
    Функция для добавления CSS-классов к любому полю формы.
    """
    return field.as_widget(attrs={'class': css})
