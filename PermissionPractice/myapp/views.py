from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView

from myapp.models import Post

class PostListView(PermissionRequiredMixin, ListView):  
    permission_required = "myapp.view_post"
    template_name = "post.html"
    model = Post

#for user view level use ---> permission required Mixin 
#for model level use -->>UserPassesTextMixin

from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import View

class PostListViewModelLevel(UserPassesTestMixin, View):
    template_name = "post_details.html"
    
    
    def test_func(self):
        return self.request.user.has_perm("myapp.set_published_status")
    
    
    def post(self, request, *args, **kwargs):
        post_id = request.POST.get('post_id')
        published_status = request.POST.get('published_status')
        if post_id:
            post = Post.objects.get(pk=post_id)
            post.is_published = bool(published_status)
            post.save()
        return render(request, self.template_name)
    
    def get(self, request, *args, **kwargs):
        return render(request,'myapp/post_details.html')