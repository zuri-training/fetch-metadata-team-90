from asyncore import write
from django.db import models
from django.db.models.signals import pre_save, post_save
from PIL import Image
from PIL.ExifTags import TAGS
from django.core.files.storage import FileSystemStorage
import filetype
import pathlib
import cv2
import pytesseract
import random
import pikepdf
from PyPDF2 import PdfFileReader
from .datetime import transform_date
from pymediainfo import MediaInfo
# Create your models here.
class FileQuerySet(models.QuerySet):
    def search(self, query):
        if query is None or query == "":
            return self.none()
        return self.filter(file_name__icontains = query)

class FileManagers(models.Manager):
    def get_queryset(self):
        return FileQuerySet(self.model, using=self._db)
    
    def search(self, query):
        return self.get_queryset().search(query=query)




class FileContent(models.Model):
    file = models.FileField(upload_to='uploaded_files/')
    file_name = models.CharField(max_length=280, null=True, blank=True)
    extracted_metaData = models.TextField(null=True, blank=True)
    extracted_text = models.TextField(null = True, blank=True)

    objects = FileManagers()


BASE_DIR = pathlib.Path(__file__).parent

def extracted_metadata(instance, save=False):
    filename = (instance.file).name
    
    f = FileSystemStorage()
    file_path = f.path(filename)
    kind = filetype.guess(str(file_path))
    possible_options = ['jpg', 'png', 'jpeg', 'gif']
    result = {}
    if kind.extension in possible_options:
        i = Image.open(instance.file)
        info = i.getexif() 
        for tag_id in info:
            tag = TAGS.get(tag_id, tag_id)
            value = info.get(tag_id)
            result[tag] = value
        if result == {} or result is None or result == '':
            result = {
                'Image-Height': i.height,
                'Image-Width': i.width,
                'Image-Mode': i.mode,
                'Image-Size': i.size,
                'Image-Type': kind.extension
            }
        # return result
    if kind.extension == 'pdf':
        pdf = pikepdf.Pdf.open(file_path)
        docinfo = pdf.docinfo
        for key, value in docinfo.items():
            if str(value).startswith("D:"):
    # pdf datetime format, convert to python datetime
                value = transform_date(str(pdf.docinfo["/CreationDate"]))
                result[key] = value
            else:
                result[key] = value
            with open(file_path, 'rb') as f:
                p = PdfFileReader(f)
                extra_data = {
                    'file type': kind.extension,
                    'Number of pages': p.getNumPages(),
                    'file name': filename,
                }
                result.update(extra_data)
    if kind.extension == 'mp3' or kind.extension == 'mp4':
        media_info = MediaInfo.parse(file_path)
        result = media_info.to_data()

    return result
    

def file_name(instance):
    filename = (instance.file).name
    return filename

def extracted_text(instance):
    filename = (instance.file).name
    f = FileSystemStorage()
    file_path = f.path(filename)
    kind = filetype.guess(str(file_path))
    possible_options = ['jpg', 'png', 'jpeg', 'gif']
    result = ''
    if kind.extension in possible_options:
        image = cv2.imread(file_path)
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        random_int = random.randint(0, 1000)
        path = str(BASE_DIR/'images'/f'{random_int}.{kind.extension}')
        read_grayscale = cv2.imwrite(path, grayscale_image)
        write_grayimage = cv2.imread(path)
        threshold, im_bw = cv2.threshold(write_grayimage, 219, 240, cv2.THRESH_BINARY)
        i = cv2.imwrite(str(BASE_DIR/'images'/f'updated{random_int}.{kind.extension}'), im_bw)
        image = Image.open(str(BASE_DIR/'images'/f'updated{random_int}.{kind.extension}'))
       
        result = pytesseract.image_to_string(image)
    return result
   

def file_post_save(sender, instance, created, *args, **kwargs):
    if created:
        instance.extracted_metaData = extracted_metadata(instance, save=True)
        instance.file_name = file_name(instance)
        instance.extracted_text = extracted_text(instance)
        instance.save()
post_save.connect(file_post_save, sender=FileContent)        
    

    
