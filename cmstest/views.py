from django.http import HttpResponse
# Create your views here.
def testView (request):
	return HttpResponse("Hello, Tested")