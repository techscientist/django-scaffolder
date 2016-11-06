from distutils.core import setup
from generate_scaffold import get_version

setup(
    name='django-scaffolder',
    version=get_version(),
    description='Generate a Django model, views, URLconf, '
                'and templates on the command line in seconds.',
    long_description='Please see the Github page for details: '
                     'https://github.com/bradlishman/django-scaffolder',
    keywords='django scaffolding scaffold CRUD',
    author='bradlishman',
    author_email='github@bradlishman.com',
    url='https://github.com/bradlishman/django-scaffolder',
    install_requires=['Django>=1.10'],
    packages=[
        'generate_scaffold',
        'generate_scaffold.generators',
        'generate_scaffold.management',
        'generate_scaffold.management.commands',
        'generate_scaffold.utils',
    ],
    package_data={'generate_scaffold': [
        'locale/ja/LC_MESSAGES/django.mo',
        'templates/generate_scaffold/models/*.txt',
        'templates/generate_scaffold/models/fields/*.txt',
        'templates/generate_scaffold/tpls/*.html',
        'templates/generate_scaffold/urls/*.txt',
        'templates/generate_scaffold/urls/urls/*.txt',
        'templates/generate_scaffold/views/*.txt',
        'templates/generate_scaffold/views/views/*.txt',
    ]},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Code Generators',
    ],
)
