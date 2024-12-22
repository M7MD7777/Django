from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views import View   
from ..models import Product
from ..forms import ProductForm
from ..decorators import admin_required 

@admin_required
def product_create(request):
    if request.method=="POST":
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            product=form.save()
            product.save()
            return redirect('product_list')
        
    else:
        form=ProductForm()
    return render(request,'product/product_form.html',{'form':form})        

@admin_required
def product_update(request,pk):
    product=get_object_or_404(Product,pk=pk)
    if request.method=="POST":
        form=ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form=ProductForm(instance=product)
    return render(request,'product/product_form.html',{'form':form}) 

def product_list(request):
    products=Product.objects.all()
    return render(request,'product/product_list.html',{'products':products})

@admin_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product/product_confirm_delete.html', {'product': product})



