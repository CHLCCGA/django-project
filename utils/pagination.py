"""
视图函数：
    def depart_list(request):
        query = models.DepartMent.objects.all()
        pager = Pagination(request, query.count())
        queryset = query[pager.start:pager.end]

        context = {
            "queryset": queryset,
            "pager_string": pager.html()
        }
        return render(request, 'depart_list.html', context)
前端页面：
        {% for obj in queryset %}

        {% endfor %}

        <ul class="pagination">
            {{ pager_string }}
        </ul>

"""
import copy
from django.utils.safestring import mark_safe


class Pagination(object):

    def __init__(self, request, total_count):
        page = request.GET.get("page", "1")
        if not page.isdecimal():
            page = 1
        else:
            page = int(page)
            if page < 1:
                page = 1

        self.page = page
        self.start = (page - 1) * 10
        self.end = page * 10

        self.total_count = total_count
        total_page_count, div = divmod(total_count, 10)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count

        self.query_dict = copy.deepcopy(request.GET)
        self.query_dict._mutable = True

    def html(self):

        pager_list = []

        # 如果页码没有超过11
        if self.total_page_count <= 11:
            pager_start = 1
            pager_end = self.total_page_count + 1
        else:
            if self.page <= 5:
                pager_start = 1
                pager_end = 11 + 1
            else:
                if self.page + 5 > self.total_page_count:
                    pager_start = self.total_page_count - 10
                    pager_end = self.total_page_count + 1
                else:
                    # 当前后5个、当前前5个
                    pager_start = self.page - 5
                    pager_end = self.page + 5 + 1
        for i in range(pager_start, pager_end):
            self.query_dict.setlist("page", [i])
            query = self.query_dict.urlencode()
            if i == self.page:
                element = '<li class="active"><a href="?{0}">{1}</a></li>'.format(query, i)
            else:
                element = '<li><a href="?{0}">{1}</a></li>'.format(query, i)
            pager_list.append(element)
        pager_string = mark_safe("".join(pager_list))
        return pager_string
