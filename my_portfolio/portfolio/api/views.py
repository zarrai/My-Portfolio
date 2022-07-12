from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet

from .serializers import (
    EducationSerializer,
    CompetenceSerializer,
    ExperienceSerializer,
    ProjectSerializer,
    InformationSerializer,
    )
from my_portfolio.portfolio.models import (
    Competence,
    Education,
    Experience,
    Project,
    Information,
)



class PortfolioViewSet(ObjectMultipleModelAPIViewSet):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    querylist = [
        {'queryset': Competence.objects.all(), 'serializer_class': CompetenceSerializer},
        {'queryset': Experience.objects.all(), 'serializer_class': ExperienceSerializer},
        {'queryset': Education.objects.all(), 'serializer_class': EducationSerializer},
        {'queryset': Project.objects.all(), 'serializer_class': ProjectSerializer},
        {'queryset': Information.objects.all(), 'serializer_class': InformationSerializer},
    ]