from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class PollApp(CMSApp):
	name = _("Poll App")#app name
	urls = ["polls.urls"]#link app to url config

apphook_pool.register(PollApp)