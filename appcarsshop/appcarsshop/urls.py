from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, users, products, \
            ProductViewSet, \
            OrderViewSet, \
            ProductOrderedViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'ordersProducts', ProductOrderedViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('usersView/', users),
    path('productView/', products),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
