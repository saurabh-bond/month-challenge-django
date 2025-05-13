from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
  "january": "Wake up before 6:30 AM every day to build a powerful morning routine.",
  "february": "Do 30 minutes of physical activity daily walk, yoga, or workout.",
  "march": "Declutter one part of your home or digital space each day.",
  "april": "Learn something new for 15 minutes daily language, skill, or trivia.",
  "may": "No sugar month avoid sweets, soft drinks, and processed sugar.",
  "june": "Read 20 pages of a book every day.",
  "july": "30-day gratitude challenge write one thing you're grateful for each day.",
  "august": "Digital detox after 8 PM no phone, social media, or screens.",
  "september": "Try a new hobby or creative activity once a week (e.g., painting, cooking).",
  "october": "Walk 10,000 steps every day track your movement!",
  "november": "Write one journal entry per day reflecting on your thoughts or progress.",
  "december": None
}


# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months): 
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        raise Http404()
    
    