from commonbox.models import *
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.serializers import Serializer

class CommonResource(ModelResource):
    class Meta:
        queryset = TELEMETRY_NEW10.objects.all()
        resource_name = 'common'
        excludes = ['iden', 'total_detected_apps', 'meta', 'resource_uri']
        authorization= Authorization()
        serializer = Serializer()
