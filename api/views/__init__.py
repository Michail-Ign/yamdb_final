from .category_genre import CategoryViewSet, GenreViewSet
from .commentviewset import CommentViewSet
from .reviewviewset import ReviewViewSet
from .titles import TitelViewSet
from .userviewset import (RegistrationView, RequestForRegistrationView,
                          UserViewSet)

__All__ = [
    CommentViewSet,
    CategoryViewSet,
    GenreViewSet,
    ReviewViewSet,
    RegistrationView,
    RequestForRegistrationView,
    TitelViewSet,
    UserViewSet]
