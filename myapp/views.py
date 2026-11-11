from myapp.models import Product
from django.shortcuts import render, redirect
from myapp.my_forms import ProductForm

# Create your views here.
def home(request):
    products = Product.objects.all() #select * from products
    # for product in products:
    #     print(product.name, product.price)
    return render(request, "home.html",{"products":products})

def add(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        #validates the data input is correct
        if  form.is_valid():
            form.save()
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