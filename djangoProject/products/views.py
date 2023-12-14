from django.shortcuts import render

# Create your views here.
from .models import Product
def porduct_detail_view(request, id):
    obj=Product.objects.all(id=1)
    return render(request, "product/detail.html", context={"title":obj.title, "decription":obj.decription})
