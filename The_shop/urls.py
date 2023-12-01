from django.urls import path
from The_shop import views




urlpatterns=[path("",views.Home,name='home'),
             path("cate",views.CategorY,name='category_page'),
             path("scate/<str:cname>/",views.Sub_categorY,name='scategory_page'),
             path("sub_p_views/<str:sname>/",views.Sub_productview,name='subproductviews'),
             path("single/<str:pname>/",views.Single_product,name='singleproduct'),
             path('cart_p',views.CartDetails,name='cartpage'),
             path('add_cart/<int:product_id>/',views.add_cart,name='add_cart'),
             path('cart_decrement/<int:product_id>', views.min_cart, name='cart_decrement'),
             path('remove/<int:product_id>', views.delete_cart, name='remove'),
             path("search",views.Searching,name='search_page'),
             path("logi",views.Login,name="login"),
             path("reg",views.Register,name="register"),
             path("logo",views.Logout,name="logout"),
             path("check",views.Checkout,name='checkout'),
             path('abt',views.About,name='about'),
             path('cont',views.Contact,name='contact'),
             path('shop',views.Shop,name='shop'),
             ]