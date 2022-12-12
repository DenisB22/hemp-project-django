from django.urls import path

from final_project.category.views import home
from final_project.store.views import ProductListView

urlpatterns = (
    path('', home, name='home'),
)