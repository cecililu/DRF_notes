from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView

from myapp.models import Post

class PostListView(PermissionRequiredMixin, ListView):
    
    permission_required = "myapp.view_post"
    template_name = "post.html"
    model = Post
