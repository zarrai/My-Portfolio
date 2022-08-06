from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from my_portfolio.portfolio.models import (
    Competence,
    Education,
    Experience,
    Information,
    Project,
)

from .serializers import (
    CompetenceSerializer,
    EducationSerializer,
    ExperienceSerializer,
    InformationSerializer,
    ProjectSerializer,
)


class PortfolioViewSet(ObjectMultipleModelAPIViewSet):
    authentication_classes = []  # disables authentication
    permission_classes = []  # disables permission
    querylist = [
        {
            "queryset": Competence.objects.all(),
            "serializer_class": CompetenceSerializer,
        },
        {
            "queryset": Experience.objects.all(),
            "serializer_class": ExperienceSerializer,
        },
        {"queryset": Education.objects.all(), "serializer_class": EducationSerializer},
        {"queryset": Project.objects.all(), "serializer_class": ProjectSerializer},
        {
            "queryset": Information.objects.all(),
            "serializer_class": InformationSerializer,
        },
    ]


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminUser]


class CompetenceViewSet(viewsets.ModelViewSet):
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer
    permission_classes = [IsAdminUser]


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsAdminUser]


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAdminUser]


class InformationViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    permission_classes = [IsAdminUser]
