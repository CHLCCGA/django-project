from django.shortcuts import render, redirect
from app01 import models
from utils.pagination import Pagination
from utils.bootstrap import BootStrapModelForm
from datetime import datetime
from django.http import JsonResponse
from django import forms


class MyModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        fields = ['tpl', ]


def my(request):
    form = MyModelForm()
    queryset = models.Order.objects.filter(user_id=request.unicom_userid)
    pager = Pagination(request, queryset.count())
    queryset = queryset[pager.start:pager.end]
    context = {
        "queryset": queryset,
        "pager_string": pager.html(),
        'form': form
    }
    return render(request, 'my.html', context)


def my_add(request):
    """ 创建工单 """
    if request.method == "GET":
        form = MyModelForm()
        return render(request, 'my_add.html', {"form": form})

    form = MyModelForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'my_add.html', {"form": form})

    tpl_object = form.cleaned_data['tpl']
    form.instance.user_id = request.unicom_userid
    form.instance.leader_id = tpl_object.leader_id
    form.instance.create_datetime = datetime.now()
    form.save()
    return redirect('/my/')


def my_add_plus(request):
    """ ajax提交并创建 """
    form = MyModelForm(data=request.POST)
    if not form.is_valid():
        return JsonResponse({'status': False, 'error': form.errors})

    tpl_object = form.cleaned_data['tpl']
    form.instance.user_id = request.unicom_userid
    form.instance.leader_id = tpl_object.leader_id
    form.instance.create_datetime = datetime.now()
    form.save()
    return JsonResponse({'status': True})
