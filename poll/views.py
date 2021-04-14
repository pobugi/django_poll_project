from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .forms import CreatePollform
from .models import Poll


def home(request):

    polls = Poll.objects.all()

    context = {'polls': polls}
    return render(request, 'poll/home.html', context)


def create(request):

    if request.method == 'POST':
        form = CreatePollform(request.POST)
        if form.is_valid():
            form.date_added = datetime.datetime.utcnow()
            form.save()
            return redirect('home')
    else:
        form = CreatePollform()

    context = {'form': form}
    return render(request, 'poll/create.html', context)


def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_1_count += 1
        elif selected_option == 'option2':
            poll.option_2_count += 1
        elif selected_option == 'option3':
            poll.option_3_count += 1
        else:
            return HttpResponse(400, 'Invalid form!')

        poll.save()
        return redirect('results', poll.id)

    context = {'poll': poll}
    return render(request, 'poll/vote.html', context)


def results(request, poll_id):

    poll = Poll.objects.get(pk=poll_id)
    context = {'poll': poll}
    return render(request, 'poll/results.html', context)


def delete(request, poll_id):

    poll = Poll.objects.get(pk=poll_id)
    poll.delete()
    return redirect('home')


def edit(request, poll_id):

    poll = Poll.objects.get(pk=poll_id)
    if request.method == 'POST':

        question = request.POST['question']
        option1 = request.POST['option1']
        option2 = request.POST['option2']
        option3 = request.POST['option3']

        poll.question = question
        poll.option_1 = option1
        poll.option_2 = option2
        poll.option_3 = option3
        poll.save()
        return redirect('home')

    context = {'poll': poll}
    return render(request, 'poll/edit.html', context)
