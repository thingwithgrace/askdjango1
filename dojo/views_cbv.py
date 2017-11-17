from django.views.generic import View, TemplateView
from django.http import HttpResponse, JsonResponse

class PostListView1(View):
    def get(self, request):
        name = '공유'
        html = '''
         <h1>AskDjango</h1>
    <p>{name}</p>
    <p>여러분의 페이스메이커가 되어드림</p>
        '''.format(name=name)
        return HttpResponse(html)
    pass

post_list1 = PostListView1.as_view()

class PostListView2(TemplateView):
    template_name = 'dojo/post_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = '공유'
        return context

post_list2 = PostListView2.as_view()

class PostListView3(object):
    pass


class ExcelDownloadView(object):
    pass