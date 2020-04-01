from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def computev1(request):
    return render(request,'compute.html')

def compute_ajax(request):
    if request.method == 'POST':
        return JsonResponse({'res':1})
    return render(request,'compute-ajax.html')
@csrf_exempt
def result(request):
    input_str=request.GET.get('input_str')
    # print(input_str)
    if input_str=="":
        return JsonResponse({"result":"none"})
    try:
        res=eval(input_str)
        return JsonResponse({"result":res})
    except Exception:
        return JsonResponse({"result":"error"})