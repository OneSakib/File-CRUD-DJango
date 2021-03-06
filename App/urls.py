from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'app'

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('login/', views.LoginForm.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.SignUpForm.as_view(), name='signup'),
    path('update/<int:pk>', views.UpdateData.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteData.as_view(), name='delete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
