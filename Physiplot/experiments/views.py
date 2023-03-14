from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

import math
import os
from django.conf import settings
import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from io import BytesIO
import image_processing
matplotlib.use('Agg')

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def doppler(request):
    if request.method == "POST":
        frequency_emitted = float(request.POST.get("frequency_emitted"))
        t1 = float(request.POST.get("t1"))
        t2 = float(request.POST.get("t2"))
        t3 = float(request.POST.get("t3"))
        t4 = float(request.POST.get("t4"))
        t5 = float(request.POST.get("t5"))
        t6 = float(request.POST.get("t6"))
        t7 = float(request.POST.get("t7"))
        t8 = float(request.POST.get("t8"))
        t9 = float(request.POST.get("t9"))
        t10 = float(request.POST.get("t10"))
        t11 = float(request.POST.get("t11"))
        t12 = float(request.POST.get("t12"))
        t13 = float(request.POST.get("t13"))
        t14 = float(request.POST.get("t14"))
        t15 = float(request.POST.get("t15"))
        f1 = float(request.POST.get("f1"))
        f2 = float(request.POST.get("f2"))
        f3 = float(request.POST.get("f3"))
        f4 = float(request.POST.get("f4"))
        f5 = float(request.POST.get("f5"))
        f6 = float(request.POST.get("f6"))
        f7 = float(request.POST.get("f7"))
        f8 = float(request.POST.get("f8"))
        f9 = float(request.POST.get("f9"))
        f10 = float(request.POST.get("f10"))
        f11 = float(request.POST.get("f11"))
        f12 = float(request.POST.get("f12"))
        f13 = float(request.POST.get("f13"))
        f14 = float(request.POST.get("f14"))
        f15 = float(request.POST.get("f15"))
        v1 = ((frequency_emitted/f1)-1)*frequency_emitted
        v2 = ((frequency_emitted/f2)-1)*frequency_emitted
        v3 = ((frequency_emitted/f3)-1)*frequency_emitted
        v4 = ((frequency_emitted/f4)-1)*frequency_emitted
        v5 = ((frequency_emitted/f5)-1)*frequency_emitted
        v6 = ((frequency_emitted/f6)-1)*frequency_emitted
        v7 = ((frequency_emitted/f7)-1)*frequency_emitted
        v8 = ((frequency_emitted/f8)-1)*frequency_emitted
        v9 = ((frequency_emitted/f9)-1)*frequency_emitted
        v10 = ((frequency_emitted/f10)-1)*frequency_emitted
        v11 = ((frequency_emitted/f11)-1)*frequency_emitted    
        v12 = ((frequency_emitted/f12)-1)*frequency_emitted
        v13 = ((frequency_emitted/f13)-1)*frequency_emitted
        v14 = ((frequency_emitted/f14)-1)*frequency_emitted
        v15 = ((frequency_emitted/f15)-1)*frequency_emitted
        y = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15]
        v = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15]
        x = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15]
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel('Time')
        ax.set_ylabel('Frequency')
        file_path = os.path.join(settings.MEDIA_ROOT, 'f-t.png')
        fig.savefig(file_path)
        v = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15]
        fig, ax = plt.subplots()
        ax.plot(x, v)
        ax.set_xlabel('Time')
        ax.set_ylabel('Velocity')    
        file_path = os.path.join(settings.MEDIA_ROOT, 'v-t.png')
        fig.savefig(file_path)
        return render(request, 'Doppler_result.html', {'t1': t1, 't2': t2, 't3': t3, 't4': t4, 't5': t5, 
                                                     't6': t6, 't7': t7, 't8': t8, 't9': t9, 't10': t10,
                                                     't11': t11, 't12': t12, 't13': t13, 't14': t14, 't15': t15,
                                                     'v1': v1, 'v2': v2, 'v3': v3, 'v4': v4, 'v5': v5, 
                                                     'v6': v6, 'v7': v7, 'v8': v8, 'v9': v9, 'v10': v10,
                                                     'v11': v11, 'v12': v12, 'v13': v13, 'v14': v14, 'v15': v15, 'ft': os.path.join(settings.MEDIA_URL, 'f-t.png'), 'vt': os.path.join(settings.MEDIA_URL, 'v-t.png')})
    else:
        template = loader.get_template('Doppler_input.html')
        return HttpResponse(template.render())
    
def infrared(request):
    template = loader.get_template('Michael_Infrared_index.html')
    return HttpResponse(template.render())

def calibrationconstant(request):
    if request.method == "POST":
        wavelength = float(request.POST.get("wavelength"))
        n1 = float(request.POST.get("n1"))
        n2 = float(request.POST.get("n2"))
        n3 = float(request.POST.get("n3"))
        n4 = float(request.POST.get("n4"))
        n5 = float(request.POST.get("n5"))
        n6 = float(request.POST.get("n6"))
        n7 = float(request.POST.get("n7"))
        n8 = float(request.POST.get("n8"))
        n9 = float(request.POST.get("n9"))
        n10 = float(request.POST.get("n10"))
        n11 = float(request.POST.get("n11"))
        n12 = float(request.POST.get("n12"))
        n13 = float(request.POST.get("n13"))
        n14 = float(request.POST.get("n14"))
        n15 = float(request.POST.get("n15"))
        m1i = float(request.POST.get("m1i"))
        m2i = float(request.POST.get("m2i"))
        m3i = float(request.POST.get("m3i"))
        m4i = float(request.POST.get("m4i"))
        m5i = float(request.POST.get("m5i"))
        m6i = float(request.POST.get("m6i"))
        m7i = float(request.POST.get("m7i"))
        m8i = float(request.POST.get("m8i"))
        m9i = float(request.POST.get("m9i"))
        m10i = float(request.POST.get("m10i"))
        m11i = float(request.POST.get("m11i"))
        m12i = float(request.POST.get("m12i"))
        m13i = float(request.POST.get("m13i"))
        m14i = float(request.POST.get("m14i"))
        m15i = float(request.POST.get("m15i"))
        m1f = float(request.POST.get("m1f"))
        m2f = float(request.POST.get("m2f"))
        m3f = float(request.POST.get("m3f"))
        m4f = float(request.POST.get("m4f"))
        m5f = float(request.POST.get("m5f"))
        m6f = float(request.POST.get("m6f"))
        m7f = float(request.POST.get("m7f"))
        m8f = float(request.POST.get("m8f"))
        m9f = float(request.POST.get("m9f"))
        m10f = float(request.POST.get("m10f"))
        m11f = float(request.POST.get("m11f"))
        m12f = float(request.POST.get("m12f"))
        m13f = float(request.POST.get("m13f"))
        m14f = float(request.POST.get("m14f"))
        m15f = float(request.POST.get("m15f"))
        d1 = m1f - m1i
        d2 = m2f - m2i
        d3 = m3f - m3i
        d4 = m4f - m4i
        d5 = m5f - m5i
        d6 = m6f - m6i
        d7 = m7f - m7i
        d8 = m8f - m8i
        d9 = m9f - m9i
        d10 = m10f - m10i
        d11 = m11f - m11i
        d12 = m12f - m12i
        d13 = m13f - m13i
        d14 = m14f - m14i
        d15 = m15f - m15i
        cc1 = (wavelength*n1)/(2*d1)
        cc2 = (wavelength*n2)/(2*d2)
        cc3 = (wavelength*n3)/(2*d3)
        cc4 = (wavelength*n4)/(2*d4)
        cc5 = (wavelength*n5)/(2*d5)
        cc6 = (wavelength*n6)/(2*d6)
        cc7 = (wavelength*n7)/(2*d7)
        cc8 = (wavelength*n8)/(2*d8)
        cc9 = (wavelength*n9)/(2*d9)
        cc10 = (wavelength*n10)/(2*d10)
        cc11 = (wavelength*n11)/(2*d11)
        cc12 = (wavelength*n12)/(2*d12)
        cc13 = (wavelength*n13)/(2*d13)
        cc14 = (wavelength*n14)/(2*d14)
        cc15 = (wavelength*n15)/(2*d15)
        ccavg = (cc1 + cc2 + cc3 + cc4 + cc5 + cc6 + cc7 + cc8 + cc9 + cc10 + cc11 + cc12 + cc13 + cc14 + cc15)/15
        return render(request, 'calibration_constant_result.html', {'wavelength': wavelength, 'n1': n1, 'n2': n2, 'n3': n3, 'n4': n4, 'n5': n5, 
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
                                                     'm11f': m11f, 'm12f': m12f, 'm13f': m13f, 'm14f': m14f, 'm15f': m15f,
                                                     'cc1': cc1, 'cc2': cc2, 'cc3': cc3, 'cc4': cc4, 'cc5': cc5, 
                                                     'cc6': cc6, 'cc7': cc7, 'cc8': cc8, 'cc9': cc9, 'cc10': cc10,
                                                     'cc11': cc11, 'cc12': cc12, 'cc13': cc13, 'cc14': cc14, 'cc15': cc15, 'ccavg': ccavg})
    else:
        template = loader.get_template('calibration_constant_input.html')
        return HttpResponse(template.render())  

def refractiveindex(request):
    if request.method == "POST":
        thickness = float(request.POST.get("thickness"))
        wavelength = float(request.POST.get("wavelength"))
        n1 = float(request.POST.get("n1"))
        n2 = float(request.POST.get("n2"))
        n3 = float(request.POST.get("n3"))
        n4 = float(request.POST.get("n4"))
        n5 = float(request.POST.get("n5"))
        n6 = float(request.POST.get("n6"))
        n7 = float(request.POST.get("n7"))
        n8 = float(request.POST.get("n8"))
        n9 = float(request.POST.get("n9"))
        n10 = float(request.POST.get("n10"))
        n11 = float(request.POST.get("n11"))
        n12 = float(request.POST.get("n12"))
        n13 = float(request.POST.get("n13"))
        n14 = float(request.POST.get("n14"))
        n15 = float(request.POST.get("n15"))
        l1 = float(request.POST.get("l1"))
        l2 = float(request.POST.get("l2"))
        l3 = float(request.POST.get("l3"))
        l4 = float(request.POST.get("l4"))
        l5 = float(request.POST.get("l5"))
        l6 = float(request.POST.get("l6"))
        l7 = float(request.POST.get("l7"))
        l8 = float(request.POST.get("l8"))
        l9 = float(request.POST.get("l9"))
        l10 = float(request.POST.get("l10"))
        l11 = float(request.POST.get("l11"))
        l12 = float(request.POST.get("l12"))
        l13 = float(request.POST.get("l13"))
        l14 = float(request.POST.get("l14"))
        l15 = float(request.POST.get("l15"))        
        r1 = float(request.POST.get("r1"))
        r2 = float(request.POST.get("r2"))
        r3 = float(request.POST.get("r3"))
        r4 = float(request.POST.get("r4"))
        r5 = float(request.POST.get("r5"))
        r6 = float(request.POST.get("r6"))
        r7 = float(request.POST.get("r7"))
        r8 = float(request.POST.get("r8"))
        r9 = float(request.POST.get("r9"))
        r10 = float(request.POST.get("r10"))
        r11 = float(request.POST.get("r11"))
        r12 = float(request.POST.get("r12"))
        r13 = float(request.POST.get("r13"))
        r14 = float(request.POST.get("r14"))
        r15 = float(request.POST.get("r15"))
        m1 = (l1 + r1)/2
        m2 = (l2 + r2)/2
        m3 = (l3 + r3)/2
        m4 = (l4 + r4)/2
        m5 = (l5 + r5)/2
        m6 = (l6 + r6)/2
        m7 = (l7 + r7)/2
        m8 = (l8 + r8)/2
        m9 = (l9 + r9)/2
        m10 = (l10 + r10)/2
        m11 = (l11 + r11)/2
        m12 = (l12 + r12)/2
        m13 = (l13 + r13)/2
        m14 = (l14 + r14)/2
        m15 = (l15 + r15)/2
        rf1 = (((2*thickness)-(n1*wavelength))*(1-math.cos(m1)))/((2*thickness*(1-math.cos(m1)))-(n1*wavelength))
        rf2 = (((2*thickness)-(n2*wavelength))*(1-math.cos(m2)))/((2*thickness*(1-math.cos(m2)))-(n2*wavelength))
        rf3 = (((2*thickness)-(n3*wavelength))*(1-math.cos(m3)))/((2*thickness*(1-math.cos(m3)))-(n3*wavelength))
        rf4 = (((2*thickness)-(n4*wavelength))*(1-math.cos(m4)))/((2*thickness*(1-math.cos(m4)))-(n4*wavelength))
        rf5 = (((2*thickness)-(n5*wavelength))*(1-math.cos(m5)))/((2*thickness*(1-math.cos(m5)))-(n5*wavelength))
        rf6 = (((2*thickness)-(n6*wavelength))*(1-math.cos(m6)))/((2*thickness*(1-math.cos(m6)))-(n6*wavelength))
        rf7 = (((2*thickness)-(n7*wavelength))*(1-math.cos(m7)))/((2*thickness*(1-math.cos(m7)))-(n7*wavelength))
        rf8 = (((2*thickness)-(n8*wavelength))*(1-math.cos(m8)))/((2*thickness*(1-math.cos(m8)))-(n8*wavelength))
        rf9 = (((2*thickness)-(n9*wavelength))*(1-math.cos(m9)))/((2*thickness*(1-math.cos(m9)))-(n9*wavelength))
        rf10 = (((2*thickness)-(n10*wavelength))*(1-math.cos(m10)))/((2*thickness*(1-math.cos(m10)))-(n10*wavelength))
        rf11 = (((2*thickness)-(n11*wavelength))*(1-math.cos(m11)))/((2*thickness*(1-math.cos(m11)))-(n11*wavelength))
        rf12 = (((2*thickness)-(n12*wavelength))*(1-math.cos(m12)))/((2*thickness*(1-math.cos(m12)))-(n12*wavelength))
        rf13 = (((2*thickness)-(n13*wavelength))*(1-math.cos(m13)))/((2*thickness*(1-math.cos(m13)))-(n13*wavelength))
        rf14 = (((2*thickness)-(n14*wavelength))*(1-math.cos(m14)))/((2*thickness*(1-math.cos(m14)))-(n14*wavelength))
        rf15 = (((2*thickness)-(n15*wavelength))*(1-math.cos(m15)))/((2*thickness*(1-math.cos(m15)))-(n15*wavelength))
        rfavg = (rf1 + rf2 + rf3 + rf4 + rf5 + rf6 + rf7 + rf8 + rf9 + rf10 + rf11 + rf12 + rf13 + rf14 + rf15)/15
        return render(request, 'refractive_index_result.html', {'thickness': thickness, 'wavelength': wavelength, 'n1': n1, 'n2': n2, 'n3': n3, 'n4': n4, 'n5': n5, 
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
                                                     'r11': r11, 'r12': r12, 'r13': r13, 'r14': r14, 'r15': r15,
                                                     'rf1': rf1, 'rf2': rf2, 'rf3': rf3, 'rf4': rf4, 'rf5': rf5, 
                                                     'rf6': rf6, 'rf7': rf7, 'rf8': rf8, 'rf9': rf9, 'rf10': rf10,
                                                     'rf11': rf11, 'rf12': rf12, 'rf13': rf13, 'rf14': rf14, 'rf15': rf15, 'rfavg': rfavg})
    else:
        template = loader.get_template('refractive_index_input.html')
        return HttpResponse(template.render())

def wavelength(request):
    if request.method == "POST":
        calibration_constant = float(request.POST.get("calibration_constant"))
        n1 = float(request.POST.get("n1"))
        n2 = float(request.POST.get("n2"))
        n3 = float(request.POST.get("n3"))
        n4 = float(request.POST.get("n4"))
        n5 = float(request.POST.get("n5"))
        n6 = float(request.POST.get("n6"))
        n7 = float(request.POST.get("n7"))
        n8 = float(request.POST.get("n8"))
        n9 = float(request.POST.get("n9"))
        n10 = float(request.POST.get("n10"))
        n11 = float(request.POST.get("n11"))
        n12 = float(request.POST.get("n12"))
        n13 = float(request.POST.get("n13"))
        n14 = float(request.POST.get("n14"))
        n15 = float(request.POST.get("n15"))
        m1i = float(request.POST.get("m1i"))
        m2i = float(request.POST.get("m2i"))
        m3i = float(request.POST.get("m3i"))
        m4i = float(request.POST.get("m4i"))
        m5i = float(request.POST.get("m5i"))
        m6i = float(request.POST.get("m6i"))
        m7i = float(request.POST.get("m7i"))
        m8i = float(request.POST.get("m8i"))
        m9i = float(request.POST.get("m9i"))
        m10i = float(request.POST.get("m10i"))
        m11i = float(request.POST.get("m11i"))
        m12i = float(request.POST.get("m12i"))
        m13i = float(request.POST.get("m13i"))
        m14i = float(request.POST.get("m14i"))
        m15i = float(request.POST.get("m15i"))
        m1f = float(request.POST.get("m1f"))
        m2f = float(request.POST.get("m2f"))
        m3f = float(request.POST.get("m3f"))
        m4f = float(request.POST.get("m4f"))
        m5f = float(request.POST.get("m5f"))
        m6f = float(request.POST.get("m6f"))
        m7f = float(request.POST.get("m7f"))
        m8f = float(request.POST.get("m8f"))
        m9f = float(request.POST.get("m9f"))
        m10f = float(request.POST.get("m10f"))
        m11f = float(request.POST.get("m11f"))
        m12f = float(request.POST.get("m12f"))
        m13f = float(request.POST.get("m13f"))
        m14f = float(request.POST.get("m14f"))
        m15f = float(request.POST.get("m15f"))
        d1 = m1f - m1i
        d2 = m2f - m2i
        d3 = m3f - m3i
        d4 = m4f - m4i
        d5 = m5f - m5i
        d6 = m6f - m6i
        d7 = m7f - m7i
        d8 = m8f - m8i
        d9 = m9f - m9i
        d10 = m10f - m10i
        d11 = m11f - m11i
        d12 = m12f - m12i
        d13 = m13f - m13i
        d14 = m14f - m14i
        d15 = m15f - m15i
        w1 = (2*d1*calibration_constant)/n1
        w2 = (2*d2*calibration_constant)/n2
        w3 = (2*d3*calibration_constant)/n3
        w4 = (2*d4*calibration_constant)/n4
        w5 = (2*d5*calibration_constant)/n5
        w6 = (2*d6*calibration_constant)/n6
        w7 = (2*d7*calibration_constant)/n7
        w8 = (2*d8*calibration_constant)/n8
        w9 = (2*d9*calibration_constant)/n9
        w10 = (2*d10*calibration_constant)/n10
        w11 = (2*d11*calibration_constant)/n11
        w12 = (2*d12*calibration_constant)/n12
        w13 = (2*d13*calibration_constant)/n13
        w14 = (2*d14*calibration_constant)/n14
        w15 = (2*d15*calibration_constant)/n15
        wavg = (w1 + w2 + w3 + w4 + w5 + w6 + w7 + w8 + w9 + w10 + w11 + w12 + w13 + w14 + w15)/15
        return render(request, 'wavelength_result.html', {'calibration_constant': calibration_constant, 'n1': n1, 'n2': n2, 'n3': n3, 'n4': n4, 'n5': n5, 
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
                                                     'm11f': m11f, 'm12f': m12f, 'm13f': m13f, 'm14f': m14f, 'm15f': m15f,
                                                     'w1': w1, 'w2': w2, 'w3': w3, 'w4': w4, 'w5': w5, 
                                                     'w6': w6, 'w7': w7, 'w8': w8, 'w9': w9, 'w10': w10,
                                                     'w11': w11, 'w12': w12, 'w13': w13, 'w14': w14, 'w15': w15, 'wavg': wavg})
    else:
        template = loader.get_template('wavelength_input.html')
        return HttpResponse(template.render()) 
    
def solar(request):
    # if request.method == "POST":
        # image = request.POST.get("image")
        # print(image)
    # if request.method == 'POST' and request.FILES.get('image'):
    #     # Read the uploaded image file into a BytesIO object
    #     image_bytes = BytesIO(request.FILES['image'].read())
    #     # Call the process_image() function in image_processing.py with the image data
    #     processed_image = image_processing.process_image(image_bytes)
    #     # Return the processed image to the user as an HTTP response
    #     # return HttpResponse(processed_image, content_type='image/jpeg')
    #     image = HttpResponse(processed_image, content_type='image/jpeg')
    #     return render(request, 'solar_output.html', {'image': image})
    # else:
    #     template = loader.get_template('solar.html')
    #     return HttpResponse(template.render())
    if request.method == 'POST':
        image = request.FILES['image']
        file_path = os.path.join(settings.MEDIA_ROOT, image.name)
        with open(file_path, 'wb') as f:
            for chunk in image.chunks():
                f.write(chunk)
        # default_storage.save(file_path, ContentFile(image.read()))
        relative_path = os.path.relpath(file_path, settings.BASE_DIR)
        # filename = default_storage.save(image.name, image)
        # image_url = default_storage.url(filename)
        img = cv2.imread(relative_path,0)
        s=img.shape[0]
        I=img[int(s/2)]
        m=max (I)
        O=[(i/m)for i in I]
        x=np.linspace(-1,1,len (O))
        fig, ax = plt.subplots()
        ax.plot(x, O)
        file_path = os.path.join(settings.MEDIA_ROOT, 'x-O.png')
        fig.savefig(file_path)
        img1 = cv2.imread(relative_path, flags = cv2.IMREAD_GRAYSCALE)
        s=img1.shape[0]
        a=0
        b= max(img1[int(s/2)])
        print(b)
        l=list(img1[int(s/2)])
        for i in l :
            k= min(l)
            if k>=10 :
                a=k
            else:
                l.remove(k)
        alpha = a/b 
        beta = 1 - (alpha)
        P = [(i/m)**(0.25) for i in I]
        y = np.linspace(-1,1,len (P))
        q=[(w-alpha/beta) for w in P]
        fig, ax = plt.subplots()
        ax.plot(P, q)
        file_path = os.path.join(settings.MEDIA_ROOT, 'P-q.png')
        fig.savefig(file_path)
        fig, ax = plt.subplots()
        ax.plot(y, P)
        file_path = os.path.join(settings.MEDIA_ROOT, 'y-P.png')
        fig.savefig(file_path)
        return render(request, 'solar_output.html', {'xO': os.path.join(settings.MEDIA_URL, 'x-O.png'), 'a': a, 'b': b, 'alpha': alpha, 'beta': beta, 
                                                     'Pq': os.path.join(settings.MEDIA_URL, 'P-q.png'), 'yP': os.path.join(settings.MEDIA_URL, 'y-P.png')})
    return render(request, 'solar.html')