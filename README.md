# **proj-fetch_metadata**

## **Description**

This is a platform that fetches and extracts metadata from files uploaded by users. Unauthenticated users can visit the platform and get the full information of what the website entails, only verified and authenticated users who are logged in can get full access to upload their files and extract metadata.

## **Contribution Guidelines**
### Follow these steps to begin your contribution

* Fork this repository
* Clone the repository to your local machine using git clone https://github.com/zuri-training/fetch-metadata-team-90.git
* Open cloned repository in your code editor
### **For Backend:**
### Requirement 
- install exiftool on your pc https://exiftool.org/
* Linux Users
  * sudo apt install libimage-exiftool-perl
* Windows USers
* Create a virtual environment
  * cd into your virtual environment
* activate your virtual enviroment:
  * ./scripts/activate for windows users
  * ./bin/activate for mac-os users
* cd fetch-metadata-team-90
* On your terminal run:
  * pip install -r requirements.txt
  * python3 manage.py runserver
* Create a superuser:
  * python manage.py createsuperuser
* Add your contributions/make changes
* Commit with a descriptive message and push
* Create a pull request
### **For Frontend:**
* Find the folder named "Frontend" and open it
* Find or create new file with the name of the page you're assigned to, e.g login.html and login.css
* Add your code/make your changes
* Commit with a descriptive message and push
* Create a pull request

### **For The DevOps Production**
* install exiftoll
 * sudo apt install libimage-exiftool-perl
* pip3 install -r requirement.txt

* create a super user
   * email: zurimetlab@gmail.com
   * username: metlab
   * password: metlab123

* Update the settings.py

   



