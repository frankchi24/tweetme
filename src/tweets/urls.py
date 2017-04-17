from django.conf.urls import url
from .views import tweet_list_view, tweet_detail_view,TweetListView,TweetDetailView


urlpatterns = [
	url(r'^$', TweetListView.as_view(), name="list"),
	# url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(),name='detail')
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name="detail")
    # url(r'^$', tweet_list_view, name="list"),
    # url(r'^1/$', tweet_detail_view, name="detail")
]
