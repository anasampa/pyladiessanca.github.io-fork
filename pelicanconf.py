AUTHOR = 'PyLadies São Carlos'
SITENAME = 'PyLadies São Carlos'
SITE_DESCRIPTION = 'PyLadies São Carlos é um grupo de mulheres que se reúne para aprender a programar em Python, compartilhar conhecimento e promover a inclusão de mulheres na tecnologia.'

AUTHOR_TWITTER = 'pyladiessanca'
AUTHOR_FACEBOOK = 'pyladiessanca'
AUTHOR_GITHUB = 'pyladiessanca'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme path
THEME = 'themes/pelican-mediumfox'

SUMMARY_MAX_LENGTH = 30

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MENUITEMS = [
    ('Sobre', './index.html'),
    ('Parcerias', './parcerias.html'),
    ('Blog', './archives.html'),
]