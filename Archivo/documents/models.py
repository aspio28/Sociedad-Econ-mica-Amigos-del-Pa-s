from django.db import models
from django.urls import reverse
from xml.etree import ElementTree as ET

class Document(models.Model):
    xml_data = models.TextField()
    
    def __str__(self):
        root = ET.fromstring(self.xml_data)
        root_name = root[0].text
        return root_name