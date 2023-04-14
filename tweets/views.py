from django.http import HttpResponse, Http404, JsonResponse
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Tweet
from .form import TweetForm
from django.utils.http import url_has_allowed_host_and_scheme


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)


def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    print('post data is: ', request.POST)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({}, status=201)
        else:
            print('is not ajax')
        if next_url is not None and url_has_allowed_host_and_scheme(allowed_hosts=settings.ALLOWED_HOSTS, url=next_url):
            return redirect(next_url)
        form = TweetForm()
    return render(request, 'components/forms.html', context={"form": form})


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [x.serialize() for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.text
    except:
        data['message'] = "Not Found"
        status = 404

    return JsonResponse(data, status=status)
