# blogantonio4

## Chapter 1: Building a Blog Application 1
- Installing Python
- Creating a Python virtual environment
    ```sh
    cd blogantonio4
    pipenv install
    pipenv shell
    ```

- Installing Django
    - Installing Django with pipenv
        ```sh
        pipenv install Django~=4.1.0
        ```
    - New features in Django
- Django overview
- Main framework components
- The Django architecture
- Creating your first project
    ```
    django-admin startproject mysite
    ```
    - Applying initial database migrations
        ```py
        cd mysite
        python manage.py migrate
        ```
    - Running the development server
        ```py
        python manage.py runserver

        //custom setting
        python manage.py runserver 127.0.0.1:8001 --settings=mysite.settings

        ```
    - Project settings
    - Projects and applications
    - Creating an application
        ```py
        
        ```
Creating the blog data models 12
    Creating the Post model • 13
    Adding datetime fields • 14
    Defining a default sort order • 15
    Adding a database index • 16
    Activating the application • 17
    Adding a status field • 17
    Adding a many-to-one relationship • 19
    Creating and applying migrations • 21
Creating an administration site for models 23
    Creating a superuser • 24
    The Django administration site • 24
    Adding models to the administration site • 25
    Customizing how models are displayed • 27
Working with QuerySets and managers 29
    Creating objects • 30
    Updating objects • 31
    Retrieving objects • 31
        Using the filter() method • 31
        Using exclude() • 32
        Using order_by() • 32
    Deleting objects • 32
    When QuerySets are evaluated • 32
    Creating model managers • 33
Building list and detail views 34
    Creating list and detail views • 34
    Using the get_object_or_404 shortcut • 35
    Adding URL patterns for your views • 36
Creating templates for your views 37
    Creating a base template • 38
    Creating the post list template • 39
    Accessing our application • 40
    Creating the post detail template • 41
The request/response cycle 42
Additional resources 43
Summary 44