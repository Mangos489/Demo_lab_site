Just an open source LIMS will be editing this further to apply a license and other neccessary documentation such as start up.

You can run the project by installing the necessary packages listed within requirements.txt & installing the packages in package.json. 

Once youve done that cd into your main directory where running the command dir (if on windows idk wuts the equivalent on apple) will return something like this 

05/01/20XX  05:47 PM    <DIR>          .
05/02/20XX  11:54 AM    <DIR>          ..
05/10/20XX  05:42 PM                   .gitignore
05/10/20XX  05:55 PM    <DIR>          backend
05/08/20XX  01:57 PM                   docker-compose.yaml
04/28/20XX  11:33 AM    <DIR>          env
05/07/20XX  02:28 PM    <DIR>          frontend

Now youll need to activate your virtual env by running

>cmd
>>.\env\scripts\activate.bat

Now youre ready to start developing. If you have any issues starting up hmu through my socials and ive got you!

To start running the website:

In your terminal:

>cd into the backend and run
>>python manage.py runserver

Open a new terminal window and run:
>cd frontend 
>>npm run dev
