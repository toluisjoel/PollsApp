from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.views import generic
from polls.models import Choice, Question
from django.utils import timezone


class IndexView(generic.ListView):
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]


class DetailView(generic.DetailView):
    model = Question


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {'question': question, 'error_message': "Omo na error you dey chop , you didn't select a choice"}
        return render(request, 'polls/question_detail.html', context)
    else:
        selected_choice.vote = F('vote') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
