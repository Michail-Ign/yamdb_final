from django.urls import include, path

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from .views import (
    CategoryViewSet,
    CommentViewSet,
    GenreViewSet,
    RegistrationView,
    RequestForRegistrationView,
    ReviewViewSet,
    TitelViewSet,
    UserViewSet
)

router_v1 = DefaultRouter()
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments for review'
)
router_v1.register(
    (r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/'
     r'comments/(?P<comment_id>\d+)'),
    CommentViewSet,
    basename='current comment for review'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)',
    ReviewViewSet,
    basename='current review for title'
)
router_v1.register('categories', CategoryViewSet)
router_v1.register('genres', GenreViewSet)
router_v1.register('titles', TitelViewSet)
router_v1.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/email/', RequestForRegistrationView.as_view(),
         name='registration'),
    path('v1/auth/token/', RegistrationView.as_view(),
         name='token_obtain_pair'),
    path('v1/auth/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
