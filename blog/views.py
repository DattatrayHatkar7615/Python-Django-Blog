from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.
'''def home(request):
    data = {
        'posts':Post.objects.all()
    }
    return render(request,'home.html',data)'''
class PostListView(ListView):
    model=Post
    template_name="home.html"
    context_object_name='posts'
    ordering=['-date_posted']

class PostDetailView(DetailView):
    model=Post
    template_name="post_detai.html"


class PostCreateView(LoginRequiredMixin,CreateView):
    login_url ='/login/'
    redirect_field_name = 'login'
    model = Post
    template_name = 'post_form.html'
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):  
    login_url = '/login/'
    redirect_field_name = 'login'
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']  

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)    

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = Post
    template_name = 'post_confirm.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
