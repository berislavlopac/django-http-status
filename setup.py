from setuptools import setup

setup(
    name            ="django-http-status",
    version         ="0.2",
    description     ="A library of useful HTTP response codes for Django.",
    long_description="Django includes a number of HttpResponse subclasses representing various HTTP response codes. This library completes that list adding the missing codes as defined in HTTP1.1.",
    keywords        ="django, views, http, response, status",
    author          ="Benjamin Slavin <benjamin.slavin@gmail.com>, Justin Fiore <justin.fiore@gmail.com>, Berislav Lopac <berislav@lopac.net>",
    author_email    ="berislav@lopac.net",
    url             ="https://bitbucket.org/BerislavLopac/django-http-status",
    license         ="BSD",
    packages        =["http_status"],
    zip_safe        =False,
    install_requires=[],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
)