from django.shortcuts import render
#from django.http import HttpResponse

# Import the Page model into the view
from . models import Page

# When Django receives a request from a browser, it find the 
# right view, then the view returns a response to the browser

# Add the pagename parameter to the definition of the index view
# The string captured by the URL dispatcher will be assigned to
# pagename when the view loads
def index(request, pagename):
    # render automatically creates a shortcut for communicating with the browser
    # to load a template Django must load the template, then
    # create a context and pass it to the browser, then 
    # return an HttpResponse, render does all this for us

    # Django removes prepending /'s, so we need to add one
    # otherwise the URL links in our template will be relative to
    # the current page and not to the root
    pagename = '/' + pagename
    # The pg object will contain the page requested by the URL
    pg = Page.objects.get(permalink=pagename)
    # We are using our pg to populate the dictionary with items to 
    # pass to the template, in Django this dict is called the context
    # The context variables will be used by the template to render dynamic
    # content to the browser
    context = {
    	'title': pg.title,
    	'content': pg.bodytext,
    	'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }
    # Assert False is for testing the view. This triggers the error Page
    # We can see if the view is passing the right information back to
    # the template
    # Click on Local Vars on the error page to see the context dict
    #assert False

    # render() requires a request object, the name of the template
    # and the context to be passed into the template. Django will then
    # compile the webpage from the information provided and return a 
    # fully rendered HTML page to the browser (HttpResponse)
    return render(request, 'pages/page.html', context)
# Create your views here.
