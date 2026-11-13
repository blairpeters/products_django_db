from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from myapp.models import Product
from django.shortcuts import render, redirect, get_object_or_404
from myapp.my_forms import ProductForm

# Create your views here.
@login_required
def home(request):
    products = Product.objects.all() #select * from products
    # for product in products:
    #     print(product.name, product.price)
    return render(request, "home.html",{"products":products})

@login_required
def add(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        #validates the data input is correct
        if  form.is_valid():
            form.save()
            messages.success(request, "Product successfully Added")
            #return redirect from django shortcuts so that when someone clicks submit it redirects back to home
            return redirect('home')

    else:
        form = ProductForm()


    return render(request,"add.html",{"form":form})


# hardcoding product row to the table is shown below

# Product.objects.create(name="Unga",
#                            code="0123334",
#                            price=250.0,
#                            cost=100.0,
#                            category="foods",
#                            for_sale=False)

@login_required
def delete_product(request,id):
    product = Product.objects.get(id=id)#select * from product where id = requested
    product.delete() #deletes the product
    messages.success(request, f"{product.name} permanently deleted")
    return redirect('home')

@login_required
def edit_product(request,id):
    products = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductForm(request.POST,instance=products)#instance = products pre loads the form ith the products data
        #validates the data input is correct
        if  form.is_valid():
            form.save()
            messages.success(request,"Product successfully Updated")
            #return redirect from django shortcuts so that when someone clicks submit it redirects back to home
            return redirect('home')

    else:
        form = ProductForm(instance=products)


    return render(request,"edit.html",{"form":form})

@login_required
def details(request,id):
    product = get_object_or_404(Product,id=id)
    return render(request,"details.html",{"product":product})


def signin(request):
    if request.method == "POST":
        #use built bin django authentication form
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('home')

    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    return None

#add a decorator to make sure before doing all this you are logged in...a decorator starts with @

@login_required
def signout(request):
    if request.method == "POST":
        logout(request)
    return redirect('login')