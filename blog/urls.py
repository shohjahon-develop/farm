from django.urls import path
from .views import (index, contact, blog, about, detail,
                    team, testimonial, feature, product, service,
                    modelsdetailview, productsdetailview, fermersdetailview, latesdetailview, wesdetailview,
                    namesdetailview, postsdetailview, loremsdetailview, oursdetailview, ProductUpdateView,
                    ProductDeleteView, productsDetail, ProductCreateView)


urlpatterns = [
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('', index, name='index'),
    path('detail/',detail,name='detail'),
    path('team/', team, name='team'),
    path('testimonial/', testimonial, name='testimonial'),
    path('feature/', feature, name='feature'),
    path('product/', product, name='product'),
    path('service/', service, name='service'),
    path('models/<int:id>', modelsdetailview, name='modelsDetail'),
    path('products/<slug:products>', productsdetailview, name='productsDetail'),
    path('fermers/<int:id>', fermersdetailview, name='fermersDetail'),
    path('lates/<int:id>', latesdetailview, name='latesDetail'),
    path('wes/<int:id>', wesdetailview, name='wesDetail'),
    path('names/<int:id>', namesdetailview, name='namesDetail'),
    path('ours/<int:id>', oursdetailview, name='oursDetail'),
    path('posts/<int:id>', postsdetailview, name='postsDetail'),
    path('lorems/<int:id>', loremsdetailview, name='loremsDetail'),
    path('products/edit/<slug>/', ProductUpdateView.as_view(),name="productsUpdate",),
    path('products/delete/<slug>/',ProductDeleteView.as_view(), name = 'productsDelete'),
    path('products/<slug:products>/',productsDetail, name='productsDetail'),
    path("products/create/",ProductCreateView.as_view(),name="products_create"),
]