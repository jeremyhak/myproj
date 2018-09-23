from __future__ import unicode_literals

from django.template import Node, Library

register = Library()


class AutoPaginateNode(Node):
    def render(self, context):
        return ''


@register.tag
def autopaginate(parser, token):
    return AutoPaginateNode()


class PaginateNode(Node):
    def render(self, context):
        return ''


@register.tag
def paginate(parser, token):
    return PaginateNode()
