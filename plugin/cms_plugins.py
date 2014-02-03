from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from plugin.models import ct
from django.utils.translation import ugettext as _

class ContactPlugin(CMSPluginBase):
    model = ct # Model where data about this plugin is saved
    name = _("Contact Plugin") # Name of the plugin
    render_template = "plugin/plugin.html" # template to render the plugin with

    def render(self, context, instance, placeholder):
        context.update({'contact':instance.contact})
        return context

plugin_pool.register_plugin(ContactPlugin) # register the plugin