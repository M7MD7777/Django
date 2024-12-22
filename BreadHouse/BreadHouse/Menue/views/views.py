from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from ..models import Category, Feedback,NewItem, Product,TrendItem,Offer
from ..forms import FeedbackForm,NewItemForm,TrendItemForm,OfferForm
from ..decorators import admin_required 




def home(request):
    categories = Category.objects.all()
    new_items = NewItem.objects.all()
    trend_items = TrendItem.objects.all()
    offers = Offer.objects.all()
    return render(request, 'home.html',{'categories': categories,'new_items': new_items,'trend_items':trend_items,'offers':offers})

def dashboard(request):
    return render(request, 'dashboard.html')

def feedback_create(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)  
            feedback.user = request.user.profile
            feedback.save()  
            return redirect("feedback_list")
    else:
        form = FeedbackForm()  

    return render(request, 'feedback/feedback_form.html', {'form': form})  


def feedback_list(request):
    feedbacks= Feedback.objects.filter(user=request.user.profile)
    return render(request,'feedback/feedback_list.html',{'feedbacks':feedbacks})

def feedback_delete(request,pk):
    feedback= get_object_or_404(Feedback, pk=pk)
    if request.method=='POST':
        feedback.delete()
        return redirect('feedback_list')
    return render(request,'feedback/feedback_confirm_delete.html',{'feedback':feedback})

@admin_required
def new_item_create(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('new_item_list')
    else:
        form = NewItemForm()
    return render(request, 'new_item/new_item_form.html', {'form': form})


def new_items_list(request):
    new_items = NewItem.objects.all()
    return render(request, 'new_item/new_item_list.html', {'new_items': new_items})

@admin_required
def delete_new_item(request, pk):
    new_item = get_object_or_404(NewItem, pk=pk)
    if request.method == 'POST':
        new_item.delete()
        return redirect('new_item_list')
    return render(request, 'new_item/new_item_confirm_delete.html', {'new_item': new_item})

@admin_required
def trend_item_create(request):
    if request.method == 'POST':
        form =TrendItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trend_item_list')
    else:
        form=TrendItemForm()
    return render(request,'trend_item/trend_item_form.html',{'form':form})  

def trend_item_list(request):
    trend_items=TrendItem.objects.all()
    return render(request,'trend_item/trend_item_list.html',{'trend_items':trend_items}) 

@admin_required
def delete_trend_item(request,pk):
    trend_item=get_object_or_404(TrendItem,pk=pk)
    if request.method=='POST':
        trend_item.delete()
        return redirect('trend_item_list')
    return render(request,'trend_item/trend_item_confirm_delete.html',{'trend_item':trend_item})
        
@admin_required
def offer_create(request):
    if request.method=='POST':
        form=OfferForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('offer_list')
    else:
        form=OfferForm()
    return render(request,'offer/offer_form.html',{'form':form})

@admin_required
def offer_update(request,pk):
    offer=get_object_or_404(Offer,pk=pk)
    if request.method=='POST':
        form=OfferForm(request.POST,request.FILES,instance=offer)
        if form.is_valid():
            form.save()
            return redirect('offer_list')
    else:
        form=OfferForm(instance=offer)
    return render(request,'offer/offer_form.html',{'form':form})


def offer_list(request):
    offers=Offer.objects.all()
    return render(request,'offer/offer_list.html',{'offers':offers})

@admin_required
def delete_offer(request,pk):
    offer=get_object_or_404(Offer,pk=pk)
    if request.method=='POST':
        offer.delete()
        return redirect('offer_list')
    
    return render(request,'offer/offer_list.html',{'offer':offer})


def users_feedback_list(request):
    feedbacks= Feedback.objects.all()
    return render(request,'feedback/users_feedbacks.html',{'feedbacks':feedbacks})


def category_items(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(category=category)
    
    return render(request, 'product/category_items.html', {'category': category, 'products': products})

def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product/product_details.html', {'product': product})