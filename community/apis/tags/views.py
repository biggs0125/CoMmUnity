from django.views.generic import View
from tags.models import Tag
from django.core import serializers
from apis.CORSHttp import CORSHttpResponse

class GetTag(View):

    def dispatch(self, request, *args, **kwargs):

        if not request.method == 'GET':
            return CORSHttpResponse(status=403)

        response = None

        if 'id' in request.GET:
            response = Tag.objects.filter(pk__in=request.GET.getlist('id')).distinct()

        if response is None:
            return CORSHttpResponse(status=400)

        serialized_response = serializers.serialize("json", response)
        return CORSHttpResponse(status=200, content=serialized_response, content_type="application/json")