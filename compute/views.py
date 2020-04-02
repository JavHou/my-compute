from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.sessions.backends.db import SessionStore

from compute.models import *
# Create your views here.


#纯js实现计算器
def computev1(request):
    return render(request, 'compute.html')

# AJAX实现计算器
def compute_ajax(request):
    return render(request, 'compute-ajax.html')

#AJAX返回计算结果
def result(request):
    input_str = request.GET.get('input_str')
    try:
        res = eval(input_str)
        return JsonResponse({"result": res})
    except Exception:
        return JsonResponse({"result": "error"})

#带history的用户登录界面
def login(request):
    message = ""
    v = request.session
    print(type(v))
    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        c = User.objects.filter(
            username=user, password=pwd).count()
        if c:
            # 设置session用于后续登录会话保持
            request.session['is_login'] = True
            request.session['username'] = user
            rep = redirect('/compute-history')
            return rep
        else:
            message = "用户名或密码错误"
    obj = render(request, 'login.html', {'msg': message})
    return obj

#验证是否登录
def auth(func):
    def inner(request, *args, **kwargs):
        is_login = request.session.get('is_login')
        if is_login:
            return func(request, *args, **kwargs)
        else:
            return redirect('login.html')
    return inner

#计算器页面视图，返回计算历史
@auth
def compute_history(request):
    user = request.session.get('username')
    print(user)
    his = History.objects.filter(username_id=user).values('history')
    return render(request, 'compute-history.html',{'history': his})

#ajax返回计算结果，并写入数据库
@auth
def result_history(request):
    input_str = request.GET.get('input_str')
    user= request.session.get('username')
    try:
        res = eval(input_str)
        print(user)
        #拼接算式与结果字符串
        his=f'{input_str}={res}'
        #写入数据库
        History.objects.create(username_id=user, history=his)
        return JsonResponse({"result": res})
    except Exception:
        return JsonResponse({"result": "error"})
