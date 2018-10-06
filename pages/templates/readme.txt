So why a second pages folder?

What if you have two apps in your project that each have a template named index.html? Django uses short circuit logic when searching for templates, so when it goes searching for templates/index.html, it will use the first instance it finds and that may not be in the app you wanted!

Adding the inner pages folder is an example of name spacing your templates. By adding this folder you can make sure Django retrieves the right template.