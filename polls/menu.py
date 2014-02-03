
from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu

from django.core.urlresolvers import reverse
from polls.models import Poll

class PollMenu(CMSAttachMenu):

	name = _("Poll Menu")

	def get_nodes(self, request):
		'''
		#used to build the menu tree
		'''

		nodes = []
		for poll in Poll.objects.all():
			# the menu tree consists of NavigationNode instances
			# Each NavigationNode takes a label as its first argument, a URL as
			# its second argument and a (for this tree) unique id as its third
			# argument.
			node = NavigationNode(
				_(poll.question),
				reverse('detail', args=(poll.pk,)),
				poll.pk
			)
			nodes.append(node)

		return nodes

menu_pool.register_menu(PollMenu)

'''
from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu

class NewMenu(CMSAttachMenu):

    name = _("new menu")

    def get_nodes(self, request):
        nodes = []
        n = NavigationNode(_('sample root page'), "/", 1)
        n2 = NavigationNode(_('sample settings page'), "/bye/", 2)
        n3 = NavigationNode(_('sample account page'), "/hello/", 3)
        n4 = NavigationNode(_('sample my profile page'), "/hello/world/", 4, 3)
        nodes.append(n)
        nodes.append(n2)
        nodes.append(n3)
        nodes.append(n4)
        return nodes

menu_pool.register_menu(NewMenu)
'''