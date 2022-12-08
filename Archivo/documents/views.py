from django.shortcuts import render
from .models import Document
from documents.forms import Form_Document,FormSearch
from xml.etree import ElementTree as ET

def New_Document(request):

    formulario = Form_Document()

    if(request.method == "POST"):
        formulario = Form_Document(request.POST,request.FILES)
    
        if(formulario.is_valid()):
            if 'xml_file' in request.FILES:
                xml_string = formulario.cleaned_data['xml_file'].read().decode('utf-8')
                
            else:
                title = request.POST.get("title")
                author = request.POST.get("author")
                year = request.POST.get("year")
                document_type = request.POST.get("document_type")
                body = request.POST.get("body")

                elements = ['titulo','autor','anho_en_que_fue_escrito',"tipo_de_documento",'cuerpo']
                atributes = [title,author,year,document_type,body]
                root = ET.Element("document")

                for element,atribute in zip(elements,atributes):
                    child = ET.SubElement(root, element)
                    child.text = atribute

                xml_string = ET.tostring(root,encoding="unicode")

            doc = Document.objects.create(xml_data = xml_string)
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
                documents.append(Document.objects.filter(xml_data__icontains=title))
                query['Título'] = title
            
            if(author != ''):
                documents.append(Document.objects.filter(xml_data__icontains=author))
                query['Autor'] = author
            
            if(year != None):
                documents.append(Document.objects.filter(xml_data__icontains=year))
                query['Año en que fue escrito'] = year
            
            if(document_type != ''):
                documents.append(Document.objects.filter(xml_data=document_type))
                query['Tipo de documento'] = document_type
            return render(request,'base/doc_search.html',{"documents":info_xml(documents),"query":query})
    else:
        searching = FormSearch()
        return render(request, "base/search.html", {"form": searching}) 
def info_xml(dic_xml):
    
    dic = {}
    for doc in dic_xml:
        for docu in doc:        
            root = ET.fromstring(docu.xml_data)
            for elem in root:
                root_element = elem.tag.replace('_',' ').title().replace('nh', 'ñ')
                root_text = elem.text
                dic[root_element] = root_text
    return dic