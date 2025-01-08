# shop/urls.py
from django.urls import path
from . import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


schema_view = get_schema_view(
    openapi.Info(
        title="Shop API",
        default_version='v1',
        description="API documentation for the shop system",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="shop@example.com"),
        license=openapi.License(name="BSD License"),
        security=[  # Add security in the Info object
            {
                'Bearer': [
                    {
                        'type': 'apiKey',
                        'in': 'header',
                        'name': 'Authorization',
                    }
                ]
            }
        ],
    ),
    public=True,
    permission_classes=[AllowAny],  # Allow access to Swagger UI without authentication
)

# Define your API URL patterns
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('categories/', views.category_list, name='category-list'),
    path('categories/<int:pk>/', views.category_detail, name='category-detail'),
    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
    path('users/', views.create_user, name='create-user'),

    # Swagger UI and ReDoc views
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),  # Swagger UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-ui'),  # ReDoc UI (optional)
]
