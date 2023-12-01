from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect,get_object_or_404
from .models import *



# Create your views here.

def Home(request):
     cate = Category.objects.all()
     ap = All_products.objects.all()
     pagination = Paginator(ap,6)
     page_num = request.GET.get('page')
     page_obj = pagination.get_page(page_num)
     total_page = page_obj.paginator.num_pages
     total_page_list = [n+1 for n in range(total_page)]

     return render(request,"index.html",{'cato':cate,'prod':page_obj,'tot':total_page,'num':total_page_list})

def CategorY(request):
    cate = Category.objects.all()


    return render(request,"category.html",{'cato':cate})


def Sub_categorY(request,cname):
    sc= Sub_category.objects.filter(category__name=cname)
    return render(request,'subcategory.html',{'sub':sc})

def Sub_productview(request,sname):
    sp = All_products.objects.filter(sub_category__sub_name=sname)

    return render(request,'sub_product_view.html',{'sub':sp})

def Single_product(request,pname):
    pro = All_products.objects.filter(all_name=pname).first()

    print('product id',pro.id)
    return render(request,'single-product.html',{'prod':pro})





    return render(request,'cart.html',{'prod':save})
def Searching(request):
    pro = None
    quary = None
    if 'q' in request.GET:
        quary = request.GET.get('q')
        pro = All_products.objects.all().filter(Q(all_name__icontains=quary)|Q(description__icontains=quary))
    return render (request,'search.html',{'qr':quary,'pr':pro})


def Login(request):
    if request.method=='POST':
        Fname=request.POST.get('uname')
        Psd=request.POST.get('psd')
        log_user=auth.authenticate(username=Fname,password=Psd)
        if log_user is not None:
            auth.login(request,log_user)
            return redirect("/")

        else:
            messages.info(request,"Incorrect username or password")
            return redirect("login")
    return render(request,"Login.html")

def Logout(request):
    auth.logout(request)
    return redirect("/")

def Register(request):
    if request.method=='POST':
        Fname=request.POST['fname']
        Sname=request.POST['sname']
        Email=request.POST['email']
        Psd=request.POST['psd']
        if User.objects.filter(username=Email).exists():
            messages.info(request,"User already exist!")
        else:
            data=User.objects.create_user(username=Email,first_name=Fname,last_name=Sname,password=Psd)
            data.save()
            return redirect("login")


    return render(request,"Register.html")




def CartDetails(request,tot=0,count=0,ftot=0):
    cart_items = None
    try:
        ct = Cart.objects.get(cart_id=cart_id(request))
        cart_items = Items.objects.filter(cart=ct,active=True)
        print('cartitems',cart_items)

        for i in cart_items:
            tot+=(i.products.discount_p*i.quantity)
            count +=i.quantity
            ftot = tot + 45
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',{'cart':cart_items,'tot':tot,'count':count,'ftot':ftot})

def cart_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id


class Product:
    pass


def add_cart(request,product_id):
    product=All_products.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=cart_id(request))
        cart.save()
    try:
        c_items=Items.objects.get(products=product,cart=cart)
        if c_items.quantity < c_items.products.stock:
            c_items.quantity+=1
            c_items.save()
    except Items.DoesNotExist:
        c_items=Items.objects.create(products=product,quantity=1,cart=cart)
        c_items.save()
    return redirect('cartpage')

def min_cart(request,product_id):
    ct=Cart.objects.get(cart_id=cart_id(request))
    print('cart', ct)
    prod= get_object_or_404(All_products,id=product_id)
    c_items=Items.objects.get(products=prod,cart=ct)
    if c_items.quantity > 1:
        c_items.quantity-= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect("cartpage")


def delete_cart(request,product_id):
    ct = Cart.objects.get(cart_id=cart_id(request))
    prod = get_object_or_404(All_products, id=product_id)
    c_items = Items.objects.get(products=prod, cart=ct)
    c_items.delete()
    return redirect("cartpage")


def Checkout(request):
    cart_items = None
    tot = 0
    ftot=0
    cart_items = Items.objects.all()
    try:
        for i in cart_items:
            tot += (i.products.price * i.quantity)
            ftot = ftot + 45

    except tot.DoesNotExist:
        messages.info(request,"no products inside the cart")
        return redirect('cartpage')

    return render(request,'checkout.html',{'item':cart_items,'totalprice':tot,'ftot':ftot})


def About(request):

    return render(request,'about.html')


def Contact(request):

    return render(request,'contact.html')


def Shop(request):
    all=All_products.objects.all()


    return render(request,'shop.html',{'all':all})