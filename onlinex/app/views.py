from django import views
from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm


# def home(request):
#  return render(request, 'app/home.html')
class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category="TW")
        bottomwears = Product.objects.filter(category="BW")
        mobile = Product.objects.filter(category="M")
        laptop = Product.objects.filter(category="L")

        return render(
            request,
            "app/home.html",
            {
                "topwears": topwears,
                "bottomwears": bottomwears,
                "mobile": mobile,
                "laptop": laptop,
            },
        )


# def product_detail(request):
#  return render(request, 'app/productdetail.html')
class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, "app/productdetail.html", {"product": product})


def add_to_cart(request):
    return render(request, "app/addtocart.html")


def buy_now(request):
    return render(request, "app/buynow.html")


def profile(request):
    return render(request, "app/profile.html")


def address(request):
    return render(request, "app/address.html")


def orders(request):
    return render(request, "app/orders.html")


def change_password(request):
    return render(request, "app/changepassword.html")


def mobile(request, data=None):
    if data is None:
        mobiles = Product.objects.filter(category="M")
    elif data in ["Redmi", "Samsung", "Apple", "Motrola", "Poco", "redmi"]:
        mobiles = Product.objects.filter(category="M", brand=data)
    elif data == "below":
        mobiles = Product.objects.filter(category="M", discounted_price__lt=10000)
    elif data == "above":
        mobiles = Product.objects.filter(category="M", discounted_price__gt=10000)
    else:
        # Handle invalid data parameter, maybe return an empty queryset or raise an error
        mobiles = Product.objects.none()

    return render(request, "app/mobile.html", {"mobiles": mobiles})


def laptop(request, data=None):
    if data is None:
        laptops = Product.objects.filter(category="L")
    elif data in ["HP", "Samsung", "Apple", "Dell", "Asus", "redmi"]:
        laptops = Product.objects.filter(category="L", brand=data)
    elif data == "below":
        laptops = Product.objects.filter(category="L", discounted_price__lt=30000)
    elif data == "above":
        laptops = Product.objects.filter(category="L", discounted_price__gt=30000)
    else:
        # Handle invalid data parameter, maybe return an empty queryset or raise an error
        laptops = Product.objects.none()

    return render(request, "app/laptop.html", {"laptops": laptops})


def topwear(request, data=None):
    if data is None:
        topwears = Product.objects.filter(category="TW")
    elif data in ["Lee", "Jockey", "Copper", "HRX", "XHR", "Discy", "Allen"]:
        topwears = Product.objects.filter(category="TW", brand=data)
    elif data == "below":
        topwears = Product.objects.filter(category="TW", discounted_price__lt=1000)
    elif data == "above":
        topwears = Product.objects.filter(category="TW", discounted_price__gt=1000)
    else:
        # Handle invalid data parameter, maybe return an empty queryset or raise an error
        topwears = Product.objects.none()

    return render(request, "app/topwear.html", {"topwears": topwears})


def bottomwear(request, data=None):
    if data is None:
        bottomwears = Product.objects.filter(category="BW")
    elif data in ["Lee", "XHR", "Allen", "Spyker"]:
        bottomwears = Product.objects.filter(category="BW", brand=data)
    elif data == "below":
        bottomwears = Product.objects.filter(category="BW", discounted_price__lt=1000)
    elif data == "above":
        bottomwears = Product.objects.filter(category="BW", discounted_price__gt=1000)
    else:
        # Handle invalid data parameter, maybe return an empty queryset or raise an error
        bottomwears = Product.objects.none()

    return render(request, "app/bottomwear.html", {"bottomwears": bottomwears})


def login(request):
    return render(request, "app/login.html")


# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, "app/customerregistration.html", {"form": form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

        return render(request, "app/customerregistration.html", {"form": form})


def checkout(request):
    return render(request, "app/checkout.html")
