from rest_framework import generics, permissions, status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Client, ConflictCheck
from .serializers import ClientSerializer, ConflictCheckSerializer


# Custom permission — only lawyers access clients
class IsLawyer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'lawyer'


class ClientListCreateView(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    permission_classes = [IsLawyer]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    ordering_fields = ['created_at', 'first_name']

    def get_queryset(self):
        # Lawyer sees only their own clients
        return Client.objects.filter(lawyer=self.request.user)

    def perform_create(self, serializer):
        # Auto assign logged in lawyer
        serializer.save(lawyer=self.request.user)


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    permission_classes = [IsLawyer]

    def get_queryset(self):
        return Client.objects.filter(lawyer=self.request.user)


class ConflictCheckView(APIView):
    permission_classes = [IsLawyer]

    def post(self, request, client_id):
        client = get_object_or_404(Client, id=client_id, lawyer=request.user)

        # Check if email exists in other cases
        conflict_exists = Client.objects.filter(
            email=client.email
        ).exclude(id=client_id).exists()

        status_result = 'conflict' if conflict_exists else 'clear'

        conflict = ConflictCheck.objects.create(
            client=client,
            checked_by=request.user,
            status=status_result,
            notes='Auto conflict check based on email'
        )

        return Response({
            "message": f"Conflict check complete — {status_result.upper()}",
            "result": ConflictCheckSerializer(conflict).data
        })


class ClientStatsView(APIView):
    permission_classes = [IsLawyer]

    def get(self, request):
        clients = Client.objects.filter(lawyer=request.user)
        return Response({
            "total_clients": clients.count(),
            "active_clients": clients.filter(status='active').count(),
            "inactive_clients": clients.filter(status='inactive').count(),
            "blacklisted_clients": clients.filter(status='blacklisted').count(),
        })