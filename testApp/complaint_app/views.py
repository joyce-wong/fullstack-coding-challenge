from rest_framework import viewsets
from .models import UserProfile, Complaint
from .serializers import UserSerializer, UserProfileSerializer, ComplaintSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

def padDistrict(dist):
  dist = dist if len(dist) > 1 else '0' + dist
class ComplaintViewSet(viewsets.ModelViewSet):
  http_method_names = ['get']
  serializer_class = ComplaintSerializer
  queryset = Complaint.objects.all()
  def list(self, request):
    # Get all complaints from the user's district
    user = request.user
    userProfile = UserProfile.objects.get(user=user)

    complaints = self.queryset.filter(
      account__exact=padDistrict(userProfile.district)
    )
    
    serializer = ComplaintSerializer(complaints, many=True)
    return Response(serializer.data)

class OpenCasesViewSet(viewsets.ModelViewSet):
  http_method_names = ['get']
  def list(self, request):
    # Get only the open complaints from the user's district
    user = request.user
    userProfile = UserProfile.objects.get(user=user)
    complaints = self.queryset.filter(closedate=None)
    serializer = ComplaintSerializer(complaints, many=True)
    return Response(serializer.data)

class ClosedCasesViewSet(viewsets.ModelViewSet):
  http_method_names = ['get'] 
  def list(self, request):
    # Get only complaints that are close from the user's district
    user = request.user
    userProfile = UserProfile.objects.get(user=user)
    complaints = self.queryset.exclude(closedate=None)
    serializer = ComplaintSerializer(complaints, many=True)
    return Response(serializer.data)
    
class TopComplaintTypeViewSet(viewsets.ModelViewSet):
  http_method_names = ['get']
  def list(self, request):
    # Get the top 3 complaint types from the user's district
    return Response()