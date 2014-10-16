Django on App Engine Example
============================

Run Django projects on Google App Engine Platform. This is a base project developed for using [Django non-rel](http://django-nonrel.org) on Google App Engine.

Introduction
------------
I started using python on Google App Engine but then I need something more powerful than the great webapp2 framework.
Mainly something like the Django admin so after a research finished using with the great iniciative of Django non-rel.

Although you can use Django on App Engine third-party Django applications that use the Django data modeling
interface—most notably Django's Admin application—may not work with App Engine directly. [source](https://cloud.google.com/appengine/docs/python/tools/libraries27#django)

Features
--------
* Administrable global configurations with [django-solo](https://github.com/lazybird/django-solo)
* Translation ready. Template and cacheable JS translation. Language selector in the index template.
* Translatable fields in models with [Model translation](https://django-modeltranslation.readthedocs.org/)
* WYSIWYG editor for admin with [summernote](https://github.com/lqez/django-summernote)
* [Cache enabled](https://docs.djangoproject.com/en/dev/topics/cache/) by default. Add @never_cache decorator to the views that must not be cached
* Base template with [Initializr](http://www.initializr.com/).

Installation
------------
* Download and install the [App Engine SDK for python](https://developers.google.com/appengine/downloads)
* Clone this repo: ```git clone https://github.com/leopittelli/Django-Google-App-Engine-Base-Project.git```
* Run the app as usual, with the App Engine Launcher or in the command line: ```dev_appserver.py myapp```

Usage
-----
You can start in the folder main. It intends to be the main django app in your project. You can add your models, views and so on.

Third-party libraries
---------------------
As you can not install any app/library in App Engine, all the dependencies must be part of the source code.
Django non-rel and its dependencies are all added in the project. Also the applications described in features.

Deployment
----------
* Remember to run ```python manage.py collectstatic``` in the root of the project to collect all the staticfiles into the /static folder.
* Uncomment the static handler in the app.yaml file.
* Deploy as usual. I recommend the button of the App Engine Launcher.