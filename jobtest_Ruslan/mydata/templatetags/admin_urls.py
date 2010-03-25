from django import template
from django.db import models
from django.core.urlresolvers import reverse, NoReverseMatch

register = template.Library()


@register.tag(name="edit_list")
def do_edit_list(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, variable_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError,\
                "%r tag requires a single argument" % token.contents.split()[0]
    return AdminPageUrlNode(variable_name)


class AdminPageUrlNode(template.Node):
    def __init__(self, variable, action="change"):
        self.variable = template.Variable(variable)
        self.action = action

    def render(self, context):
        variable = self.variable.resolve(context)
        if issubclass(variable.__class__, models.Model):
            try:
                return reverse('admin:%s_%s_%s' % (variable._meta.app_label,
                                                  variable._meta.module_name,
                                                  self.action),
                               args=[variable.id])
            except NoReverseMatch:
                pass
