from django.http import HttpResponse

class CORSHttpResponse(HttpResponse):
    def __init__(self, *args, **kwargs):
        #print kwargs
        super(CORSHttpResponse, self).__init__(*args, **kwargs)
        self['Access-Control-Allow-Origin'] = '*'

