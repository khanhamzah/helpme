from django.http import HttpResponse
from django.shortcuts import render
from .models import User, Posts, Message
import json
# , Chats, Message

def index (req) :
	userId = req.COOKIES.get("id")
	try:
		userDetails = User.objects.get(id = userId)
	except:
		return render(req,'login.html')
	
	posts = []
	postsQueried =  list(Posts.objects.all())[::-1]
	for post in postsQueried :
		posts.append({"postContent" : post.postContent, "postAuthor" : post.postAuthor.username, "postId" : post.id})

	params = {"posts" : {"posts" : posts}, "username" : userDetails.username or "unavailable"}
	return render(req, 'index.html', params)

def makepost(req) :
	userId = req.COOKIES.get("id")
	try:
		userDetails = User.objects.get(id = userId)
	except:
		return render(req,'login.html')

	errorMessage = ""
	postStatus = "false"
	content = req.POST.get("postContent") or ""
	if content and content != "None" :
		newPost = Posts(
			postContent = content,
			postAuthor = userDetails
		)
		try :
			newPost.save()
			postStatus = "true"
		except :
			errorMessage = "! could not save post ¡"

	params = {"postContent" : content, "postStatus" : postStatus, "errorMessage" : errorMessage, "username" : userDetails.username or "undefined"}
	return render(req, 'post.html', params)

def login(req) :
	loginStatus = False
	username = ""
	password = ""
	if req.method == 'POST' :
		username = req.POST.get("username")
		password = req.POST.get("password")

	if username != "" and password != "" :
		try :
			ret = User.objects.get(username = username, password = password)
			loginStatus = True
			username = ret.id
		except:
			loginStatus = False
	params = {"username" : username, "password" : password, "loginStatus" : loginStatus}
	return render(req, 'login.html', params)

def	signup(req) :
	errorMessage = ""
	status = "false"
	newUsername = req.POST.get("new-username")
	newPassword = req.POST.get("new-password")
	if newUsername and newPassword :
		try :
			newUser = User(
				username = newUsername,
				password = newPassword
			)
			newUser.save()
			newUsername = newUser.id
			status = "true"
		except :
			errorMessage = "username taken"
	elif not newUsername and not newPassword :
		pass
	else :
		errorMessage = "empty"
			
	return render(req, 'signup.html', {"error" : errorMessage, "status" : status, "username" : newUsername or "", "password" : newPassword or ""})

def profileShow(req, userId) :
	userDetails = {}
	posts = []
	try :
		userDetails = User.objects.get(id = userId)
		try :
			postList = Posts.objects.filter(postAuthor = userDetails)
			for post in postList :
				posts.append({"postContent" : post.postContent, "postAuthor" : post.postAuthor.username, "postId" : post.id})
		except :
			posts = []
	except:
		userDetails = {"username" : "user not available"}

	return render(req, 'profile.html',{"username" : userDetails.username ,"profileName" : userDetails.username, "profileContent" : {"posts" : posts}})

def messaging(req, postId):
	userId = req.COOKIES.get("id")
	userDetails = {}
	userMessages = []
	try:
		userDetails = User.objects.get(id = userId)
	except:
		return render(req,'login.html')
	
	try:
		userMessages = Message.objects.filter(postId = Posts.objects.get(id = postId))
	except:
		userMessages = []
	msgs = [{"message":x.message, "userId":x.userId.username} for x in userMessages]
	return render(req, "chat.html", { "username": userDetails.username, "messages": msgs, "profileName" : userDetails.username, "postId" : postId, "post": Posts.objects.get(id = postId) })

def addMessage(req, postId, message):

	try:
		newMessagage = Message(
			postId = Posts.objects.get(id = postId),
			userId = User.objects.get(id = req.COOKIES.get("id")),
			message = message
		)
		newMessagage.save()
	except:
		return HttpResponse("False")

	return HttpResponse(json.dumps({"userId":newMessagage.userId.username,"message":newMessagage.message}))