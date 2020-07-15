from django.shortcuts import render, redirect
import facebook
import requests
from .forms import PostForm
from .models import *
from django.conf import settings
import os
# Create your views here.

app_id = '688986821665698'
app_secret = '0167c9a12032fef90e4ba874afd3ea82'
user_short_token = 'EAAJyoT7Co6IBAFTcAn7T90JWNm21fRzvEuJLIUfqPAOKTT9LfFQwSCZAlkr7Ta2znIzX9VQStZBuPZBbTo4ZCX9xO7Pr5aTZCUXwamdNBFLFrkx8aTaVxMPh0797D2Ljd9QY2ftKFiLqJHD1RPvwlgjwVS0QekaE4GCne9304kR9Nygj0G20PrtZAsaWSL80LLDKU8AtZCZBYAiVhoEfmChn'
token = 'EAAJyoT7Co6IBAFwb1yEDAQhpxKFAuHGAZBzVCN6HGYQamW7885LcgSKYmJZAHVhJB1ha1ZBdMffj9wJioIhNEEcD6c0BE95f1aQz6CPubIZBLzAiU2JVaN6MjgSLLpEskkgVZCr8EVsJAgSCCIZAdNVh58oViHfZANmezaAmidbuZBF8JhICQQKUMwJKSICIo7IZD'
def testPage(request):


    # access_token_url = "https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id={}&client_secret={}&fb_exchange_token={}".format(app_id, app_secret, user_short_token)
    # r = requests.get(access_token_url)

    # access_token_info = r.json()
    # user_long_token = access_token_info['access_token']
    # print(user_long_token)
    
    graph = facebook.GraphAPI(access_token=token)





    # token = graph.get_access_token_from_code(app_id=app_id, app_secret=app_secret,)
    # print(token)
    # graph = facebook.GraphAPI(access_token=token)

    # data = graph.put_object(parent_object='me',connection_name='feed',message='Hello.... This is my test for fb pages.')
    graph.put_object(parent_object='103759348081459_111610630629664', connection_name='comments',
                  message='First!')
    # print(data)
    # comments = graph.get_connections(id='103917968065597_103922051398522', connection_name='comments')
    # print(comments)
    # friends = graph.get_connections(id='me', connection_name='friends')
    # print('friends')
    #comment
    # comments = graph.get_connections(id='103759348081459_103917968065597', connection_name='comments')
    # reply = graph.put_comment(comments['data'][0]['id'],'okay')
    # print(comments['data'][0]['id'])
    
    return redirect('/')


def social_index(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            graph = facebook.GraphAPI(access_token=token)
            message = form.cleaned_data['message']
            if form.cleaned_data['image'] != None:
                post =form.save(commit=False)
                post.created_by = request.user
                post.save()
                post_file = PostFiles()
                post_file.file= form.cleaned_data['image']
                post_file.post = post
                post_file.save()
                post = Post.objects.get(id=post.id)
                response = graph.put_photo(image=open( os.path.join(settings.BASE_DIR, post.postfiles.file.path), 'rb'),
                message=message)
                update_post = Post.objects.get(id=post.id)
                update_post.post_id = response['post_id']
                update_post.save()

            else:
                response = graph.put_object(parent_object='me',connection_name='feed',message=message)
                post =form.save(commit=False)
                post.created_by = request.user
                post.post_id =  response['id']
                post.save()
            redirect('social:social_index')
    context = {
        'title':'Post',
        'posts': Post.objects.all(),
    }
    return render(request,'social/index.html',context)