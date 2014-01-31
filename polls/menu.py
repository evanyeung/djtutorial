from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from polls.models import Poll

class PollsMenu(CMSAttachMenu):
	name = _("Polls Menu")

	def get_nodes(self, request):
		'''
		used to build the menu tree
		'''
		nodes = []
		for poll in Poll.objects.all():
			# the menu tree consists of NavigationNode instances
			# Each NavigationNode takes a label as its first argument, a URL as
			# its second argument and a (for this tree) unique id as its third
			# argument.
			node = NavigationNode(
				poll.question,
				reverse('polls.views.detail', args=(poll.pk,)),
				poll.pk
			)
			nodes.appent(node)
		return nodes

menu_pool.register_menu(PollsMenu)