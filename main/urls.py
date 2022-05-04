from django.urls import path
from . import views
from project.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home, name='home' ),
    path('carla', views.carla, name='carla' ),
    path('about', views.about, name='about'),
    path('last', views.last, name='last'),
    path('festival', views.festival, name='festival'),
    path('Art', views.Art, name='Art'),
    path('page', views.page, name='page'),
    path('end', views.end, name='end'),
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-book'),
    path('update/<int:book_id>', views.update_book),
    path('delete/<int:book_id>', views.delete_book),
    path('add_emp/', views.add_emp),
    

]
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)



