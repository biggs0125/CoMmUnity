from django.views.generic import View
from tags.models import Tag
from organizations.models import Organization
from users.models import OurUser
from django.core import serializers
from apis.CORSHttp import CORSHttpResponse
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import json

class GetTag(View):

    def dispatch(self, request, *args, **kwargs):

        if not request.method == 'GET':
            return CORSHttpResponse(status=403)

        response = None

        if 'id' in request.GET:
            response = Tag.objects.filter(pk__in=request.GET.getlist('id')).distinct()
        else:
            response = Tag.objects.all()

        if 'username' in request.GET:
            try:
                subscribed = [s.pk for s in OurUser.objects.get(username=request.GET['username']).subscriptions.all()]
            except ObjectDoesNotExist:
                CORSHttpResponse(status=400)
            response = response.filter(~Q(pk__in=subscribed))


        if response is None:
            return CORSHttpResponse(status=400)

        
        serialized_response = serializers.serialize('json', response)
        return CORSHttpResponse(status=200, content=serialized_response, content_type="application/json")
