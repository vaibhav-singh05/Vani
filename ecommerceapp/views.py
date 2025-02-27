from django.shortcuts import render, redirect
from ecommerceapp.models import Contact, Product
from django.contrib import messages
from math import ceil
from .models import Product,Contact,Order,OrderUpdate
# Create your views here.

def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod= Product.objects.filter(category=cat)
        n=len(prod)
        nSlides = n // 4 + ceil(n / 4)
        allProds.append([prod, range(1, nSlides), nSlides])
        
    params= {'allProds': allProds}
    return render(request, "index.html", params)



def contact(request):
    if request.user.is_anonymous:
        return redirect('auth/login')
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        desc = request.POST.get("desc")
        contact = Contact(nmae = name, email = email, phonenumber=mobile, desc=desc)
        contact.save()
        messages.info(request,"We will get back to you")
    return render(request, "contact.html")


def myprofile(request):
    if request.user.is_anonymous:
        return redirect('/auth/login')
    orders = Order.objects.filter(email=request.user.email).order_by('-order_id')
    return render(request, 'myprofile.html', {'user': request.user, 'orders': orders})



def checkout(request):
    if request.user.is_anonymous:
        return redirect('/auth/login')
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = float(request.POST.get('amt', 0))  # Convert to float
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        order = Order.objects.create(
            items_json=items_json, name=name, amount=amount, email=email,
            address1=address1, address2=address2, city=city, state=state,
            zip_code=zip_code, phone=phone
        )

        OrderUpdate.objects.create(order_id=order.order_id, update_desc="The order has been placed.")
        return redirect('payment', order_id=order.order_id)
    return render(request, 'checkout.html')


def payment(request):
    return render(request, "payment.html")






