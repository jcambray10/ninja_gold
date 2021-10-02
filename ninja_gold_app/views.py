from django.shortcuts import render, redirect
from datetime import datetime
from pytz import timezone
import random, pytz

def ninja_gold(request):
    if 'gold' not in request.session or 'activities' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []

    context = {
        "activties":request.session['activities']
    }
    return render(request, "index.html", context)

def process_money(request):
        if request.method == 'POST':
            myGold = request.session['gold']
            activities = request.session['activities']
            location = request.POST['location']
            if location == 'farm':
                goldthisturn = round(random.random() * 10 + 10)
            elif location == 'cave':
                goldthisturn = round(random.random() * 5 + 10)
            elif location == 'house':
                goldthisturn = round(random.random() * 3 + 2)
            else:
                winOrLose = round(random.random())
                if winOrLose == 1:
                    goldthisturn = round(random.random() * 50)
                else:
                    goldthisturn = (round(random.random() * 50) * -1)
                
            date_format='%m/%d/%Y %H:%M:%S %Z'
            date = datetime.now(tz=pytz.utc)
            date = date.astimezone(timezone('US/Pacific'))
            myTime = date.strftime(date_format)

            myGold += goldthisturn
            request.session['gold'] = myGold
                    
            if goldthisturn >= 0:
                str = f"Earned {goldthisturn} from the {location}! Hooray!! {myTime}"
            else:
                goldthisturn *= -1
                str = f"Lost {goldthisturn} from the {location}! Sad!! {myTime}"

            activities.append(str)
            request.session['activities'] = activities

                
        return redirect("/")


# Create your views here.
