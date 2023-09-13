from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question

# a view can do one of two things: return and HttpResponse object or raise an exception.
# the HttpResonse object contains the content of the page. no limits on what you can put in it.

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    print("running poll.views vote function")
    question = get_object_or_404(Question, pk=question_id)
    try:
        # get the value of the choice attribute of the request sent.
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form.
        return render(request, "polls:detail.html", {"question": question, "error_message": "You didn't select a choice.",})
    else:
        # if things go smoothly and there is no eeror
        selected_choice.votes += 1
        selected_choice.save()
        # always return and HttpResponse after processing a POST request. This prevents data from being posted twice if a user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))