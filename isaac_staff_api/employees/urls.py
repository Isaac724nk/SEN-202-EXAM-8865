from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ManagerViewSet, InternViewSet, StaffRoleView

router = DefaultRouter()
router.register(r'managers', ManagerViewSet)
router.register(r'interns', InternViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('staff-roles/', StaffRoleView.as_view(), name='staff-roles'),
]
