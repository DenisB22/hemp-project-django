from django.contrib.auth.decorators import login_required
from django.urls import path

from final_project.accounts.views import register_user, login_user, activate, forgotPassword, \
    resetPassword, resetpassword_validate, change_password, EditProfileView, OrderDetail, MyOrders, \
    LogoutUser, Dashboard
from final_project.carts.views import cart

urlpatterns = (
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    # path('logout/', logout_user, name='logout_user'),
    path('logout/', login_required(LogoutUser.as_view()), name='logout_user'),
    # path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/', login_required(Dashboard.as_view()), name='dashboard'),
    # path('', dashboard, name='dashboard'),
    path('', login_required(Dashboard.as_view()), name='dashboard'),

    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('forgotPassword/', forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', resetPassword, name='resetPassword'),

    # path('my_orders/', my_orders, name='my_orders'),
    path('my_orders/', login_required(MyOrders.as_view()), name='my_orders'),
    path('edit_profile/', login_required(EditProfileView.as_view()), name='edit_profile'),
    # path('edit_profile/', edit_profile, name='edit_profile'),
    path('change_password/', change_password, name='change_password'),
    # path('order_detail/<int:order_id>/', order_detail, name='order_detail'),
    path('order_detail/<int:order_id>/', login_required(OrderDetail.as_view()), name='order_detail'),
)