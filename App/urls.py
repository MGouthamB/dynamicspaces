from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('add-post', views.add_post, name='add-post'),
    path('add-content', views.add_content, name='add-content'),
    path('edit-post', views.edit_post, name='edit-post'),
    path('edit-content', views.edit_content, name='edit-content'),
    path('delete-post', views.delete_post, name='delete-post'),
    path('delete-content', views.delete_content, name='delete-content'),
    path('adding-job', views.adding_job, name='adding-job'),
    path('editing-job', views.editing_job, name='editing-job'),
    path('GroziitDynamicSpace', views.GroziitDynamicSpace, name='GroziitDynamicSpace'),
    path('postdetail/<str:id>/<int:integration_id>', views.integration_detail, name='integration_detail'),
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
    path('dynamicspace-form/<str:id>/<int:integration_id>',views.integrations_form,name="integrations_form"),
    path('GroziitFromview',views.GroziitFromview,name="GroziitFromview"),
    path('GroziitApplicationsView',views.GroziitApplicationsView,name="GroziitApplicationsView"),
    path('GroziitImageview',views.GroziitImageview,name="GroziitImageview"),
    path('GroziitRemoveImage',views.GroziitRemoveImage,name="GroziitRemoveImage"),
    path('GroziitContentAPI',views.GroziitContentAPI,name="GroziitContentAPI"),
    path('GroziitIntegrations',views.GroziitIntegrations,name="GroziitIntegrations"),
    path('GroziitIntegrations/<int:id>',views.GroziitIntegrationsDetails,name="GroziitIntegrationsDetails"),

    path("test",views.test,name="test")
    # path('dynamicspace', views.)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
