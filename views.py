# from django.http import HttpResponse
# from django.shortcuts import render
# from app.models import Users
# # , Posts, Chats, Message

# currentUser = "Ahan"

# def index (req) :
# 	if not currentUser :
# 		return render(req, 'login.html')
# 	# posts =  Posts.objects.all()
# 	posts = [{"postContent" : "Hi, please help me by clicking the help me button and save me life for this once", "postAuthor": "Ahan Ray", "postId" : "1"},
# 				{"postContent" : "Calling for help in the western region for supplying relif aid to the disaster struck areas", "postAuthor" : "Govt India", "postId" : "2"}]
# 	params = {"posts" : {"posts" : posts}, "username" : currentUser}
# 	return render(req, 'index.html', params)

# def makepost(req) :
# 	content = req.GET.get("postContent")
# 	postStatus = "false"
# 	# if content and content != "None" :
# 	# 	newPost = Posts(
# 	# 		postcontent = content,
# 	# 		postAuthor = currentUser
# 	# 	)
# 	# 	newPost.save()
# 	# 	postStatus = "true"

# 	params = {"name" : currentUser, "postContent" : content, "postStatus" : postStatus, "errorMessage" : ""}
# 	return render(req, 'post.html', params)

# def login(req) :
# 	res = Users.objects.get(username = "Ahan Ray", password = "passwornd")
# 	logStatus = "false"
# 	if(len(res) == 1) :
# 		logStatus = "true"
# 	params = {"username" : "ahan", "password" : "not a pasword", "loginStatus" : logStatus}
# 	return render(req, 'login.html', params)

# def	signup(req) :
# 	return render(req, 'signup.html')
