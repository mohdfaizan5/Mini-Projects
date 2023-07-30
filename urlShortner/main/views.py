from django.shortcuts import render
import uuid # to generate unique id

# Create your views here.

def index(request):
    print(request.method)
    if request.method == "POST":
        print("inside the post request")
        uid = uuid.uuid4()
        uid = str(uid)
        uid = uid[:5]
        print(uid)
        return render(request, "main/index.html", {
            "uuid": uid
        })
    else:
        # return render(request, "main/index.html")
        pass
#     print("GET request")
#     return render(request, "main/index.html")


# def shorten(request):
#     # if request.method == "POST":
#     if request.method == "POST":
#         print("inside the post request")
#         url = request.post['url']
#         print(url)
#         uid = uuid.uuid4()
#         uid = str(uid)
#         uid = uid[:5]
#         print(uid)
#         return render(request, "main/index.html", {
#             "uuid": uid
#         })


# def index(request):
#     if request.method == "POST":
#         print("inside the post request")
#         uid = uuid.uuid4()
#         uid = str(uid)
#         uid = uid[:5]
#         print(uid)
#         return render(request, "main/index.html", {
#             "uuid": uid
#         })
#     else:
#         # return render(request, "main/index.html")
#         pass
    
#     return render(request, "main/index.html")

