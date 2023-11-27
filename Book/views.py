from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url= "/login_page/")
def home(request):
    #return HttpResponse("This is django")

    queryset = book_model.objects.all()
    context = {'books' : queryset}

    return render(request , "Book/index.html" , context = context)  

@login_required(login_url= "/login_page/")
def new_book(request):
    if request.method == "POST": 
        data = request.POST 

        dic = {
            'title' : data.get('title') ,
            'ISBN' : data.get('ISBN') ,
            'publication_date' : data.get('publication_date') ,
            'book_description' : data.get('book_description') ,
            'file' : request.FILES.get('file') ,
            'book_image' : request.FILES.get('book_image'),
            'uploaded_by' : request.user,
        }
        if dic['book_image'] == None :
            del dic['book_image']
        print(dic)

        book_model.objects.create(**dic) 

        return redirect('/new_book/')


    return render(request , "Book/new_book.html") 

def update_book(request , id):
    queryset = book_model.objects.get(id = id) 
    
    context = {'book':queryset} 
    if request.method == "POST" :
        print("try post updating" , id)
        data = request.POST
        dic = {
            'title' : data.get('title') ,
            'ISBN' : data.get('ISBN') ,
            #'publication_date' : data.get('publication_date') ,
            'book_description' : data.get('book_description') ,
            'file' : request.FILES.get('file') ,
            'book_image' : request.FILES.get('book_image'),
        }
        
        if dic['title'] != None :
            queryset.title = dic['title'] 
        if dic['ISBN'] != None :
            queryset.ISBN = dic['ISBN']  
        
        if dic['book_description'] != None :
            queryset.book_description = dic['book_description']
        if dic['file'] != None :
            queryset.file = dic['file'] 
        if dic['book_image'] != None :
            queryset.book_image = dic['book_image']   

        queryset.save()    

        try :
            aa = data.get('publication_date')
            print(aa)
            if aa != None :
                queryset.publication_date = aa
            queryset.save()    
        except : 
            pass

        return redirect(f"/book_detail/{id}")     



    return render(request , 'Book/update_book.html', context = context)


def delete_book(request , id):
    queryset = book_model.objects.get(id = id)

    queryset.delete()

    return redirect('/') 

def book_detail(request , id):
    queryset = book_model.objects.get(id = id) 
    print(queryset.user)
    context = {'book' : queryset}

    return render(request , "Book/book_detail.html", context = context) 
