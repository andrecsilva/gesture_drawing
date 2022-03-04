# What?

A webapp for gesture drawing sessions and organizing references using tags.

Right now it supports adding and tagging references, and organizing gesture drawing sessions.

Interface is barebones but functional for now .

# How to use?

Make sure you have django and all its needed dependencies somehow (e.g pip `pip install django`).

Initialize the database:
```
cd gesture_drawing
python manage.py makemigrations && python manage.py migrate
```
You can add existing references using a handy script included:
```
./add_references.py <path/to/your/references>
```

It adds a symbolic link to the `media` folder. Be aware that changes on your original folder may break the links to the references.


If you know what you are doing, deploy it, otherwise:
```
python manage.py runserver 0.0.0.0:8000
```

The app will available on your local network at `<your-ip>:8000`, where `<your-ip>` is the ip of the machine running the above command.

# Why?

Pretty useful not only to organizing your references using tags, but to quickly do gesture session drawings across several devices (e.g. tablets and pcs).
