
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.decorators import csrf

# 接收POST请求数据
def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)