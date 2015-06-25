# thinkster-django-angular-boilerplate

## Installation

*NOTE: Requires [virtualenv](http://virtualenv.readthedocs.org/en/latest/),
[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) and
[Node.js](http://nodejs.org/).*

* Fork this repository.
* `$ mkproject thinkster-djangular`
* `$ git clone git@github.com:<your username>/thinkster-django-angular-boilerplate.git ./`
* ~~`$ mkvirtualenv thinkster-djangular`~~
* ~~`$ cd thinkster-django-angular-boilerplate/`~~
* `$ pip install -r requirements.txt`
* ~~`$ npm install -g bower`~~
* `$ sudo npm install -g bower`
* `$ npm install`
* `$ bower install`
* `$ python manage.py migrate`
* `$ python manage.py runserver`

## Creating an Angular frontend interface to a DRF API endpoint

*EXAMPLE ENDPOINT: localhost:8000/api/v1/accounts/*

* Enable HTML5 routing for AngularJS (get rid of ugly hash routing)
    * Create a config.js for the root module (eg. static/javascripts/thinkster.config.js)
    * Add the config as a depencency in the root module (eg. static/javascripts/thinkster.js)
* Configure AngularJS CSRF settings to harmonize with Django cookie and headers
    * xsrfHeaderName = 'X-CSRFToken'(eg. static/javascripts/thinkster.js)
    * xsrfCookieName = 'csrftoken' (eg. static/javascripts/thinkster.js)
* Define the service (eg. static/javascripts/authentication/services/authentication.service.js)
    * Create the factory (eg. Authentication)
    * Add methods (eg. register, which corresponds to Django Account.create ) 
* Create the user interface
    * Create an Angular template for the partial (eg. static/templates/authentication/register.html)
    * Create an Angular controller for the module (eg. static/javascripts/authentication/controllers/register.controller.js)
    * Create Angular routes for the module (eg. static/javascripts/thinkster.routes.js)
    * Define the module and it's dependencies (eg. static/javascripts/authentication/authentication.module.js)
    * Update the root module to include it's new dependencies (eg. static/javascripts/thinkster.js)
    * Include the new js files in the appropriate Django template (eg. templates/javascripts.html)

