from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect
from django.conf import settings


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 0.无需登录的地址，放行
        if request.path_info in ["/login/", '/logout/']:
            return

        # 1.获取用户session信息
        # {"id": admin_object.id, 'username': admin_object.username}
        user_info = request.session.get("user_info")

        # 2.有值，表示已登录，则继续
        if user_info:
            request.unicom_userid = user_info['id']
            request.unicom_username = user_info['username']
            request.unicom_role = user_info['role']
            return

        # 3.无值=None
        return redirect('/login/')

    def process_view(self, request, view_func, args, kwargs):
        if request.path_info in ["/login/", '/logout/']:
            return
        # 1.当前用户角色
        role = request.unicom_role
        # 2.自己具备的权限
        user_permission_set = settings.UNICOM_PERMISSION[role]

        # 3.是否具有权限（有权限)
        if request.resolver_match.url_name in user_permission_set:
            return

        # 4.无权限
        return HttpResponse("无权访问")
