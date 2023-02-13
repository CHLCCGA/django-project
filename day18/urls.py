"""day18 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01.views import account
from app01.views import order
from app01.views import user
from app01.views import work
from app01.views import tpl
from app01.views import my
from app01.views import checkout
from app01.views import upload

from django.views.static import serve
from django.urls import re_path
from django.conf import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', account.login, name='login'),
    path('logout/', account.logout, name='logout'),

    path('home/', account.home, name='home'),
    path('order/', order.order, name='order'),
    path('order/add/', order.order_add, name='order_add'),
    path('user/', user.user, name='user'),
    path('work/', work.work, name='work'),

    # 工单模板
    path('tpl/', tpl.tpl, name='tpl'),
    path('tpl/<int:pk>/edit/', tpl.tpl_edit, name='tpl_edit'),
    path('tpl/<int:pk>/delete/', tpl.tpl_delete, name='tpl_delete'),

    # 我的工单
    path('my/', my.my, name='my'),
    path('my/add/', my.my_add, name='my_add'),
    path('my/add/plus/', my.my_add_plus, name='my_add_plus'),

    # 工单审批
    path('checkout/', checkout.checkout, name='checkout'),
    path('checkout/action/<int:action>/<int:oid>/', checkout.checkout_action, name='checkout_action'),

    # 上传
    path('up/', upload.up, name='up'),
    path('up/form/', upload.up_form, name='up_form'),
    path('up/excel/', upload.up_excel, name='up_excel'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
]
