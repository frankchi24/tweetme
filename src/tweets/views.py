from django.shortcuts import render
from .models import Tweet
from django.views.generic import ListView,DetailView
# Create your views here.


class TweetDetailView(DetailView):
	queryset = Tweet.objects.all()

class TweetListView(ListView):
	queryset = Tweet.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView,self).get_context_data(*args,**kwargs)
		return context




def tweet_detail_view(request,pk=None):
	obj = Tweet.objects.get(pk=pk)
	context = {
	"object":obj

	}
	print('yes')
	return render(request, "tweets/detail_view.html",context)



def tweet_list_view(request):
	queryset = Tweet.objects.all()
	context = {
	"object_list":queryset
	}
	return render(request, "tweets/list_view.html",context)
