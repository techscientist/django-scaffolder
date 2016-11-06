# django-scaffolder

Generate a Django model, views, URLconf, and templates using a single command.

(Based on django-generate-scaffold. Updated for Python 3 and Django 1.10. See the old screencast for an idea of how it runs [here](http://vimeo.com/42399125).)


## Usage

### Generating Models, Views, URL Patterns, and Templates

- Install `django-scaffolder`:

        $ pip install https://github.com/bradlishman/django-scaffolder

- One pypi package sync happens use this:

        $ pip install django-scaffolder

- Add `generate_scaffold` to your `INSTALLED_APPS`
- Run the `generatescaffold` management command:

        $ python manage.py generatescaffold --help
        ... displays usage

- Create a model using the syntax in the help message:

        $ python manage.py generatescaffold blogs Post title:string body:text is_public:bool blog:foreignkey=Blog
        ... Generates a Post model, with title (CharField), body (TextField),
        ...     is_public (BooleanField), and blog (ForeignKey) fields.

### Generating Views, etc. Based on Existing Models

- Alternatively, you can generate views, urlpatterns, and templates for an existing model:

        $ python manage.py generatescaffold blogs --model Post
        ... Generates views, etc. for Post


- Note that if the model specified with the `--model` option has a `DateField` or a `DateTimeField`,
  date-based generic views will be generated based on that field. To specify a specific field to use,
  pass in the `--timestamp-field` option:

        $ python manage.py generatescaffold blogs --model Post --timestamp-field ctime

#### Limitations When Using Existing Models

For best results, existing models should implement a `get_absolute_url` method
which conforms to the urlpatterns used by `django-scaffolder`:

        @models.permalink
        def get_absolute_url(self):
            return ('<app_name>_<model_name>_detail', (), {'pk': self.pk})

Not conforming to this model will lead to broken links and potentially other
issues when rendering templates.


## Development

`django-scaffolder` is currently in ALPHA.


### How to Contribute

- Propose new features or report bugs by creating an issue on Github.
- Add new features, tests, or fix stuff and issue a pull request.


## Issues

If you experience any issues, please
[create an issue on Github](https://github.com/bradlishman/django-scaffolder/issues).
