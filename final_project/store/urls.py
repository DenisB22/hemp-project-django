from django.urls import path


from final_project.store.views import store, product_details, product_search, submit_review, ProductsListApiView, \
    CategoriesListApiView, DemoApiView

urlpatterns = (
    path('', store, name='store'),
    path('category/<slug:category_slug>/', store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', product_details, name='product_details'),
    path('search/', product_search, name='search'),
    path('submit_review/<int:product_id>/', submit_review, name='submit_review'),

    # REST
    path('products/', ProductsListApiView.as_view(), name='api list products'),
    path('categories/', CategoriesListApiView.as_view(), name='api list categories'),
    path('demo/', DemoApiView.as_view(), name='demo view'),
)
