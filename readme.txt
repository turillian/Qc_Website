
To activate the Django interactive shell:
$> python manage.py shell\

	We can figure stuff out about our models by using the interactive shell:

	# import pages model from pages app
	>>> from pages.models import Page 
	# we are retrieving a single page from the database and storing it in the object pg, in this example we are retrieving the home page
	>>> pg = Page.objects.get(permalink='/')

	>>> pg.title\
	'QC Co Homepage'

	>>> pg.update_date
	datetime.datetime(2018, 3, 18, 3, 5, 47, tzinfo=<UTC>)

	>>> pg.bodytext
	'<your page content will show here>'

#assert False 
	Uncomment Asert False to trigger the Django Error Page in root/pages/views.py, this is a supremely useful debug tool
	Go to the Assert False on the Error page and open the Local vars, there we can see what the context dictionary contains, the context dictionary contains the page variables that we are passing to the template
