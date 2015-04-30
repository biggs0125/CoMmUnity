from django.views.generic import View
from apis.CORSHttp import CORSHttpResponse
from organizations.models import Organization
from tags.models import Tag
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from users.models import OurUser
from slugify import slugify


class CreateOrganization(View):

    def dispatch(self, request, *args, **kwargs):

        if not request.method == 'POST':
            return CORSHttpResponse(status=403)

        self.name = request.POST['name']
        self.admins = request.POST.getlist('admins')
        self.tagname = slugify(self.name, separator="_")
        Tag.objects.get_or_create(name=self.tagname)
        admin_objects = []
        try:
            for admin_name in self.admins:
                admin, created = OurUser.objects.get_or_create(username=admin_name)
                admin_objects.append(admin)
        except ObjectDoesNotExist:
            # One or more of the Users given does not exist, HTTP 400 - bad request
            return CORSHttpResponse(status=400)

        org, created = Organization.objects.get_or_create(name=self.name)
        if not created:
            # Organization with name already exists, HTTP 409 - conflict
            return CORSHttpResponse(status=409)

        org.admins = admin_objects
        org.save()

        return CORSHttpResponse(status=200)

class GetOrganizations(View):

    def dispatch(self, request, *args, **kwargs):

        if not request.method == 'GET':
            return CORSHttpResponse(status=403)

        if 'id' in request.GET:
            try:
                org = Organization.objects.filter(pk=request.GET['id'])
            except ObjectDoesNotExist:
                return CORSHttpResponse(status=400)
            serialized_response = serializers.serialize("json", org)
            return CORSHttpResponse(status=200, content=serialized_response, content_type="application/json")

        elif 'name' in request.GET:
            try:
                org = Organization.objects.filter(name=request.GET['name'])
            except ObjectDoesNotExist:
                return CORSHttpResponse(status=400)
            serialized_response = serializers.serialize("json", org)
            return CORSHttpResponse(status=200, content=serialized_response, content_type="application/json")

        elif 'admin' in request.GET:
            try:
                orgs = set()
                for org in Organization.objects.all():
                    for admin in org.admins.all():
                        if request.GET['admin'] == admin.username:
                            orgs.add(org)
                orgs_as_list = list(orgs)
            except ObjectDoesNotExist:
                return CORSHttpResponse(status=400)
            serialized_response = serializers.serialize("json", orgs_as_list)
            return CORSHttpResponse(status=200, content=serialized_response, content_type="application/json")

        else:
            orgs = Organization.objects.all()
            serialized_response = serializers.serialize("json", orgs)
            return CORSHttpResponse(status=200, content=serialized_response, content_type="application/json")

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
