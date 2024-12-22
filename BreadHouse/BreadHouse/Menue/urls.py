from xml.etree.ElementInclude import include
from .views import views,UserViews,CategoryViews,ProductViews
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("register/",UserViews.register,name="register"),


    path('feedback/create/', views.feedback_create, name='feedback_create'),
    path('feedback/', views.feedback_list, name='feedback_list'),
    path('users_feedbacks/', views.users_feedback_list, name='users_feedbacks'),
    path('feedback/delete/<int:pk>/', views.feedback_delete, name='feedback_delete'),
    path('category/create/', CategoryViews.category_create, name='category_create'),
    path('category/', CategoryViews.categories_list, name='category_list'),
    path('category/update/<int:pk>/', CategoryViews.category_update, name='category_update'),
    path('category/delete/<int:pk>', CategoryViews.category_delete, name='category_delete'),
    path('product/product/', ProductViews.product_create, name='product_create'),
    path('product/', ProductViews.product_list, name='product_list'),
    path('product/update/<int:pk>/', ProductViews.product_update, name='product_update'),
    path('product/delete/<int:pk>', ProductViews.product_delete, name='product_delete'),
    path('new_item/new_item/', views.new_item_create, name='new_item_create'),
    path('new_item/', views.new_items_list, name='new_item_list'),
    path('new_item/delete/<int:pk>/', views.delete_new_item, name='new_item_delete'),
    path('trend_item/trend_item/', views.trend_item_create, name='trend_item_create'),
    path('trend_item/', views.trend_item_list, name='trend_item_list'),
    path('trend_item/delete/<int:pk>/', views.delete_trend_item, name='trend_item_delete'),
    path('offer/offer/', views.offer_create, name='offer_create'),
    path('offer/', views.offer_list, name='offer_list'),
    path('offer/update/<int:pk>/', views.offer_update, name='offer_update'),
    path('offer/delete/<int:pk>', views.delete_offer, name='offer_delete'),
    path('category/<int:category_id>/', views.category_items, name='category_items'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)