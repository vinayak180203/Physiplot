from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def doppler(request):
    if request.method == "POST":
        t1 = request.POST.get("t1")
        t2 = request.POST.get("t2")
        t3 = request.POST.get("t3")
        t4 = request.POST.get("t4")
        t5 = request.POST.get("t5")
        t6 = request.POST.get("t6")
        t7 = request.POST.get("t7")
        t8 = request.POST.get("t8")
        t9 = request.POST.get("t9")
        t10 = request.POST.get("t10")
        t11 = request.POST.get("t11")
        t12 = request.POST.get("t12")
        t13 = request.POST.get("t13")
        t14 = request.POST.get("t14")
        t15 = request.POST.get("t15")
        f1 = request.POST.get("f1")
        f2 = request.POST.get("f2")
        f3 = request.POST.get("f3")
        f4 = request.POST.get("f4")
        f5 = request.POST.get("f5")
        f6 = request.POST.get("f6")
        f7 = request.POST.get("f7")
        f8 = request.POST.get("f8")
        f9 = request.POST.get("f9")
        f10 = request.POST.get("f10")
        f11 = request.POST.get("f11")
        f12 = request.POST.get("f12")
        f13 = request.POST.get("f13")
        f14 = request.POST.get("f14")
        f15 = request.POST.get("f15")
        return render(request, 'Dopplerresult.html', {'t1': t1, 't2': t2, 't3': t3, 't4': t4, 't5': t5, 
                                                     't6': t6, 't7': t7, 't8': t8, 't9': t9, 't10': t10,
                                                     't11': t11, 't12': t12, 't13': t13, 't14': t14, 't15': t15})
    else:
        template = loader.get_template('Dopplerinput.html')
        return HttpResponse(template.render())
    