from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


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

#带History的计算器
def compute_history(request):
    return render(request, 'compute-ajax.html')

#返回计算结果与最近的三次计算历史
def result_history(request):
    input_str = request.GET.get('input_str')
    if request.session.get('user',None):
        result(request)
    else:
        request.session['user']
        result(request)
