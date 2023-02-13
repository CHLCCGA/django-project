# README

---

+ ### overview

This project uses the python web framework to connect django and mysql to add, delete and modify personnel information.

+ ### env

	+ IDE: Pycharm & Vscode
	+ Language: Python
	+ Framework: Django
	+ Database: MySQL

+ ### Introduction

	+ log in
	+ homepage (show different page to leader and user)
	+ template mytask & menage page (leader creat template like sick, then user are able to apply for template sick, after that leader can dicide to pass the application or not )
	+ upload files

+ ### details

>*middleware to check if user were logged in and the role of user(user or leader)*
>
>```python
>class AuthMiddleware(MiddlewareMixin):
>    def process_request(self, request):
>        # 0.无需登录的地址，放行
>        if request.path_info in ["/login/", '/logout/']:
>            return
>
>        # 1.获取用户session信息
>        # {"id": admin_object.id, 'username': admin_object.username}
>        user_info = request.session.get("user_info")
>
>        # 2.有值，表示已登录，则继续
>        if user_info:
>            request.unicom_userid = user_info['id']
>            request.unicom_username = user_info['username']
>            request.unicom_role = user_info['role']
>            return
>
>        # 3.无值=None
>        return redirect('/login/')
>
>    def process_view(self, request, view_func, args, kwargs):
>        if request.path_info in ["/login/", '/logout/']:
>            return
>        # 1.当前用户角色
>        role = request.unicom_role
>        # 2.自己具备的权限
>        user_permission_set = settings.UNICOM_PERMISSION[role]
>
>        # 3.是否具有权限（有权限)
>        if request.resolver_match.url_name in user_permission_set:
>            return
>
>        # 4.无权限
>        return HttpResponse("无权访问")
>```

>*what user can use and what leader can use*
>
>```python
>UNICOM_MENU = {
>    'leader': [
>        {"text": "templete", 'url': "/tpl/"},
>        {"text": "my task", 'url': "/my/"},
>        {"text": "memage", 'url': "/checkout/"},
>        {"text": "upload", 'url': "/up/"},
>        {"text": "form upload", 'url': "/up/form/"},
>        {"text": "Excel upload ", 'url': "/up/excel/"},
>    ],
>    'user': [
>        {"text": "my task", 'url': "/my/"},
>    ]
>}
>
>```
>
>

>*pagination part *
>
>```python
>class Pagination(object):
>
>    def __init__(self, request, total_count):
>        page = request.GET.get("page", "1")
>        if not page.isdecimal():
>            page = 1
>        else:
>            page = int(page)
>            if page < 1:
>                page = 1
>
>        self.page = page
>        self.start = (page - 1) * 10
>        self.end = page * 10
>
>        self.total_count = total_count
>        total_page_count, div = divmod(total_count, 10)
>        if div:
>            total_page_count += 1
>        self.total_page_count = total_page_count
>
>        self.query_dict = copy.deepcopy(request.GET)
>        self.query_dict._mutable = True
>
>    def html(self):
>
>        pager_list = []
>
>        # 如果页码没有超过11
>        if self.total_page_count <= 11:
>            pager_start = 1
>            pager_end = self.total_page_count + 1
>        else:
>            if self.page <= 5:
>                pager_start = 1
>                pager_end = 11 + 1
>            else:
>                if self.page + 5 > self.total_page_count:
>                    pager_start = self.total_page_count - 10
>                    pager_end = self.total_page_count + 1
>                else:
>                    # 当前后5个、当前前5个
>                    pager_start = self.page - 5
>                    pager_end = self.page + 5 + 1
>        for i in range(pager_start, pager_end):
>            self.query_dict.setlist("page", [i])
>            query = self.query_dict.urlencode()
>            if i == self.page:
>                element = '<li class="active"><a href="?{0}">{1}</a></li>'.format(query, i)
>            else:
>                element = '<li><a href="?{0}">{1}</a></li>'.format(query, i)
>            pager_list.append(element)
>        pager_string = mark_safe("".join(pager_list))
>        return pager_string
>
>```
>
>

>*connect to database*
>
>```python
>DATABASES = {
>    'default': {
>        'ENGINE': 'django.db.backends.mysql',
>        'NAME': 'web',  # 数据库名字
>        'USER': 'root',
>        'PASSWORD': 'root123',
>        'HOST': '127.0.0.1',
>        'PORT': 3306
>    }
>}
>
>```
>
>

>*ajax : send url to beckend*
>
>```javascript
>$.ajax({
>                url: "/tpl/" + DELETE_ID + "/delete/",   //
>                type: "GET",
>                dataType: "JSON",
>                success: function (res) {
>                    if (res.status) {
>                        // 删除成功
>                        $('#myDeleteModal').modal('hide');
>                        location.href = location.href;
>                        //location.reload();
>
>                    } else {
>                        // 删除失败
>                        alert("try again");
>                    }
>```

+ ### pictures

