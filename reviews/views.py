from django.shortcuts import render

from django.http import HttpResponse

from .models import Book,Review

from .utils import average_rating

from django.shortcuts import render


def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for
                                          review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0


        book_list.append({'book':book,'book_rating':book_rating,'number_of_reviews':number_of_reviews})
        context = {'book_list': book_list}
        return render(request,'reviews/books_list.html',context)











# def welcome_view(request):
#   return render(request,'base.html')
# def index(request):
#
#    return render(request,"base.html")
#
# # Create your views here.
#
# def book_search(request):
#    search_text = request.GET.get("search","")
#    return render(request,"search_result.html", {"search_text":search_text})


