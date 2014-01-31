from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from cmstest.models import Hello

class HelloPlugin(CMSPluginBase):
	model = Hello
	name = _("Hello Plugin")
	render_template = "cmstest/hello_plugin.html"

	def render(self, context, instance, placeholder):
		context['instance'] = instance
		return context

plugin_pool.register_plugin(HelloPlugin)