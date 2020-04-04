from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render,get_object_or_404
from .models import Khatm

# Create your views here.


class KhatmIndex(ListView):
    model = Khatm
    template_name='khatm/new_index.html'
    context_object_name = 'khatm'

    def get_queryset(self):
        return Khatm.objects.filter(selected=False).order_by('joz')

    def get_context_data(self,object_list=None,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']="ختم"
        return context

def add_hezb(request,khatm_id):

    khatm_obj = get_object_or_404(Khatm, id=khatm_id)
    khatm_obj.selected=True
    khatm_obj.save()

    return render(request,'khatm/single.html',{
        # 'title': article.title,
        'article': khatm_obj
    })