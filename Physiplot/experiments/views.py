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
        return render(request, 'Doppler_result.html', {'t1': t1, 't2': t2, 't3': t3, 't4': t4, 't5': t5, 
                                                     't6': t6, 't7': t7, 't8': t8, 't9': t9, 't10': t10,
                                                     't11': t11, 't12': t12, 't13': t13, 't14': t14, 't15': t15})
    else:
        template = loader.get_template('Doppler_input.html')
        return HttpResponse(template.render())
    
def infrared(request):
    template = loader.get_template('Michael_Infrared_index.html')
    return HttpResponse(template.render())

def calibrationconstant(request):
    if request.method == "POST":
        n1 = request.POST.get("n1")
        n2 = request.POST.get("n2")
        n3 = request.POST.get("n3")
        n4 = request.POST.get("n4")
        n5 = request.POST.get("n5")
        n6 = request.POST.get("n6")
        n7 = request.POST.get("n7")
        n8 = request.POST.get("n8")
        n9 = request.POST.get("n9")
        n10 = request.POST.get("n10")
        n11 = request.POST.get("n11")
        n12 = request.POST.get("n12")
        n13 = request.POST.get("n13")
        n14 = request.POST.get("n14")
        n15 = request.POST.get("n15")
        m1i = request.POST.get("m1i")
        m2i = request.POST.get("m2i")
        m3i = request.POST.get("m3i")
        m4i = request.POST.get("m4i")
        m5i = request.POST.get("m5i")
        m6i = request.POST.get("m6i")
        m7i = request.POST.get("m7i")
        m8i = request.POST.get("m8i")
        m9i = request.POST.get("m9i")
        m10i = request.POST.get("m10i")
        m11i = request.POST.get("m11i")
        m12i = request.POST.get("m12i")
        m13i = request.POST.get("m13i")
        m14i = request.POST.get("m14i")
        m15i = request.POST.get("m15i")
        m1f = request.POST.get("m1f")
        m2f = request.POST.get("m2f")
        m3f = request.POST.get("m3f")
        m4f = request.POST.get("m4f")
        m5f = request.POST.get("m5f")
        m6f = request.POST.get("m6f")
        m7f = request.POST.get("m7f")
        m8f = request.POST.get("m8f")
        m9f = request.POST.get("m9f")
        m10f = request.POST.get("m10f")
        m11f = request.POST.get("m11f")
        m12f = request.POST.get("m12f")
        m13f = request.POST.get("m13f")
        m14f = request.POST.get("m14f")
        m15f = request.POST.get("m15f")
        d1 = request.POST.get("d1")
        d2 = request.POST.get("d2")
        d3 = request.POST.get("d3")
        d4 = request.POST.get("d4")
        d5 = request.POST.get("d5")
        d6 = request.POST.get("d6")
        d7 = request.POST.get("d7")
        d8 = request.POST.get("d8")
        d9 = request.POST.get("d9")
        d10 = request.POST.get("d10")
        d11 = request.POST.get("d11")
        d12 = request.POST.get("d12")
        d13 = request.POST.get("d13")
        d14 = request.POST.get("d14")
        d15 = request.POST.get("d15")
        return render(request, 'calibration_constant_result.html', {'n1': n1, 'n2': n2, 'n3': n3, 'n4': n4, 'n5': n5, 
                                                     'n6': n6, 'n7': n7, 'n8': n8, 'n9': n9, 'n10': n10,
                                                     'n11': n11, 'n12': n12, 'n13': n13, 'n14': n14, 'n15': n15, 
                                                     'd1': d1, 'd2': d2, 'd3': d3, 'd4': d4, 'd5': d5, 
                                                     'd6': d6, 'd7': d7, 'd8': d8, 'd9': d9, 'd10': d10,
                                                     'd11': d11, 'd12': d12, 'd13': d13, 'd14': d14, 'd15': d15, 
                                                     'm1i': m1i, 'm2i': m2i, 'm3i': m3i, 'm4i': m4i, 'm5i': m5i, 
                                                     'm6i': m6i, 'm7i': m7i, 'm8i': m8i, 'm9i': m9i, 'm10i': m10i,
                                                     'm11i': m11i, 'm12i': m12i, 'm13i': m13i, 'm14i': m14i, 'm15i': m15i,
                                                     'm1f': m1f, 'm2f': m2f, 'm3f': m3f, 'm4f': m4f, 'm5f': m5f, 
                                                     'm6f': m6f, 'm7f': m7f, 'm8f': m8f, 'm9f': m9f, 'm10f': m10f,
                                                     'm11f': m11f, 'm12f': m12f, 'm13f': m13f, 'm14f': m14f, 'm15f': m15f})
    else:
        template = loader.get_template('calibration_constant_input.html')
        return HttpResponse(template.render())  

def refractiveindex(request):
    if request.method == "POST":
        n1 = request.POST.get("n1")
        n2 = request.POST.get("n2")
        n3 = request.POST.get("n3")
        n4 = request.POST.get("n4")
        n5 = request.POST.get("n5")
        n6 = request.POST.get("n6")
        n7 = request.POST.get("n7")
        n8 = request.POST.get("n8")
        n9 = request.POST.get("n9")
        n10 = request.POST.get("n10")
        n11 = request.POST.get("n11")
        n12 = request.POST.get("n12")
        n13 = request.POST.get("n13")
        n14 = request.POST.get("n14")
        n15 = request.POST.get("n15")
        l1 = request.POST.get("l1")
        l2 = request.POST.get("l2")
        l3 = request.POST.get("l3")
        l4 = request.POST.get("l4")
        l5 = request.POST.get("l5")
        l6 = request.POST.get("l6")
        l7 = request.POST.get("l7")
        l8 = request.POST.get("l8")
        l9 = request.POST.get("l9")
        l10 = request.POST.get("l10")
        l11 = request.POST.get("l11")
        l12 = request.POST.get("l12")
        l13 = request.POST.get("l13")
        l14 = request.POST.get("l14")
        l15 = request.POST.get("l15")        
        r1 = request.POST.get("r1")
        r2 = request.POST.get("r2")
        r3 = request.POST.get("r3")
        r4 = request.POST.get("r4")
        r5 = request.POST.get("r5")
        r6 = request.POST.get("r6")
        r7 = request.POST.get("r7")
        r8 = request.POST.get("r8")
        r9 = request.POST.get("r9")
        r10 = request.POST.get("r10")
        r11 = request.POST.get("r11")
        r12 = request.POST.get("r12")
        r13 = request.POST.get("r13")
        r14 = request.POST.get("r14")
        r15 = request.POST.get("r15")
        m1 = request.POST.get("m1")
        m2 = request.POST.get("m2")
        m3 = request.POST.get("m3")
        m4 = request.POST.get("m4")
        m5 = request.POST.get("m5")
        m6 = request.POST.get("m6")
        m7 = request.POST.get("m7")
        m8 = request.POST.get("m8")
        m9 = request.POST.get("m9")
        m10 = request.POST.get("m10")
        m11 = request.POST.get("m11")
        m12 = request.POST.get("m12")
        m13 = request.POST.get("m13")
        m14 = request.POST.get("m14")
        m15 = request.POST.get("m15")
        return render(request, 'refractive_index_result.html', {'n1': n1, 'n2': n2, 'n3': n3, 'n4': n4, 'n5': n5, 
                                                     'n6': n6, 'n7': n7, 'n8': n8, 'n9': n9, 'n10': n10,
                                                     'n11': n11, 'n12': n12, 'n13': n13, 'n14': n14, 'n15': n15, 
                                                     'm1': m1, 'm2': m2, 'm3': m3, 'm4': m4, 'm5': m5, 
                                                     'm6': m6, 'm7': m7, 'm8': m8, 'm9': m9, 'm10': m10,
                                                     'm11': m11, 'm12': m12, 'm13': m13, 'm14': m14, 'm15': m15, 
                                                     'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4, 'l5': l5, 
                                                     'l6': l6, 'l7': l7, 'l8': l8, 'l9': l9, 'l10': l10,
                                                     'l11': l11, 'l12': l12, 'l13': l13, 'l14': l14, 'l15': l15, 
                                                     'r1': r1, 'r2': r2, 'r3': r3, 'r4': r4, 'r5': r5, 
                                                     'r6': r6, 'r7': r7, 'r8': r8, 'r9': r9, 'r10': r10,
                                                     'r11': r11, 'r12': r12, 'r13': r13, 'r14': r14, 'r15': r15})
    else:
        template = loader.get_template('refractive_index_input.html')
        return HttpResponse(template.render())

def wavelength(request):
    if request.method == "POST":
        n1 = request.POST.get("n1")
        n2 = request.POST.get("n2")
        n3 = request.POST.get("n3")
        n4 = request.POST.get("n4")
        n5 = request.POST.get("n5")
        n6 = request.POST.get("n6")
        n7 = request.POST.get("n7")
        n8 = request.POST.get("n8")
        n9 = request.POST.get("n9")
        n10 = request.POST.get("n10")
        n11 = request.POST.get("n11")
        n12 = request.POST.get("n12")
        n13 = request.POST.get("n13")
        n14 = request.POST.get("n14")
        n15 = request.POST.get("n15")
        m1i = request.POST.get("m1i")
        m2i = request.POST.get("m2i")
        m3i = request.POST.get("m3i")
        m4i = request.POST.get("m4i")
        m5i = request.POST.get("m5i")
        m6i = request.POST.get("m6i")
        m7i = request.POST.get("m7i")
        m8i = request.POST.get("m8i")
        m9i = request.POST.get("m9i")
        m10i = request.POST.get("m10i")
        m11i = request.POST.get("m11i")
        m12i = request.POST.get("m12i")
        m13i = request.POST.get("m13i")
        m14i = request.POST.get("m14i")
        m15i = request.POST.get("m15i")
        m1f = request.POST.get("m1f")
        m2f = request.POST.get("m2f")
        m3f = request.POST.get("m3f")
        m4f = request.POST.get("m4f")
        m5f = request.POST.get("m5f")
        m6f = request.POST.get("m6f")
        m7f = request.POST.get("m7f")
        m8f = request.POST.get("m8f")
        m9f = request.POST.get("m9f")
        m10f = request.POST.get("m10f")
        m11f = request.POST.get("m11f")
        m12f = request.POST.get("m12f")
        m13f = request.POST.get("m13f")
        m14f = request.POST.get("m14f")
        m15f = request.POST.get("m15f")
        d1 = request.POST.get("d1")
        d2 = request.POST.get("d2")
        d3 = request.POST.get("d3")
        d4 = request.POST.get("d4")
        d5 = request.POST.get("d5")
        d6 = request.POST.get("d6")
        d7 = request.POST.get("d7")
        d8 = request.POST.get("d8")
        d9 = request.POST.get("d9")
        d10 = request.POST.get("d10")
        d11 = request.POST.get("d11")
        d12 = request.POST.get("d12")
        d13 = request.POST.get("d13")
        d14 = request.POST.get("d14")
        d15 = request.POST.get("d15")
        return render(request, 'wavelength_result.html', {'n1': n1, 'n2': n2, 'n3': n3, 'n4': n4, 'n5': n5, 
                                                     'n6': n6, 'n7': n7, 'n8': n8, 'n9': n9, 'n10': n10,
                                                     'n11': n11, 'n12': n12, 'n13': n13, 'n14': n14, 'n15': n15, 
                                                     'd1': d1, 'd2': d2, 'd3': d3, 'd4': d4, 'd5': d5, 
                                                     'd6': d6, 'd7': d7, 'd8': d8, 'd9': d9, 'd10': d10,
                                                     'd11': d11, 'd12': d12, 'd13': d13, 'd14': d14, 'd15': d15, 
                                                     'm1i': m1i, 'm2i': m2i, 'm3i': m3i, 'm4i': m4i, 'm5i': m5i, 
                                                     'm6i': m6i, 'm7i': m7i, 'm8i': m8i, 'm9i': m9i, 'm10i': m10i,
                                                     'm11i': m11i, 'm12i': m12i, 'm13i': m13i, 'm14i': m14i, 'm15i': m15i,
                                                     'm1f': m1f, 'm2f': m2f, 'm3f': m3f, 'm4f': m4f, 'm5f': m5f, 
                                                     'm6f': m6f, 'm7f': m7f, 'm8f': m8f, 'm9f': m9f, 'm10f': m10f,
                                                     'm11f': m11f, 'm12f': m12f, 'm13f': m13f, 'm14f': m14f, 'm15f': m15f})
    else:
        template = loader.get_template('wavelength_input.html')
        return HttpResponse(template.render()) 