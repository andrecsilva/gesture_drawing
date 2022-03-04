from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from .models import Reference,Tag
from .forms import SessionForm,NewTagForm

from django.template import loader
from django.template.response import TemplateResponse

from django.core.paginator import Paginator

from django.views.generic.list import ListView

import random

# Create your views here.

def reference(request,ref_id):
    ref = get_object_or_404(Reference,pk=ref_id)
    ref_tags = ref.tags.all()
    template = loader.get_template('gesture/ref_view.html')
    all_tags = Tag.objects.all().difference(ref_tags)
    context = {
        'ref' : ref,
        'ref_tags' : ref_tags,
        'all_tags' : all_tags,
    }
    return HttpResponse(template.render(context,request))

def tag(request,tag_id):
    tag = get_object_or_404(Tag,pk=tag_id)
    ref_set = tag.reference_set.all()
    template = loader.get_template('gesture/tag_view.html')
    context = {
            'tag' : tag,
            'ref_set' : ref_set,
            'ref_count' : ref_set.count(),
    }
    return HttpResponse(template.render(context,request))

def index(request):
    template = loader.get_template('gesture/index.html')
    session_form = SessionForm()
    context = {
            'session_form':session_form,
            }
    return TemplateResponse(request,template,context)

def untagged_refs(request):
    ref_set = Reference.objects.filter(tags__isnull=True)

    context = {
            'ref_set' : ref_set,
            'ref_count' : ref_set.count(),
    }

    template = loader.get_template('gesture/untagged_refs.html')
    return HttpResponse(template.render(context,request))

def session(request):
    session_form = SessionForm(request.POST)
    if session_form.is_valid():

        ref_count = session_form.cleaned_data['ref_count']
        if session_form.cleaned_data['tags_filter']:
            ht,*tl = session_form.cleaned_data['tags_filter']
            union = ht.reference_set.all().union(*[t.reference_set.all() for t in tl])
        else:
            union = Reference.objects.all()
            
        indexes = random.sample(range(0,union.count()),min(ref_count,union.count()))
        ref_set = [union[i] for i in indexes]

        template = loader.get_template('gesture/session.html')
        context = {
                'ref_set' : ref_set,
                'ref_count' : ref_count,
        }

        return HttpResponse(template.render(context,request))
    else:
        return HttpResponseRedirect(reverse('gesture:index'));

def add_new_tag(request):
    tag_name = request.POST['tag_name']
    tag_description = request.POST['tag_description']
    t = Tag(name=tag_name,description=tag_description)
    t.save()

    return HttpResponseRedirect(reverse('gesture:tag_list'));

def add_tag_to_ref(request,ref_id):
    tags_id = request.POST.getlist('tags_id')

    if tags_id:
        r = Reference.objects.get(pk=ref_id)
        r.tags.add(*tags_id)

    #return HttpResponse(str(tags_id))
    return HttpResponseRedirect(reverse('gesture:reference',args=(ref_id,)));

def remove_tag_from_ref(request,ref_id):
    tags_id = request.POST.getlist('tags_id')

    if tags_id:
        r = Reference.objects.get(pk=ref_id)
        r.tags.remove(*tags_id)

    #return HttpResponse(str(tags_id))
    return HttpResponseRedirect(reverse('gesture:reference',args=(ref_id,)));


class TagListView(ListView):
    template_name = 'gesture/tag_list.html'
    context_object_name = 'tag_list'

    def get_queryset(self):
        return [(t,t.reference_set.count()) for t in Tag.objects.order_by('name')]

    def get_context_data(self,**kwargs):
        context = super(TagListView,self).get_context_data(**kwargs)
        new_tag_form = NewTagForm()
        context['tag_count'] = Tag.objects.count()
        context['new_tag_form'] = new_tag_form
        return context

