# Rose Parade backend
This applications was build using:
- Django Rest Framework
- djangorestframework-simpleJWT
- MySQL Database

###The challenge
Christmas, 2021. Barely a year ago, Intel launched the most powerful quantic computer ever.
This computer gained self-awareness and the war between humans and machines started.
Nowadays, humanity can’t use the Internet and almost all the existing information is inaccessible for humans.

As a show of power, a squad of volunteers and sellers of flowers from the United States have started a clandestine network to organize the traditional Rose Parade.
To achieve this, they will need to store the information about the carriages and the bands that are going to participate and what order will they follow.


###What does this API?
This api exposes the next functionalities:

- Public:
    * POST api/participants/join: Endpoint to register a new participant of the Rose Parade Fest
- Protected (user authentication needed)
    * GET api/participants: Endpoint to get the list of registered participants
    

##How to set up the project?
If you will test locally, you need a MySQL database with the following specs:

        'NAME': 'rose_parade_db',
        'USER': 'YOUR_USER',
        'PASSWORD': 'YOUR_PASS',
        'HOST': '127.0.0.1',
        'PORT': '3306',

Be sure to update YOUR_USER and YOUR_PASS on /rose_parade_backend/settings.py

Once you clone this repo, I highly recommend to use a virtual env to run this app.
You can create one installing virtualenv.

1.- On the folder of your preference execute
        `virtualenv create {EnvName}`
        
2.- Then `cd {EnvName}/bin` and execute `activate`. You must see the env name at
the beginning of your command line.

3.- Go to the directory of this repo and on root execute `pip install -r requirements.txt`
That will install all the necessary dependencies for this project.

4.- We are ready to create our tables on our DB, execute `python manage.py makemigrations participants`

5.- To apply the migration execute `python manage.py migrate participants`

6.- Some endpoints need authentication, to achieve that, we will create a super user with: `python manage.py createsuperuser`.
This will require you a username, email and password.

7.- We are ready to use the project. On the postman folder, you will found a collection to use the 
available requests. First of all execute `Obtain JWT token` request providing your username and password
