from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from utils.pagination import Pagination


def checkout(request):
    # 0.查询当前待审批工单的数量
    count = models.Order.objects.filter(leader_id=request.unicom_userid, status=1).count()

    # 1.查询自己待审批的工单
    queryset = models.Order.objects.filter(leader_id=request.unicom_userid).order_by('status', '-id')
    pager = Pagination(request, queryset.count())
    queryset = queryset[pager.start:pager.end]
    context = {
        "queryset": queryset,
        "pager_string": pager.html(),
        'count': count
    }

    return render(request, 'checkout.html', context)


def checkout_action(request, action, oid):
    # action=1  action=2   oid=订单ID
    if not action in [1, 2]:
        return HttpResponse("wrong")

    #
    import datetime
    ctime = datetime.datetime.now()
    if action == 1:
        models.Order.objects.filter(id=oid, status=1, leader_id=request.unicom_userid).update(status=2,update_datetime=ctime)
    else:
        models.Order.objects.filter(id=oid, status=1, leader_id=request.unicom_userid).update(status=3,update_datetime=ctime)

    return redirect('/checkout/')
