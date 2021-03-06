from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

userRouter = DefaultRouter()
userRouter.register('userslist/', UsersView)
# userRouter.register('cart/<int:id>/', CartUpdateView)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="reg"),
    path("login/", LoginView.as_view(), name="log"),
    path("wishlist/", WishlistAPI.as_view()),
    # path("cart/", CartView.as_view(), name="cart"),
    # test cart with id
    path("<int:id>/cart/", CartView.as_view(), name="cart"),
    path("cart/<int:pk>",CartUpdateView.as_view({'put': 'update'}), name="updateCart"),
]
urlpatterns += userRouter.urls
