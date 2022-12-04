from django.shortcuts import render
from .models import Document
from documents.forms import Form_Document,FormSearch
from documents.models import Document
from django.http import HttpResponse

def New_Document(request):

    formulario = Form_Document()

    if(request.method == "POST"):
        formulario = Form_Document(data=request.POST)

        if(formulario.is_valid()):
            title = request.POST.get("title")
            author = request.POST.get("author")
            year = request.POST.get("year")
            document_type = request.POST.get("document_type")
            body = request.POST.get("body")

            doc = Document.objects.create(title= title , author= author,year= year, document_type = document_type, body= body)

            return render(request, "base/index.html",{"estado": "valido"})

    return render(request, "base/document.html",{"form":formulario})

def Search(request):
    if(request.method == "POST"):
        searching=FormSearch(request.POST)
        if(searching.is_valid()):
            info = searching.cleaned_data
            documents = []
            query={}
            title = info['title']
            author = info['author']
            year = info['year']
            document_type = info['document_type']
            
            if(title != ''):
                documents.append(Document.objects.filter(title__icontains=title))
                query['Título'] = title
            
            if(author != ''):
                documents.append(Document.objects.filter(author__icontains=author))
                query['Autor'] = author
            
            if(year != None):
                documents.append(Document.objects.filter(year__icontains=year))
                query['Año en que fue escrito'] = year
            
            if(document_type != ''):
                documents.append(Document.objects.filter(document_type=document_type))
                query['Tipo de documento'] = document_type
            return render(request,'base/doc_search.html',{"documents":documents,"query":query})
    else:
        searching = FormSearch()
        return render(request, "base/search.html", {"form": searching}) 