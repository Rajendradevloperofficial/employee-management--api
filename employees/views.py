from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all().order_by('id')

    
    def get_queryset(self):
        queryset = super().get_queryset()
        department = self.request.query_params.get('department')
        role = self.request.query_params.get('role')

        if department:
            queryset = queryset.filter(department__iexact=department)
        if role:
            queryset = queryset.filter(role__iexact=role)

        return queryset

   
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        email = request.data.get('email')

        if email and Employee.objects.exclude(id=instance.id).filter(email=email).exists():
            return Response(
                {"email": "Employee with this email already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().update(request, *args, **kwargs)

    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
