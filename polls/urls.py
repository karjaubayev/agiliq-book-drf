from django.conf.urls import url

from .views import polls_list, polls_detail
from .api import PollList, PollDetail, ChoiceList, CreateVote


urlpatterns = [
	# url(r'^$', idea_list_view, name='idealist'),
    url(r'^polls/$', PollList.as_view(), name='polls_list'),
    url(r'^poll/(?P<pk>\d+)/$', PollDetail.as_view(), name='polls_detail'),
    url(r'^choices/$', ChoiceList.as_view(), name="choice_list"),
    url(r'^vote/$', CreateVote.as_view(), name="create_vote"),
]
