__title__ = "dj-rest-auth"
__description__ = "Authentication and Registration in Django Rest Framework."
__url__ = "http://github.com/jazzband/dj-rest-auth"
__author__ = "@iMerica https://github.com/iMerica"
__author_email__ = "imichael@pm.me"
__license__ = "MIT"
__copyright__ = "Copyright 2020 @iMerica https://github.com/iMerica"

from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution("dj-rest-auth").version
except DistributionNotFound:
    # package is not installed
    __version__ = None
