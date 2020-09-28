<h1 align="center">Product Manager</h1>
<p align="center">
  	<img alt="Repository size" src="https://img.shields.io/github/repo-size/igorsilva3/product_manager">
  	<a href="https://github.com/igorsilva3/product_manager/commits/master">
    	<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/igorsilva3/product_manager">
  	</a> 
  	<img alt="License" src="https://img.shields.io/github/license/igorsilva3/product_manager">
  	<a href="https://github.com/igorsilva3/product_manager/stargazers">
    	<img alt="Stargazers" src="https://img.shields.io/github/stars/igorsilva3/product_manager">
  	</a>
</p>

> This is a Django project. A product manager, where it has the register of product, updates of data product, the exclusion of product and th listing of all products added. :stars:

## :pushpin: Table of Contents
* [Pages screenshot](#pages-screenshot)
* [Technologies](#technologies)
* [Prerequisites](#prerequisites)
* [License](#license)


## Pages screenshot

| ![Page Home](https://i.imgur.com/6MKi77x.jpg)           | ![Page Add Product](https://i.imgur.com/FdLVD8M.jpg) | 
|---------------------------------------------------------|------------------------------------------------------|
| ![Page Update Product](https://i.imgur.com/XtTbDAE.jpg) | ![Page Search](https://i.imgur.com/BN2mVCp.jpg)      | 


## Technologies
* [Python](https://www.python.org/) 
* [Django Framework](https://www.djangoproject.com/)
* [Postgresql](https://www.postgresql.org/)
* [Django-Filter](https://django-filter.readthedocs.io/en/stable/)
* [Django-Boostrap-Pagination](https://pypi.org/project/django-bootstrap-pagination/)
* [Django-Widget-Tweaks](https://pypi.org/project/django-widget-tweaks/)
* [Pillow](https://pillow.readthedocs.io/en/stable/)

## Prerequisites
* Python 3.7.1+
* Postgresql

### Creation of virtual environment
```bash
# Installing virtualenv for Python
$ pip install virtualenv

# Creating your virtual environment
$ python3 -m virtualenv name-of-your-virtual-environment

# Activating virtual environment
$ source name-of-your-virtual-environment/bin/activate
```

### Installing dependencies
```bash
# Enter in folder of project
$ cd product_manager/
``` 
Make sure what the virtual environment this activated
```bash
# Installing requirements
(name-of-your-virtual-environment) $ pip install -r requirements.txt
``` 

### Migrating database
```bash
# Building the database tables and fields
(name-of-your-virtual-environment) $ python manage.py makemigrations

# Migrating for database
(name-of-your-virtual-environment) $ python manage.py migrate
``` 

## License

Released in 2020 License :closed_book:

Made with :heart: by [Igor Silva](https://github.com/igorsilva3).
This project is under the [MIT license](./LICENSE).

Give a :star: if this project helped you!
