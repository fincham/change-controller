from __future__ import unicode_literals
from django.core.files.storage import default_storage

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from django import forms
from django.forms.models import inlineformset_factory

from django.contrib import messages

from .models import *

from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSet
from extra_views.generic import GenericInlineFormSet


class CommentForm(forms.Form):
    RESOLUTIONS = (
        ('approve', 'Approve'),
        ('reject', 'Reject'),
        ('nothing', 'Comment only'),        
    )
    text = forms.CharField()
    resolve = forms.ChoiceField(choices=RESOLUTIONS)

class AnswerInline(InlineFormSet):
    model = Answer
    fields = ["text"]

class RequestList(ListView):
    model = Request

class RevisionCreate(CreateWithInlinesView):
    model = Revision
    fields = ['implemented']
    inlines = [AnswerInline]

class RequestDetail(DetailView):
    model = Request

    def get_context_data(self, **kwargs):
        context = super(RequestDetail, self).get_context_data(**kwargs)
        try:
            context['revision'] = Revision.objects.get(id=self.kwargs.get('version', context['object'].revision_set.first().id))
        except:
            pass
        return context    

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['resolve'] == 'approve':
                resolution_dict = {'approves': True}
            elif form.cleaned_data['resolve'] == 'reject':
                resolution_dict = {'rejects': True}
            else:
                resolution_dict = {}

            comment = Comment(user=request.user, text=form.cleaned_data['text'], revision=Revision.objects.get(id=self.kwargs.get('version', self.get_object().latest_revision().id)), **resolution_dict)
            comment.save()
        else:
            messages.add_message(request, messages.INFO, 'Bad form.')
        return self.get(request, *args, **kwargs)
