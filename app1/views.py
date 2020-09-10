from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render,redirect
import  requests
import  json
from .forms import PricingForm
from app1.models import PricingTable,PrincingTablesSerializer

from rest_framework.viewsets import ModelViewSet


class  PrincingTableViewsets(ModelViewSet):
    queryset = PricingTable.objects.all()
    serializer_class = PrincingTablesSerializer


# def display(request):
#        c1=requests.get("http://127.0.0.1:8000/showapi/")
#        ps=c1.json()
#        p=Paginator(ps,4)
#        p_no=request.GET.get("page_no",1)
#        page_obj=p.page(p_no)
#        print(page_obj)
#        return  render(request,"index.html",{"PrincingTables":page_obj})

def showdata(request):
    c1 = requests.get("http://127.0.0.1:8000/api/")
    ps = c1.json()
    p=Paginator(ps,4)
    p_no=request.GET.get('page_no',1)
    page_obj=p.page(p_no)
    print(page_obj)
    return render(request, "showdata.html", {"PricingTables": page_obj})
    # return render(request, "showdata.html",{"data":PricingTable.objects.all()})



def savedata(request):
    n1=request.POST['pricingid']
    print(n1)
    n2=request.POST["p1"]
    n3=request.POST["p2"]
    n4=request.POST["p3"]
    n5=request.POST["p4"]
    n6=request.POST["p5"]
    n7=request.POST["p6"]
    res = PricingTable(ID=n1, Plan_Name=n2, Plan_Formula=n3, Location=n4, Plan_Status=n5, Created_Date=n6,
                       Updated_Date=n7).save()
    messages.success(request, "Details are Saved")
    return redirect('showdata')




    #
    # # ef = PricingForm(request.POST)
    # # if ef.is_valid():
    # #     print("one")
    #  res=PricingTable(ID=n1,Plan_Name=n2,Plan_Formula=n3,Location=n4,Plan_Status=n5,Created_Date=n6,Updated_Date=n7).save()
    #  messages.success(request,"Details are Saved")
    #   return redirect('showdata')
    # # else:
    # #     print("not valif form")
    # #     return render(request,"index.html",{"ef":PricingForm()})
    #



def update_details(request):
    p0=request.POST['id']
    p1=request.POST['plan_name']
    print(p1)
    p2=request.POST['plan_formula']
    l1=request.POST['location']
    p3=request.POST['plan_status']
    res1=PricingTable.objects.filter(ID=p0)
    res1.update(Plan_Name=p1,Plan_Formula=p2,Location=l1,Plan_Status=p3)
    return redirect('showdata')


def delete(request):
    del_no=request.POST['delete']
    print(del_no)
    PricingTable.objects.filter(ID=del_no).delete()
    return redirect('showdata')


def individualdata(request):
    d=request.POST['d1']
    print(d)
    try:
        qs=PricingTable.objects.get(ID=d)
        return render(request,"search.html",{"qs1":qs,"ef":PricingForm()})
    except  PricingTable.DoesNotExist:
        return  render(request,"search.html",{"error_message":"Please Enter Valid Id No"})

