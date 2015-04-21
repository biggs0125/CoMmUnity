from django.views.generic import View
from users.models import User
from tags.models import Tag
from django.core import serializers
from apis.CORSHttp import CORSHttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse


class GetUser(View):

    def dispatch(self, request, *args, **kwargs):

        if not request.method == 'POST':
            return CORSHttpResponse(status=403)

        if 'username' in request.POST:
            username = request.POST['username']
            user_obj, created = User.objects.get_or_create(username=username)

            json_response = JsonResponse({"new" : created})
            return CORSHttpResponse(status=200, content=json_response.content, content_type="application/json")


class AddSubscriptions(View):

    def dispatch(self, request, *args, **kwargs):

        if not request.method == 'POST':
            return CORSHttpResponse(status=403)

        self.username = request.POST['username']
        self.tags = request.POST.getlist('tag')

        for tag in self.tags:
            try:
                Tag.objects.get(name=tag)
            except ObjectDoesNotExist:
                return CORSHttpResponse(status=404)

        # TODO: IMPLEMENT THIS!!

        return CORSHttpResponse(status=501)


class GetSubscriptions(View):

    def dispatch(self, request, *args, **kwargs):

        if not request.method == 'GET':
            return CORSHttpResponse(status=403)

        return CORSHttpResponse(state=501)

        # TODO: IMPLEMENT THIS!!