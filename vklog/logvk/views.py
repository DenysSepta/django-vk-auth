from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from social_django.models import UserSocialAuth
import requests





import vk
import json


def friends_out(request):
    try:
        user_id = request.user.social_auth.get(provider='vk-oauth2').uid
        token = '48635a2d48635a2d48635a2de748082d244486348635a2d157ff2e699748d184a5cfa92'
        link = 'https://api.vk.com/method/{}?user_id={}&v=5.52&access_token=' + token
        res = requests.get(link.format("users.get", user_id)).json()
        ids_js = requests.get(link.format("friends.get", user_id)).json()
        user_name = res["response"][0]["first_name"]+" "+ res["response"][0]["last_name"]
        friends = []
        ids = []
        for x in ids_js["response"]["items"]:
            ids.append(x)
        for id in  ids :
            friends_res = requests.get(link.format("users.get", id)).json()
            friend_name = friends_res["response"][0]["first_name"]+" "+friends_res["response"][0]["last_name"]
            friends.append(friend_name)
            if len(friends) == 5:
                break
        context = {'user': user_name, 'friends' : friends}
        return render(request,'logvk/profile.html' , context)
    except:
        return render(request, "logvk/loginvk.html")







def index(request):
    return render(request, 'logvk/homePage.html')
