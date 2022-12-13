from django.test import SimpleTestCase
from django.urls import reverse, resolve
from final_project.accounts.views import register_user, login_user, LogoutUser, activate, Dashboard, forgotPassword, resetpassword_validate, resetPassword, MyOrders, EditProfileView, change_password, OrderDetail


class TestUrls(SimpleTestCase):

    def test_register_user_url_is_resolved(self):
        url = reverse('register_user')
        self.assertEquals(resolve(url).func, register_user)

    def test_login_user_url_is_resolved(self):
        url = reverse('login_user')
        self.assertEquals(resolve(url).func, login_user)

    def test_logout_user_url_is_resolved(self):
        url = reverse('logout_user')
        self.assertEquals(resolve(url).func.view_class, LogoutUser)

    def test_activate_url_is_resolved(self):
        url = reverse('activate', args=['uidb64', 'token'])
        self.assertEquals(resolve(url).func, activate)

    def test_dashboard_url_is_resolved(self):
        url = reverse('dashboard')
        self.assertEquals(resolve(url).func.view_class, Dashboard)

    def test_forgot_password_url_is_resolved(self):
        url = reverse('forgotPassword')
        self.assertEquals(resolve(url).func, forgotPassword)

    def test_resetpassword_validate_url_is_resolved(self):
        url = reverse('resetpassword_validate', args=['uidb64', 'token'])
        self.assertEquals(resolve(url).func, resetpassword_validate)

    def test_reset_password_url_is_resolved(self):
        url = reverse('resetPassword')
        self.assertEquals(resolve(url).func, resetPassword)

    def test_my_orders_url_is_resolved(self):
        url = reverse('my_orders')
        self.assertEquals(resolve(url).func.view_class, MyOrders)

    def test_edit_profile_view_url_is_resolved(self):
        url = reverse('edit_profile')
        self.assertEquals(resolve(url).func.view_class, EditProfileView)

    def test_change_password_view_url_is_resolved(self):
        url = reverse('change_password')
        self.assertEquals(resolve(url).func, change_password)

    def test_order_detail_view_url_is_resolved(self):
        url = reverse('order_detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, OrderDetail)
