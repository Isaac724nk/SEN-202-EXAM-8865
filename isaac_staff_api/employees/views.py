from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Manager, Intern
from .serializers import ManagerSerializer, InternSerializer

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class InternViewSet(viewsets.ModelViewSet):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer

# Polymorphic View
class StaffRoleView(APIView):
    def get(self, request):
        managers = Manager.objects.all()
        interns = Intern.objects.all()

        roles = []

        for manager in managers:
            roles.append({
                'name': f'{manager.first_name} {manager.last_name}',
                'role': manager.get_role()
            })

        for intern in interns:
            roles.append({
                'name': f'{intern.first_name} {intern.last_name}',
                'role': intern.get_role()
            })

        return Response(roles)
