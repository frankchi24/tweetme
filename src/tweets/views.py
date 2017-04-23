from django.shortcuts import render
from .models import Tweet
from django.views.generic import (
ListView,
DetailView,
CreateView,
UpdateView,
DeleteView)
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.

class TweetCreateView(LoginRequiredMixin,FormUserNeededMixin,CreateView):
	form_class = TweetModelForm
	template_name = 'tweets/create_view.html'
	success_url = '/tweet/'
	login_url = '/admin/'

	# def form_valid(self,form):
	# 	if self.request.user.is_authenticated():
	# 		form.instance.user = self.request.user
	# 		return super(TweetCreateView, self).form_valid(form)
	# 	else:
	# 		form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["user must be logged in to continue"])
	# 		return self.form_invalid(form)

class TweetDetailView(DetailView):
	queryset = Tweet.objects.all()

class TweetListView(ListView):
	queryset = Tweet.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView,self).get_context_data(*args,**kwargs)
		return context

class TweetUpdateView(UserOwnMixin,UpdateView):
	queryset = Tweet.objects.all()
	form_class = TweetModelForm
	success_url = "/tweet/"
	template_name = 'tweets/update_view.html'

class TweetDeleteView(LoginRequiredMixin, DeleteView):
	model = Tweet
	template_name = 'tweets/delete_confirm.html'
	success_url = reverse_lazy('list')




def tweet_create_view(request):
	form = TweetModelForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
	context = {
		"form":form
	}
	return render(request, 'tweets/create_view.html', context)

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
