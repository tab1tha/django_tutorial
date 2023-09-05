from django.http import HttpResponse

from .models import Question

# a view can do one of two things: return and HttpResponse object or raise and exception.
# the HttpResonse object contains the content of the page. no limits on what you can put in it.

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ",".join([question.question_text for question in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)