from django.template import Library
from django.conf import settings
import copy

register = Library()


@register.inclusion_tag('menu.html')
def unicom_menu(request):
    # 0.当前用是什么角色？
    role = request.unicom_role

    # 1.去session中获取所有菜单信息
    user_menu_list = copy.deepcopy(settings.UNICOM_MENU[role])
    """
    user_menu_list = [
        {"text": "user", 'url': "/user/",},
        {"text": "order", 'url': "/order/", 'class':"active"},
        {"text": "task", 'url': "/work/"},
    ]
    """
    for row in user_menu_list:
        if request.path_info.startswith(row['url']):
            row['class'] = 'active'

    return {'menu_list': user_menu_list}
