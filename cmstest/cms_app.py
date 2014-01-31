from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class TestApp(CMSApp):
	name = _("Test")#app name
	urls = ["cmstest.urls"]#link app to url config

apphook_pool.register(TestApp)