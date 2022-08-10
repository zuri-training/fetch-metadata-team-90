Made Research and provided a solution on how we can extract text from images using pytessarct, a python machine learning library that performs Optical Character Recognition (OCR) and works based on Tesseract, a software that helps in the extraction of text from images.
Was able to extract metadata from some files such as: images, pdfs file, mp3 and mp4 files using some python libraries such as pillow, pikepdf and pymediainfo. I was also able to implement the extraction of metadata in Django, using Django signals. 
https://github.com/zuri-training/fetch-metadata-team-90/tree/main/metadata_extraction

https://github.com/zuri-training/fetch-metadata-team-90/blob/main/metadata_extraction/models.py

I also implemented the finished design from the Frontend codes of our home page into Django templates.https://github.com/zuri-training/fetch-metadata-team-90/blob/main/templates/index.html 

However, someone else, was able to come up with a more better solution on how we can extract metadata from files using a software called exiftool and a python library that works hand in hand with the exiftool know as py-exiftool.So we decided to go with that, this is because my solution tends to consume more system storage, because we will have to be using a lot of dependencies for our project which may on the other hand crash with other teams that we will be sharing server with.
