from django.urls import path
from .views import login_view,register_login,logout_view,user_update_view,delete_user
app_name='accounts'
urlpatterns=[
    path('login/',login_view,name='login'),
    path('register/',register_login,name='reg'),
    path('login_out/',logout_view,name='logout'),
    path('update/', user_update_view, name='update'),
    path('delete/', delete_user, name='delete'),

]