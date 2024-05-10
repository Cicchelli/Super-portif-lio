from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets
from .models import Profile, Project, CertifyingInstitution, Certificate
from .serializers import (
    CertificateSerializer,
    CertifyingInstitutionSerializer,
    ProfileSerializer,
    ProjectSerializer,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from django.shortcuts import render


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if request.method == "GET":
            profile = Profile.objects.get(id=kwargs["pk"])

            return render(
                request,
                "profile_detail.html",
                {
                    "profile": profile,
                    "certificates": profile.certificates.all(),
                    "projects": profile.projects.all(),
                },
            )
        return super().retrieve(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer
    permission_classes = [IsAuthenticated]


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated]
