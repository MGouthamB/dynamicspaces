from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('add-post', views.add_post, name='add-post'),
    path('edit-post', views.edit_post, name='edit-post'),
    path('adding-job', views.adding_job, name='adding-job'),
    path('editing-job', views.editing_job, name='editing-job'),
    path('GroziitDynamicSpace', views.GroziitDynamicSpace, name='GroziitDynamicSpace'),
    path('postdetail', views.postdetail, name='postdetail'),
    path('payment', views.payment, name='payment'),
    path('cancelsub', views.cancelsub, name='cancelsub'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('pages-contact', views.pages_contact, name="pages-contact"),
    path('pages-login', views.pages_login, name="pages-login"),
    path('pages-register', views.pages_register, name="pages-register"),
    path('users-profile', views.users_profile, name="users-profile"),
    path('edit-profile', views.edit_profile, name="edit_profile"),
    path('change-password', views.change_password, name="change-password"),
    path('dynamicspace-form',views.dynamicspace_form,name="dynamicspace-form"),
    path('GroziitFromview',views.GroziitFromview,name="GroziitFromview")
    # path('dynamicspace', views.)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
