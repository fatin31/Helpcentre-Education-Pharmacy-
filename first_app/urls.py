
from django.urls import re_path,path
from first_app import views
from django.contrib import admin


urlpatterns = [
   #re_path(r'^$', views.student, name='student'),
    re_path(r'^$', views.index, name='index'),
    path('log_in/',views.user_login,name='login'),
    path('education/',views.education,name='eduaction'),
    path('sign_up/',views.sign_up,name='login'),
    path('sign_up/log_in/sign_up/',views.sign_up,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('logout/login/',views.user_login,name='login'),
    path('sign_up/log_in/',views.user_login,name='login'),
    path('sign_up/login/',views.user_login,name='login'),
    path('login/',views.user_login,name='login'),
    path('login/sign_up/',views.sign_up,name='signup'),
    path('login/sign_up/login/',views.user_login,name='login'),
    
    path('search/', views.search_results, name='search_results'),
    path('dhaka/',views.Dhaka,name='dhaka'),
    path('education/dhaka/',views.Dhaka,name='dhaka'),
    path('khulna/',views.Khulna,name='khulna'),
    path('education/khulna/',views.Khulna,name='khulna'),
    path('rangpur/',views.Rangpur,name='rangpur'),
    path('education/rangpur/',views.Rangpur,name='rangpur'),
    path('barishal/',views.Barishal,name='barishal'),
    path('education/barishal/',views.Barishal,name='barishal'),
    path('chittagong/',views.Chittagong,name='chittagong'),
    path('education/chittagong/',views.Chittagong,name='chittagong'),
    path('msingh/',views.Mymensingh,name='mymensingh'),
    path('education/msingh/',views.Mymensingh,name='mymensingh'),
    path('raj/',views.Rajshahi,name='rajshahi'),
    path('education/raj/',views.Rajshahi,name='rajshahi'),
    path('slet/',views.Sylhet,name='sylhet'),
    path('education/slet/',views.Sylhet,name='sylhet'),

    path('pharmacy/',views.Pharmacy,name='pharmacy'),
    path('diabetics/',views.Diabetic,name='diabetics'),
    path('pharmacy/diabetics/',views.Diabetic,name='diabetics'),
    path('otc/',views.otc,name='otc'),
    path('pharmacy/otc/',views.otc,name='otc'),
    path('babycare/',views.babycare,name='babycare'),
    path('pharmacy/babycare/',views.babycare,name='babycare'),
    path('wchoice/',views.womenchoice,name='womenchoice'),
    path('pharmacy/wchoice/',views.womenchoice,name='womenchoice'),
    path('pharmacy/wchoice/add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('pcare/',views.personalcare,name='pcare'),
    path('pharmacy/pcare/',views.personalcare,name='pcare'),
    path('swness/',views.wellness,name='swness'),
    path('pharmacy/swness/',views.wellness,name='swness'),
    path('add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('pharmacy/diabetics/add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('quicktest/',views.quick_test,name='quicktest'),
    path('pharmacy/diabetics/quicktest/',views.quick_test,name='quicktest'),
    path('ordernow/',views.Order,name='order'),
    path('pharmacy/diabetics/ordernow/',views.Order,name='order'),
    path('checkout/', views.checkout, name='checkout'),

    path('confirm/',views.confirm,name='confirm'),
    path('checkout/confirm/',views.orderlist,name='confirm'),
    






    path('edulist/',views.eduList,name='eduaction'),


]
