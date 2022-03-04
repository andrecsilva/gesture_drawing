from django import template
from django.core.paginator import Paginator

register = template.Library()

@register.inclusion_tag('gesture/gallery.html',takes_context=True)
def gallery(context,ref_set):
    paginator = Paginator(ref_set,30)
    page_number = context['request'].GET.get('page')
    page_obj = paginator.get_page(page_number)

    new_context = {

            'page_obj' : page_obj,
            #'ref_count' : ref_set.count(),
    }
    return new_context

