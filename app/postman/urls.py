from __future__ import unicode_literals
from django.conf import settings
from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views
from django.core.urlresolvers import reverse_lazy
from django.conf.urls import url
from django import VERSION
if VERSION < (1, 10):
    from django.core.urlresolvers import reverse_lazy
else:
    from django.urls import reverse_lazy
if getattr(settings, 'POSTMAN_I18N_URLS', False):
    from django.utils.translation import pgettext_lazy
else:
    def pgettext_lazy(c, m): return m

from .views import (InboxView, SentView, ArchivesView, TrashView,
        WriteView, ReplyView, MessageView, ConversationView,
        ArchiveView, DeleteView, UndeleteView, MarkReadView, MarkUnreadView)


app_name = 'postman'
urlpatterns = [


    #url(r'^inbox/?$',views.InboxView, name='inbox'),
    url(pgettext_lazy('postman_url', r'^inbox/(?:(?P<option>m)/)?$'), InboxView.as_view(), name='inbox'),
    url(pgettext_lazy('postman_url', r'^sent/(?:(?P<option>m)/)?$'), SentView.as_view(), name='sent'),
    # Translators: keep consistency of the <option> parameter with the translation for 'm'
    url(pgettext_lazy('postman_url', r'^archives/(?:(?P<option>m)/)?$'), ArchivesView.as_view(), name='archives'),
    # Translators: keep consistency of the <option> parameter with the translation for 'm'
    url(pgettext_lazy('postman_url', r'^trash/(?:(?P<option>m)/)?$'), TrashView.as_view(), name='trash'),
    url(pgettext_lazy('postman_url', r'^write/(?:(?P<recipients>[^/#]+)/)?$'), WriteView.as_view(), name='write'),
    #url(pgettext_lazy('postman_url', r'^messageme/(?:(?P<recipients>[^/#]+)/)?$'), MessageMeView.as_view(), name='messageme'),
    url(pgettext_lazy('postman_url', r'^reply/(?P<message_id>[\d]+)/$'), ReplyView.as_view(), name='reply'),
    url(pgettext_lazy('postman_url', r'^view/(?P<message_id>[\d]+)/$'), MessageView.as_view(), name='view'),
    # Translators: 't' stands for 'thread'
    url(pgettext_lazy('postman_url', r'^view/t/(?P<thread_id>[\d]+)/$'), ConversationView.as_view(), name='view_conversation'),
    url(pgettext_lazy('postman_url', r'^archive/$'), ArchiveView.as_view(), name='archive'),
    url(pgettext_lazy('postman_url', r'^delete/$'), DeleteView.as_view(), name='delete'),
    url(pgettext_lazy('postman_url', r'^undelete/$'), UndeleteView.as_view(), name='undelete'),
    url(pgettext_lazy('postman_url', r'^mark-read/$'), MarkReadView.as_view(), name='mark-read'),
    url(pgettext_lazy('postman_url', r'^mark-unread/$'), MarkUnreadView.as_view(), name='mark-unread'),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('postman:inbox'), permanent=True)),


]
