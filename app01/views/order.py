from django.shortcuts import render


def order(request):
    return render(request, 'order.html')


def order_add(request):
    return render(request, 'order_add.html')
