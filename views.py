from django.shortcuts import render
from django.http import HttpResponse
from my_app.azureai import client
from my_app.models import Comment
# Create your views here.
def fun1(request):
    # data="THIS IS BACKEND TEXT"
    # data1="THIS IS FIRST VARIABLE"
    # data2="THIS IS SECOND VARIABLE"
    # context={'response':data,
    #          'firstpart':data1,
    #          'secondpart':data2,}
    # context={'firstpart':'THIS IS FIRST VARIABLE','secondpart':'THIS IS SECOND VARIABLE'}
    # details={'mobilename':'OnePlus',
    #          'price':24000,
    #          'RAM':'8GB'}
    # response={'context':details}
    # return render(request,"index.html",response)
    #sample for sentiment analysis
    # comments=["ONEPLUUS HAS BEST BATTERY PERFORMANCE",
    #           "VIVO HAS BEST PHOTOGRPAHIC SENSORS",
    #           "Is This job good or not",
    #           "This property is illegal"]
    # result=client.analyze_sentiment(documents=comments)
    # return render(request,"index.html",{"SENTIMENT_ANALYSIS":result})  
    return render(request,"index.html")
def fun2(request):
    # di=[
    #     {
    #     'name':"ONEPLUS",
    #      'feedback':["IT IS WORTH THE PRICE",
    #                  "IT IS WORTH THE PRICE BUT THE SPECIFICATIONS IS AVERAGE",
    #                  "IT IS NOT WORTH THE PRICE"],
    #         'sentiment':None
    #      },
    #     {
    #     'name':"VIVO",
    #      'feedback':["IT IS WORTH THE PRICE",
    #                  "IT IS WORTH THE PRICE BUT THE SPECIFICATIONS IS AVERAGE",
    #                  "IT IS NOT WORTH THE PRICE"],
    #      'sentiment':None
    #      }
    # ]
    text=request.POST.get("comment")
    if text:
        obj=Comment(msg=text,review="Pending")
        obj.save()
    return render(request,"index1.html")
    # return render(request,"index1.html")
def fun3(request):
    if request.method=="POST":
        a=request.POST.get("comment")
        print(a)
        result=client.analyze_sentiment(documents=[a])
        t=result[0].sentiment
        return render(request,"index2.html",{"res":a,
                                             "resu":result,
                                             "resul":t}) 
    else:
        return render(request,"index2.html")
    # return render(request,"index2.html")
    
def analyze_review(request):
    comment=Comment.objects.filter(review="Pending")
    if comment:
        for x in comment:
            t=x.msg
            res=client.analyze_sentiment(documents=[t])
            re=res[0].sentiment
            x.review=re
            x.save()
    return render(request,"index1.html")
            
 