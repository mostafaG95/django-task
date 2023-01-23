from django.shortcuts import render


def renderHtml(request):
    user_dict={'users':[{'name':'mostafa','age':30,'salary':1111},{'name':'osama','age':20,'salary':2222}]}
    return render(request,'app2/index.html',user_dict)
