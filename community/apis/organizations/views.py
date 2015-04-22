from django.views.generic import View
from apis.CORSHttp import CORSHttpResponse


class CreateOrganization(View):

    def dispatch(self, request, *args, **kwargs):

        if not request.method == 'POST':
            return CORSHttpResponse(status=403)

        return CORSHttpResponse(status=501)

class GetOrganizations(View):

    def dispatch(self, request, *args, **kwargs):

        if not request.method == 'GET':
            return CORSHttpResponse(status=403)

        return CORSHttpResponse(status=501)

class AddAdmin(View):

    def dispatch(self, request, *args, **kwargs):

        if not request.method == 'POST':
            return CORSHttpResponse(status=403)

        return CORSHttpResponse(status=501)

class GetAdmins(View):

    def dispatch(self, request, *args, **kwargs):

        if not request.method == 'GET':
            return CORSHttpResponse(status=403)

        return CORSHttpResponse(status=501)