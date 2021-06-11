from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
import datetime
from .models import job
from django.http import HttpResponse
from django.shortcuts import render
from GoogleNews import GoogleNews

def news(request):
    googlenews = GoogleNews()
    googlenews = GoogleNews(period='7d')
    googlenews.search('fifa')
    result=googlenews.result()
    a=[]
    b=[]
    c=[]
    d=[]
    for x in result:
        a.append(x['title'])
        b.append(x['date'])
        c.append(x['desc'])
        d.append(x['link'])
    mylist=zip(a,b,c,d)
    return render(request,'news.html',context ={"mylist":mylist})
def home(request):
    return render(request,'home.html')
def paypal(request):
    return render(request,'paypal.html')
def F1go(request):
    return render(request,'F1go.html')
def horsego(request):

    return render(request,'horsego.html')
def soccergo(request):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    plt.switch_backend('agg')
    import seaborn as sns
    from sklearn.model_selection import train_test_split
    from sklearn import linear_model
    from sklearn.metrics import r2_score
    from sklearn.linear_model import LogisticRegression
    from sklearn.linear_model import LinearRegression

    world_cup = pd.read_csv('C:/Users/NAGA HANUMA/Desktop/sp-pro-kit/data-files/WorldCupMatches (2).csv')

    df = pd.DataFrame(world_cup)

    conditions = [(df['Home Team Goals'] > df['Away Team Goals']), (df['Home Team Goals'] < df['Away Team Goals'])]
    Values = [df['Home Team Name'], df['Away Team Name']]
    df['Winner'] = np.select(conditions, Values)

    argentine = world_cup[((world_cup['Home Team Name'] == 'Argentina') | (world_cup['Away Team Name'] == 'Argentina'))]
    # mexico=world_cup[(world_cup['Home Team Name']=='Mexico')&(world_cup['Away Team Name']=='Argentina')]
    ad = pd.DataFrame(argentine)
    # me=pd.DataFrame(mexico)
    a = [[ad['Winner']]]

    labels = np.arange(len(ad))
    x = [np.array(argentine[['Home Team Goals']], dtype='<U10'), np.array(argentine[['Away Team Goals']], dtype='<U10')]

    ab = plt.bar(labels, list(map(float, x[0])), align='edge', width=-0.5)
    ab = plt.bar(labels, list(map(float, x[1])), align='edge', width=-0.5)
    plt.title("ratio of football")
    plt.savefig('media/footbal.png')
    plt.clf()

    teams = ['Uruguay', 'Russia', 'Saudi Arabia', 'Egypt', 'Spain', 'Portugal', 'Iran', 'Morocco', 'France', 'Denmark',
             'Peru', 'Australia', 'Croatia', 'Argentina', 'Nigeria', 'Iceland', 'Brazil', 'Switzerland', 'Serbia',
             'Costa Rica', 'Sweden', 'Mexico', 'Korea Republic', 'Germany', 'Belgium', 'England', 'Tunisia', 'Panama',
             'Colombia', 'Japan', 'Senegal', 'Poland']
    team1 = argentine[argentine['Home Team Name'].isin(teams)]
    team2 = argentine[argentine['Away Team Name'].isin(teams)]
    team = pd.concat((team1, team2))
    team = team.drop_duplicates()

    team_result = team.drop(
        ['Year', 'Datetime', 'Stage', 'Stadium', 'City', 'Win conditions', 'Attendance', 'Half-time Home Goals',
         'Half-time Away Goals', 'Referee', 'Assistant 1', 'Assistant 2', 'RoundID', 'MatchID', 'Home Team Initials',
         'Away Team Initials'], axis=1)

    final_result = pd.get_dummies(team_result, prefix=['Home Team Name', 'Away Team Name'],
                                  columns=['Home Team Name', 'Away Team Name'])

    X = np.asanyarray(final_result[['Home Team Goals']])
    y = np.asanyarray(final_result[['Away Team Goals']])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

    model = linear_model.LinearRegression()
    # model=LogisticRegression()
    model.fit(X_train, y_train)
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)

    y_pred = model.predict(X_test)
    plt.scatter(X_train, y_train)
    plt.plot(X_train, model.predict(X_train), color="red")
    plt.xlabel("Home Team Goals")
    plt.ylabel("Away Team Goals")
    plt.savefig('media/f1.png')


    return render(request,'soccergo.html')



def profile(request):
    return render(request,'profile.html')
def mail(request):
    return render(request,'mail.html')
def work(request):
    return render(request,'work.html')
def contact(request):
    return render(request,'contact.html')
def aboutus(request):
    return render(request,'aboutus.html')
def logout(request):
    auth.logout(request)

    return redirect('home')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("work/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')
        else:
            print('password not matched...')
            messages.info(request, 'password not matched.....')
            return redirect('register')
        return redirect('')
    else:
        return render(request, 'register.html')

def sendanemail(request):
    if request.method == "POST":
        to = request.POST.get('toemail')
        content = request.POST.get('content')
        send_mail(
            "testing",
            content,
            settings.EMAIL_HOST_USER,
            [to]

        )
        return render(
            request,
            'mail.html',
            {
                'title':'send an email'
            }
        )

    else:
        return render(
            request,
            'mail.html',
            {
                'title':'send an email'
            }
        )
    return HttpResponse('Mail successfully sent')



