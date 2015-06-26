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
* Create/edit layout template for the navbar register controll (eg. static/templates/layout/navbar.html) 

*SAME THING FOR POSTS: localhost:/api/v1/posts/ and '/api/v1/accounts/' + username + '/posts/'*

* static/javascripts/posts/posts.module.js (define module)
* static/javascripts/thinkster.js (add module as a dependency)
* templates/javascripts.html (add module script tag to django template)
* static/javascripts/posts/services/posts.service.js (define the service ie. create a factory)
* templates/javascripts.html (add service script tag to django template)
* static/templates/layout/index.html (add/modify layout template. Example employs a directive, posts)
    * The posts interface employs a snackbar utility for communicating the status of post actions:
    * static/javascripts/utils/utils.module.js (the module)
    * static/javascripts/utils/services/snackbar.service.js (the service)
    * static/javascripts/thinkster.js (add the utis module as a dependency)
* templates/javascripts.html (add utils and the snackbar service script tag to django template)
* static/javascripts/layout/controllers/index.controller.js (layout controller for the index page)
* static/javascripts/thinkster.routes.js (append the route for the index)
* static/javascripts/posts/directives/posts.directive.js (define the directive, post, used in the template)
* templates/javascripts.html (add the directives script tag to the django template)
* static/javascripts/posts/controllers/posts.controller.js (controller for the posts directive -- lots of good examples of formatting and layout methods here)
* templates/javascripts.html (Add the controller js tag)
* static/templates/posts/posts.html (template for the posts directive -- ng-cloak masks fouc, neat!)
* static/javascripts/posts/directives/post.directive.js (single post directive "post")
* static/templates/posts/post.html (single post directive template)
* static/stylesheets/styles.css (a couple of css declarations for post elements)



