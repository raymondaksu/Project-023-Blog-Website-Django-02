# Project-023-Blog-Website-Django-02
A blog website comprises Bootstrap, Django and SQLite.

## Intructions of Django Blog
1. Create environment and activate it
2. Install django
3. Create requirement.txt, .gitignore and .env files
4. Install decouple
5. Move SECRET_KEY to .env and edit settigs.py
  * from decouple import config SECRET_KEY = config('SECRET_KEY')
6. Change folder name to src and Start project
7. Create an app and edit settings>INSTALLED_APPS
8. Migrate
9. Create superuser
10. Run server and check from browser
11. Create model (Category and Post)
12. Register the modelsin admin.py
13. Install pillow and edit requirement.txt
14. Make migrations + migrate
15. Run server and check, add items to models manually from admin panel
16. Add str function to models to make them seen other than an object
17. Add MEDIA_URl and MEDIA_ROOT to seetings.py and edit urls.py. Create media_root folder
18. Edit models.py for uploading images (paths)
19. For generating slug create signals.py file, and add a function to apps.py
20. Edit signals.py
21. Create Comment, Like and View classes in models. Make migrations + migrate
22. Create forms.py. Add PostForm and CommentForm
23. Edit views -> post_list
24. Edit settings.py ->TEMPLATES
  * 'DIRS': [BASE_DIR, "templates"]
25. Create folder templates under src folder and create file base.html
26. Create folders templates/blog under blog folder and create post_list.html
27. Create post_list function in views, edit both urls.py files
28. Create post_create function in views.(❗️ adding files, getting author info )
29. Create post_create.html and edit urls.py
30. uuid -> create file utils.py. Inside create a 10 char-long unique id to improve slugify
31. Create post_details function in views, edit urls.py, create post_details.html file
32. Pace post titles in post_list page anchor to link user to post_detail page
33. Add update and delete posts as above
34. Apply bootstrap starter template to base.html
35. Create navbar.html under src/templates
36. Include navbar in base.html
37. Create folders static/blog under application (blog) and create main.css file. (This is sth django wants)
38. Add main.css file's link to head section of base.html and add {% load static %} on top
39. Edit settings.py as
  * STATICFILES_DIRS = [BASE_DIR / "static"]
40. Apply a card style to post_list page with bootstrap.
41. Get a kit script from fontawesome and apply to base.html to icons for comment, like and view
42. Add functions to Post class in models.py to retrieve count of comments, likes and views
43. Import CommentForm to views and add comment to post_detail function
44. Add a method to Post class to retrieve all the comments of a post
45. Display all the comments of a post using a for loop in post_detail page, and add a form to the same page to get comments from the user
46. Import Like to views + add a like function + add like func to urls + create a form in post_detail.html (❗️ Note the action url)
47. Add an if statement to post_detail.html do display delete and update buttons. If the user is the author, he should see update & delete buttons for his own post
48. Now the problem is that a user can reach delete & update pages to any post by typing the url path to address bar. A temporary solution below. After using authentication we will change the way we do it.
49. Install HttpResponse from django.http in views and add an if statement to post_update and post_delete as
  * if request.user.id != obj.author.id
  * return HttpResponse("You are not authorized")
50. Install django-crispy-forms with pip and add crispy_forms to INSTALLED_APPS in settings.py. This third party app is for styling forms w bootstrap.
51. Edit the detail, create, update and delete pages as follows:
  * add {% load crispy_forms_tags %}
  * and change previously form.as_p to form|crispy
52. Style these pages with bootstrap
53. Create users app + add the new app to INSTALLED_APPS in settings.py
54. Create a Profile class in users > models add fields. Add a function to point the path to save the uploaded profile pictures of the user
55. pip freeze > requiremets.txt
56. makemigrations & migrate
57. Register Profile in users > admin.py
58. In order to automatically create a userf profile just after adding a user create a signals.py file (see the code)
59. Add a ready method in users > apps.py to make signals.py take effect
