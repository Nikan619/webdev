from django.shortcuts import render


from django.shortcuts import render

def index(request):

   return render(request,"base.html")

# Create your views here.

def book_search(request):
   search_text = request.GET.get("search","")
   return render(request,"search_result.html", {"search_text":search_text})


