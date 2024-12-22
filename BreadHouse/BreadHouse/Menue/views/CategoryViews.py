from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views import View
from ..models import Category
from ..forms import CategoryForm
from ..decorators import admin_required 

@admin_required
def category_create(request):
    if request.method=='POST':
        form=CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            category = form.save() 
            category.save()  
            return redirect('category_list')
    else:
        form = CategoryForm()  

    return render(request, 'category/category_form.html', {'form': form}) 

@admin_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST,request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category/category_form.html', {'form': form})


def categories_list(request):
    categories= Category.objects.all()
    return render(request,'category/category_list.html',{'categories':categories})


@admin_required        
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category/category_confirm_delete.html', {'category': category})