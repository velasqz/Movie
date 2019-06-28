from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from mdb.api.pagination import CustomPagination
from mdb.api.serializers import MovieRateSerializer, MovieSerializer
from mdb.models import MovieRate, Movie


class ExampleViewset(viewsets.ReadOnlyModelViewSet):
    queryset = MovieRate.objects.all()
    serializer_class = MovieRateSerializer


class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_classes = {
        'rate': MovieRateSerializer,
        'default': MovieSerializer
    }
    permission_classes = [DjangoModelPermissions, ]
    pagination_class = CustomPagination

#from mdb.api.serializers import MovieRateSerializerAll

# movierateall_detail = MovieRateSerializerAll.as_view({
#
#     'gt': 'list,',
#     'post': 'create',
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
#
# })

