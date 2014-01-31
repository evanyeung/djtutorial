from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from polls.menu import PollsMenu
from django.utils.translation import ugettext_lazy as _

class PollApp(CMSApp):
	name = _("Poll App")#app name
	urls = ["polls.urls"]#link app to url config
	menus = [PollsMenu] #attach a CMSAttachMenu to this apphook

apphook_pool.register(PollApp)
