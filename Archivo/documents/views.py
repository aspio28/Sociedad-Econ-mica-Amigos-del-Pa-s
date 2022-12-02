from django.shortcuts import render
from .models import Document
from documents.forms import Form_Document

def New_Document(request):

    formulario = Form_Document()

    if(request.method == "POST"):
        formulario = Form_Document(data=request.POST)

        if(formulario.is_valid()):
            info = formulario.cleaned_data
            title = request.POST.get("title")
            author = request.POST.get("author")
            body = request.POST.get("body")

            doc = Document.objects.create(title= title , author= author, body= body)

            return render(request, "base/index.html",{"estado": "valido"})

    return render(request, "base/document.html",{"form":formulario})