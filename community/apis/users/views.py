from django.views.generic import View
from users.models import User
from django.core import serializers
from apis.CORSHttp import CORSHttpResponse


class GetUser(View):

    def dispatch(self, request, *args, **kwargs):

        if not request.method == 'PUT':
            return CORSHttpResponse(status=403)

        if request.PUT['username']:
            return CORSHttpResponse(status=501)

