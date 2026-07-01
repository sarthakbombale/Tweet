from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet
from .forms import TweetForm  # Make sure you have a form class in forms.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

# 1. Main Application Landing Page
def index(request):
    return render(request, 'index.html')

# 2. View All Tweets (The Feed Layout)
def tweet_list(request):
    # Fetch all tweets ordered by the most recent posting date
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})

# 3. Create a New Tweet
@login_required  # Protect this view so only logged-in users can tweet
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user  # Assign the current logged-in user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})

# 4. Edit an Existing Tweet
@login_required
def tweet_edit(request, tweet_id):
    # Fetch the tweet or return a 404 page if it doesn't exist
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})

# 5. Delete a Tweet
@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'object': tweet})


# Simple registration view using Django's UserCreationForm
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in after successful registration
            auth_login(request, user)
            return redirect('tweet_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
