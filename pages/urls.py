#\projroot\pages\urls.py
from django.urls import path
# import all views from the current package (. is shorthand")
from . import views

urlpatterns = [
    # Matches an empty string or "/" as Django auto removes /
    # views.index points to our index view
    
    #path('', views.index, name = 'index'),
    # The above path() was commented out to setup the following capturing
    # group
    # This is a special case for the home page because path() can't
    # capture an empty string.
    # When the user navigates to the site root, pagename is set to an 
    # empty string ''
    path('',views.index, {'pagename': ''}, name ='home'),
    # The following uncommented line is the capturing group
    # Everything in the < > brackets will be captured and sent to the view
    # as a parameter (pagename)
    # For example if the URL services/ is passed to this function, 
    # the index view is called and the string "services" is passed to 
    # the view as a parameter

    # str: is a path converter, which will convert the captured data into 
    # a particular type, int and slug are also path converters
    # path converters are str by default, but it's zen to be explicit
    path('<str:pagename>', views.index, name = 'index'),
]
