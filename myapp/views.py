from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from myapp.models import *


def AHome(request):
    return render(request,"Admin/Home.html")
def login(request):
    return render(request,"login.html")
def login_post(request):
    user=request.POST['username']
    pswd=request.POST['password']

    lg=LOGIN.objects.filter(Username=user,Password=pswd)
    if lg.exists():
        lg1=LOGIN.objects.get(Username=user,Password=pswd)
        request.session['lid']=lg1.id
        if lg1.Type == 'admin':
            return  HttpResponse("<script>alert('Welcome Admin');window.location='/myapp/AHome/'</script>")
        elif lg1.Type == 'user':
            return  HttpResponse("<script>alert('Welcome User');window.location='/myapp/UserHome/'</script>")
        elif lg1.Type == 'deliveryboy':
            return  HttpResponse("<script>alert('Welcome DBoy');window.location='/myapp/DBHome/'</script>")
        else:
            return HttpResponse("<script>alert('Invalid');window.location='/myapp/login/'</script>")
    else:
        return HttpResponse("<script>alert('Invalid');window.location='/myapp/login/'</script>")

def admin_changepwd(request):
    return render(request,"Admin/ChangePassword.html")
def admin_changepwd_post(request):
    old=request.POST['textfield']
    new=request.POST['textfield2']
    confirm=request.POST['textfield3']

    ch = LOGIN.objects.filter(Password=old,id=request.session['lid'])
    if ch.exists():
        if new==confirm:
            ch = LOGIN.objects.filter(Password=old, id=request.session['lid']).update(Password=confirm)
            return HttpResponse("<script>alert('Update Admin pwd Success');window.location='/myapp/login/'</script>")
        else:
            return HttpResponse("<script>alert('Invalid');window.location='/myapp/login/'</script>")


    else:
        return HttpResponse("<script>alert('Invalid');window.location='/myapp/login/'</script>")

def Addprofile(request):
    # obj=PROFILE.objects.all()
    return render(request,"Admin/1.AddProfile.html")

def Addprofile_post(request):
    Bname=request.POST['textfield']
    place=request.POST['textfield2']
    post=request.POST['textfield3']
    pin=request.POST['textfield4']
    Open_Time=request.POST['textfield5']
    Close_Time=request.POST['textfield8']
    mail=request.POST['textfield6']
    estDate=request.POST['textfield7']

    obj=PROFILE()
    obj.Bname=Bname
    obj.place=place
    obj.post=post
    obj.pin=pin
    obj.Open_Time=Open_Time
    obj.Close_Time=Close_Time
    obj.mail=mail
    obj.estDate=estDate
    obj.save()

    return HttpResponse("<script>alert(' ADMIN PROFILE ADDED!!');window.location='/myapp/AHome/'</script>")

def ViewProfile(request):
    obj=PROFILE.objects.get()
    return render(request,"Admin/2.ViewProfile.html",{"data":obj})

def Updateprofile(request,id):
    obj=PROFILE.objects.get(id=id)
    return render(request,"Admin/3.UpdateProfile.html",{"data":obj})

def Updateprofile_post(request):
    Bname = request.POST['textfield']
    place = request.POST['textfield2']
    post = request.POST['textfield3']
    pin = request.POST['textfield4']
    Open_Time = request.POST['textfield5']
    Close_Time = request.POST['textfield8']
    mail = request.POST['textfield6']
    estDate = request.POST['textfield7']
    id=request.POST['id']

    obj = PROFILE.objects.get(id=id)
    obj.Bname = Bname
    obj.place = place
    obj.post = post
    obj.pin = pin
    obj.Open_Time = Open_Time
    obj.Close_Time = Close_Time
    obj.mail = mail
    obj.estDate = estDate
    obj.save()

    return HttpResponse("<script>alert(' ADMIN PROFILE EDITED!!');window.location='/myapp/ViewProfile/'</script>")

def Addproduct(request):
    a=CATEGORY.objects.all()
    return render(request,"Admin/4.AddProduct.html",{'data':a})
def Addproduct_post(request):
    cat=request.POST['cat']
    pname=request.POST['textfield']
    image=request.FILES['fileField']
    mfd=request.POST['textfield3']
    exp=request.POST['textfield4']
    details=request.POST['textarea']
    rate=request.POST['textfield6']


    date=datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"

    fs=FileSystemStorage()
    fs.save(date,image)



    a=PRODUCT()
    a.CATEGORY=CATEGORY.objects.get(id=cat)
    a.Product_name=pname
    a.Image=fs.url(date)
    a.MFD=mfd
    a.EXP=exp
    a.Details=details
    a.Rate=rate
    a.save()

    return HttpResponse("<script>alert(' Success');window.location='/myapp/ViewProduct/'</script>")

def ViewProduct(request):
    a=PRODUCT.objects.all()
    return render(request,"Admin/5.ViewProduct.html",{"data":a})
def Viewproduct_post(request):
    search=request.POST['search']
    obj=PRODUCT.objects.filter(Product_name__icontains=search)
    return render(request,"Admin/5.ViewProduct.html",{"data":obj})

def Updateproduct(request):
    a=CATEGORY.objects.all()
    return render(request,"Admin/6.UpdateProduct.html",{'data':a})
def Updateproduct_post(request):
    cat=request.POST['cat']
    pname=request.POST['textfield']
    image=request.POST['fileField']
    mfd=request.POST['textfield3']
    exp=request.POST['textfield4']
    details=request.POST['textarea']
    rate=request.POST['textfield6']

    a=PRODUCT()
    a.CATEGORY=CATEGORY.objects.get()
    a.Product_name = pname
    a.Image = image
    a.MFD = mfd
    a.EXP = exp
    a.Details = details
    a.Rate = rate
    a.save()

    return HttpResponse("<script>alert(' Success');window.location='/myapp/ViewProduct/'</script>")

def Deleteproduct(request,id):
    d=PRODUCT.objects.get(id=id)
    d.delete()
    return HttpResponse("<script>alert(' Delete Success');window.location='/myapp/ViewProduct/'</script>")

def AddDboy(request):
    return render(request,"Admin/7.AddDeliveyBoy.html")
def AddDboy_post(request):
    dboyname=request.POST['textfield']
    phone=request.POST['textfield2']
    dob=request.POST['textfield3']
    place=request.POST['textfield4']
    post=request.POST['textfield5']
    pin=request.POST['textfield6']
    email=request.POST['textfield7']
    password=request.POST['textfield8']
    liscence=request.POST['textfield9']

    Dobj=LOGIN()
    Dobj.Username=email
    Dobj.Password=password
    Dobj.Type="deliveryboy"
    Dobj.save()

    Dobj1=DELIVERY_BOY()
    Dobj1.D_Name=dboyname
    Dobj1.DOB=dob
    Dobj1.Phone=phone
    Dobj1.Place=place
    Dobj1.Post=post
    Dobj1.Pin=pin
    Dobj1.Emails=email
    Dobj1.Liscence=liscence
    Dobj1.LOGIN=Dobj
    Dobj1.save()
    return HttpResponse("<script>alert(' Add DBoy Success');window.location='/myapp/AHome/'</script>")

def ViewDboy(request):
    vobj=DELIVERY_BOY.objects.all()
    return render(request,"Admin/8.ViewDBoy.html",{"data":vobj})
def ViewDboy_post(request):
    search=request.POST['search']
    vobj = DELIVERY_BOY.objects.filter(D_Name__icontains=search)
    return render(request, "Admin/8.ViewDBoy.html", {"data": vobj})
def DeleteDeliveryboy(request,id):
    d=DELIVERY_BOY.objects.get(id=id)
    d.delete()
    return HttpResponse("<script>alert(' Delete Success');window.location='/myapp/AddDBoy/'</script>")
def UpdateDboy(request,id):
    obj=DELIVERY_BOY.objects.get(id=id)
    return render(request,"Admin/9.UpdateDBoy.html",{"data":obj})
def UpdateDboy_post(request):
    dboyname = request.POST['textfield']
    phone = request.POST['textfield2']
    dob = request.POST['textfield3']
    place = request.POST['textfield4']
    post = request.POST['textfield5']
    pin = request.POST['textfield6']
    email = request.POST['textfield7']
    #password = request.POST['textfield8']
    liscence = request.POST['textfield9']
    id=request.POST['id']


    Dobj = LOGIN()
    Dobj.Username = email
   # Dobj.Password = password
    Dobj.Type = "deliveryboy"
    Dobj.save()

    Dobj1=DELIVERY_BOY.objects.get(id=id)
    #Dobj1 = DELIVERY_BOY()
    Dobj1.D_Name = dboyname
    Dobj1.DOB = dob
    Dobj1.Phone = phone
    Dobj1.Place = place
    Dobj1.Post = post
    Dobj1.Pin = pin
    Dobj1.Emails = email
    Dobj1.Liscence = liscence
    Dobj1.LOGIN = Dobj
    Dobj1.save()
    return HttpResponse("<script>alert(' Add DBoy Success');window.location='/myapp/AHome/'</script>")



def View_A_R_Assign_post(request):
    search=request.POST['textfield']
    obj=USER.objects.filter(User_name__icontains=search)
    return render(request,"Admin/10.5.ViewAccept-Reject-Assign.html",{"data":obj})

def AcceptUserOrder(request,id):
    ORDER_MAIN.objects.filter(id=id).update(Status="Approved")
    return HttpResponse("<script>alert('Order Accepted Successfully!!');window.location='/myapp/ViewAccRej/'</script>")
def RejectUserOrder(request,id):
    ORDER_MAIN.objects.filter(id=id).update(Status="Rejected")
    return HttpResponse("<script>alert('Order REJECTED!!');window.location='/myapp/ViewAccRej/'</script>")


def ViewMoreDetails(request,id):
    res=ORDER_SUB.objects.get(ORDERMAIN_id=id)
    return render(request,"Admin/AdminViewMoreDetails.html",{"data":res})


def ViewARassign(request):
    res=ORDER_MAIN.objects.all()
    assignments = ASSIGN.objects.values_list('ORDER_MAIN_id', flat=True)
    return render(request,"Admin/10.5.ViewAccept-Reject-Assign.html",{"data":res,'assignments':assignments})

def AssignDBoy(request, id):
    obj = DELIVERY_BOY.objects.all()
    product = ORDER_MAIN.objects.get(id=id)
    return render(request, "Admin/10.AssignDBoy.html", {"data": obj,'product':product})

def AssignDboy_post(request):
    p_id = request.POST['id']
    if request.method == 'POST':
        delivery_boy_id = request.POST['select']

        try:
            delivery = DELIVERY_BOY.objects.get(id=delivery_boy_id)
        except DELIVERY_BOY.DoesNotExist:
            return HttpResponse("<script>alert('Delivery Boy not found!');window.history.back();</script>")

        assignment = ASSIGN()
        assignment.Assign_date = datetime.now()
        assignment.Status = 'assigned'
        assignment.DELIVERY_BOY = delivery
        assignment.ORDER_MAIN = ORDER_MAIN.objects.get(id=p_id)  # Ensure you're getting the correct ORDER_MAIN
        assignment.save()
        return HttpResponse("<script>alert('Order ASSIGNED!!');window.location='/myapp/ViewAccRej/'</script>")
    return render(request,"Admin/10.5.ViewAccept-Reject-Assign.html")


def Viewasssignstatus(request):
    return render(request,"Admin/11.ViewAssignedStatus.html")

def Viewreject(request):
    return render(request,"Admin/13.ViewReject.html")

def Addcategory(request):
    return render(request,"Admin/AddCategory.html")
def Addcategory_post(request):
    category=request.POST['cat']
    cat1=CATEGORY()
    cat1.Category_name=category
    cat1.save()
    return HttpResponse("<script>alert(' Success');window.location='/myapp/AddCategory/'</script>")
def Editcategory(request,id):
    d=CATEGORY.objects.get(id=id)
    return render(request,"Admin/EditCategory.html",{'data':d})
def Editcategory_post(request):
    category=request.POST['cat']
    id=request.POST['id']
    cat1 = CATEGORY.objects.get(id=id)
    cat1.Category_name = category
    cat1.save()
    return HttpResponse("<script>alert(' Edit Success');window.location='/myapp/ViewCategory/'</script>")
def Viewcategory(request):
    a=CATEGORY.objects.all()
    return render(request,"Admin/ViewCategory.html",{'data':a})
def Deletecategory(request,id):
    d=CATEGORY.objects.get(id=id)
    d.delete()
    return HttpResponse("<script>alert(' Delete Success');window.location='/myapp/AddCategory/'</script>")



#DELIVERY BOY!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def DBHome(request):
    return render(request,"DeliveryBoy/DBHome.html")

def ViewDboyprofile(request):
    data=DELIVERY_BOY.objects.get(LOGIN__id=request.session['lid'])
    return render(request,"DeliveryBoy/1.ViewDBoyProfile.html",{"data":data})

def EditDboyprofile(request):
    return render(request,"DeliveryBoy/2.EditDBoyProfile.html")

def EditDboyprofile_post(request):
    dboyname = request.POST['textfield']
    phone = request.POST['textfield2']
    dob = request.POST['textfield3']
    place = request.POST['textfield4']
    post = request.POST['textfield5']
    pin = request.POST['textfield6']
    email = request.POST['textfield7']
    liscence = request.POST['textfield9']

    dobj=DELIVERY_BOY.objects.get(LOGIN_id=request.session['lid'])
    dobj.D_Name=dboyname
    dobj.Phone=phone
    dobj.DOB=dob
    dobj.Emails=email
    dobj.Place=place
    dobj.Post=post
    dobj.Pin=pin
    dobj.Liscence=liscence
    dobj.save()

    return HttpResponse("<script>alert('Success');window.location='/myapp/login/'</script>")

def Viewassign(request):
    obj=ASSIGN.objects.filter(DELIVERY_BOY__LOGIN__id=request.session['lid'])
    return render(request,"DeliveryBoy/3.ViewAssign.html",{"data":obj})
def UpdateOrderstatus(request):
    return render(request,"DeliveryBoy/4.UpdateOrderStatus.html")
def UpdateOrderstatus_post(request):
    Dboyid=request.POST['textfield']
    details=request.POST['textarea']
    OTP=request.POST['textfield2']
    Completed=request.POST['RadioGroup1']
    return HttpResponse('ok')
def DBoy_Changepwd(request):
    return render(request,"DeliveryBoy/ChangePassword.html")
def DBoy_Changepwd_post(request):
    old = request.POST['textfield']
    new = request.POST['textfield2']
    confirm = request.POST['textfield3']
    ch = LOGIN.objects.filter(Password=old, id=request.session['lid'])
    if ch.exists():
        if new == confirm:
            ch2 = LOGIN.objects.filter(Password=old, id=request.session['lid']).update(Password=confirm)
            return HttpResponse("<script>alert('Update DeliveryBoy pwd Success');window.location='/myapp/login/'</script>")
        else:
            return HttpResponse("<script>alert('Invalid');window.location='/myapp/login/'</script>")


    else:
        return HttpResponse("<script>alert('Invalid');window.location='/myapp/login/'</script>")


#USER

def UserHome(request):
    return render(request,"User/UserHome.html")

def Register(request):
    return render(request,"User/1.Register.html")

def Register_post(request):
    User_name=request.POST['textfield']
    Phone=request.POST['textfield2']
    Place=request.POST['textfield3']
    Post=request.POST['textfield4']
    Pin=request.POST['textfield5']
    Email=request.POST['textfield6']
    Password=request.POST['textfield7']
    Confirm_Password=request.POST['textfield8']

    print(User_name)

    ob=LOGIN()
    ob.Username=Email
    ob.Password=Password
    ob.Type='user'
    ob.save()

    if Password==Confirm_Password:
        ob1=USER()
        ob1.User_name=User_name
        ob1.Place=Place
        ob1.Post=Post
        ob1.Pin=Pin
        ob1.Phone=Phone
        ob1.Email=Email
        ob1.LOGIN=ob
        ob1.save()
        return HttpResponse("<script>alert('Success');window.location='/myapp/login/'</script>")
    else:
        return HttpResponse("<script>alert('Invalid');window.location='/myapp/Regiser/'</script>")


def Viewregister(request):
    data=USER.objects.get(LOGIN_id=request.session['lid'])
    return render(request,"User/2.ViewRegister.html",{"data":data})

def Updateregister(request,id):
    data=USER.objects.get(id=id)
    return render(request,"User/3.UpdateRegister.html",{'data':data})
def Updateregister_post(request):
    id=request.POST['id']
    User_name = request.POST['textfield']
    Phone = request.POST['textfield2']
    Place = request.POST['textfield3']
    Post = request.POST['textfield4']
    Pin = request.POST['textfield5']
    Email = request.POST['textfield6']


    ob1 = USER.objects.get(id=id)
    ob1.User_name = User_name
    ob1.Place = Place
    ob1.Post = Post
    ob1.Pin = Pin
    ob1.Phone = Phone
    ob1.Email = Email
    ob1.save()
    return HttpResponse("<script>alert('Update Success');window.location='/myapp/login/'</script>")


def User_Viewproduct(request):
    vobj=PRODUCT.objects.all()
    return render(request,"User/4.ViewProduct~.html",{"data":vobj})
def User_Viewproduct_post(request):
    search=request.POST['textfield']
    vobj=PRODUCT.objects.filter(Product_name__icontains=search)
    return render(request,"User/4.ViewProduct~.html",{"data":vobj})


# def Orderproduct(request):
#
#     return render(request,"User/5.OrderProduct.html")
# def Orderproduct_post(request):
#     Product_name=request.POST['textfield']
#     Quantity=request.POST['textfield3']
#     PIN=request.POST['textfield4']
#     return HttpResponse('OK')

def Vieworder(request):
    obj=ORDER_SUB.objects.filter(ORDERMAIN__USER__LOGIN_id=request.session['lid'])
    return render(request,"User/6.ViewOrder.html",{"data":obj})
def Vieworder_post(request):
    search = request.POST['textfield']
    obj = ORDER_SUB.objects.filter(ORDERMAIN__USER__LOGIN_id=request.session['lid'],PRODUCT__Product_name__icontains=search)
    return render(request, "User/6.ViewOrder.html", {"data": obj})


def ViewDeliverystatus(request):
    return render(request,"User/7.ViewDeliveryStatus~.html")

def User_Changepwd(request):
    return render(request,"User/ChangePassword.html")
def User_Changepwd_post(request):
    old = request.POST['textfield']
    new = request.POST['textfield2']
    confirm = request.POST['textfield3']

    ch = LOGIN.objects.filter(Password=old, id=request.session['lid'])
    if ch.exists():
        if new == confirm:
            ch1 = LOGIN.objects.filter(Password=old, id=request.session['lid']).update(Password=confirm)
            return HttpResponse("<script>alert('Update User pwd Success');window.location='/myapp/login/'</script>")
        else:
            return HttpResponse("<script>alert('Invalid');window.location='/myapp/login/'</script>")


    else:
        return HttpResponse("<script>alert('Invalid');window.location='/myapp/login/'</script>")


def User_Viewcategory(request):
    return render(request,"User/ViewCategory.html")

def User_Addtocart(request,id):
    return render(request,"User/addquantity.html",{"id":id})
def User_Addtocart_post(request):
    id=request.POST['id']
    qty=request.POST['cat']
    obj=CART()
    obj.PRODUCT_id=id
    obj.USER=USER.objects.get(LOGIN_id=request.session['lid'])
    obj.Quantity=qty
    obj.save()

    return HttpResponse("<script>alert('Product added to cart!!');window.location='/myapp/UserViewProduct/'</script>")

def User_ViewCart(request):
    data = CART.objects.filter(USER__LOGIN__id=request.session['lid'])
    total_amount = 0
    for item in data:
        total_amount += item.Quantity * item.PRODUCT.Rate
        request.session['pid']=item.PRODUCT.id
    return render(request,"User/ViewCart.html",{"data":data,"totalamount":total_amount})

def User_Buynow(request):
    # lid = request.session['lid']
    # res = CART.objects.filter(USER__LOGIN_id=lid)
    # for i in res:
    #     print(i)
    #     res2 = CART.objects.filter(USER__LOGIN_id=lid)
    #     boj = ORDER_MAIN()
    #     boj.USER = USER.objects.get(LOGIN_id=lid)
    #     # t=i.amount*i.qty
    #     boj.Amount = 0
    #     import datetime
    #     boj.Date = datetime.datetime.now().date().today()
    #     boj.Status = "pending"
    #     boj.save()
    #
    #     # res3 =
    #     mytotal = 0
    #     for j in res2:
    #         # print(j)
    #         bs = ORDER_SUB()
    #         bs.ORDERMAIN_id = boj.id
    #         bs.PRODUCT_id = j.PRODUCT.id
    #         bs.Quantity = j.Quantity
    #         bs.save()
    #
    #         mytotal += (float(j.PRODUCT.Rate) * j.Quantity)
    #         print(mytotal)
    #     CART.objects.filter(PRODUCT__id=i.id, USER__LOGIN_id=lid).delete()
    #     boj = ORDER_MAIN.objects.get(id=boj.id)
    #     boj.Amount = mytotal
    #     boj.save()


    lid = request.session['lid']
    # Get all items in the user's cart
    cart_items = CART.objects.filter(USER__LOGIN_id=lid)

    if cart_items.exists():
        # Create a new order
        boj = ORDER_MAIN()
        boj.USER = USER.objects.get(LOGIN_id=lid)
        boj.Amount = 0
        boj.Date = datetime.now().date()
        boj.Status = "pending"
        boj.save()

        mytotal = 0

        # Loop through cart items to create order sub-items
        for item in cart_items:
            bs = ORDER_SUB()
            bs.ORDERMAIN_id = boj.id
            bs.PRODUCT_id = item.PRODUCT.id
            bs.Quantity = item.Quantity
            bs.save()

            mytotal += (float(item.PRODUCT.Rate) * item.Quantity)

        # Update the total amount in the ORDER_MAIN table
        boj.Amount = mytotal
        boj.save()

        # Clear the user's cart after processing
        CART.objects.filter(USER__LOGIN_id=lid).delete()
    else:
        print("No items in the cart.")
    return HttpResponse("<script>alert('Buy success!!');window.location='/myapp/UserViewProduct/'</script>")

def User_directbuy(request,id):
    return render(request,"User/BuyProduct.html",{'id':id})
def User_directbuy_post(request):

    qty=request.POST["qty"]
    id=request.POST["id"]

    boj = ORDER_MAIN()
    boj.USER = USER.objects.get(LOGIN_id=request.session['lid'])
    boj.Amount = PRODUCT.objects.get(id=id).Rate*int(qty)
    boj.Date = datetime.now().date()
    boj.Status = "paid"
    boj.save()

    mytotal = 0

    bs = ORDER_SUB()
    bs.ORDERMAIN_id = boj.id
    bs.PRODUCT_id = id
    bs.Quantity = qty
    bs.save()

    return HttpResponse("<script>alert('Quantity successfully selected !!');window.location='/myapp/UserViewProduct/'</script>")
# def search(request):
#     src=request.POST['textfield']
#     obj=User.objects

