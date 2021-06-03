# GanMoodle

GanMoodle is a web app designed for kindergarten teachers,parents and students <br>
that helps keep education flow and connection for time of lockdowns.

## insructions for installing:

1. install latest version of Python   
2. open cmd/powershell/terminal :
    1. cd to desired folder
    2. git clone
    3. install virtual environment - `pip insatll virtualenv`
3. initiate virtual environmen `virtualenv <name>`
4. pip install requierment.txt:
   ```  
     asgiref==3.3.4
     Django==3.1.7
     django-widget-tweaks==1.4.8
     Pillow==8.2.0
     pytz==2021.1
     sqlparse==0.4.1
     coverage==5.5
     pylint==2.8.3 
     ```
 5. activate virtual environment by navigating to `.\<virtualenv_name>\Scripts\Activate`
 6. run the server by navigating to the projects folder and excuting the command: `python manage.py runserver`
 7. open `localhost:8000` on browser.
