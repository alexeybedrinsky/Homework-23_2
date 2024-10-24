from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from users.views import RegisterView, CustomLoginView, PasswordResetView, verify_email, UserProfileUpdateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),
    path('blog/', include('blog.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('verify/<uidb64>/<token>/', verify_email, name='verify_email'),
    path('profile/edit/', UserProfileUpdateView.as_view(), name='profile_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)