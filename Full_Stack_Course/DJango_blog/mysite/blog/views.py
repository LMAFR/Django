from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, 
                                  DetailView, CreateView, 
                                  UpdateView, DeleteView)
from blog.models import Post, Comment 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.forms import CommentForm, PostForm
from django.urls import reverse_lazy
from django.utils import timezone

# Create your views here.

class AboutView(TemplateView):
    template_name = 'blog/about.html'

#################################################################

#                           POST MODEL                       #

#################################################################

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect("post_detail", pk=pk)

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        # The line below force this method to return the list of all the posts ordered from the most recent published date to the oldest one.
        # The __lte means "less than or equal to" and it is part of the filter (this is called "lookup").
        # The "-" before "published_date" provides the ordering direction:
        return Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")

class PostDetailView(DetailView):
    model = Post

# In order to only allow to see the create post settings to logged in users, we will add another inherited class to that view (this is equivalent 
# to use the login_required decorator in normal views, not CBVs):
class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = "blog/post_detail.html"

    form_class = PostForm

    model = Post

# The update post view will have the same restrictions that the CreateView one:
class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = "blog/post_detail.html"

    form_class = PostForm

    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):

    model = Post
    # We have to specify where we will be redirected after we delete the post (success url) 
    # and we have to ensure it will do it after delete the post (reverse_lazy):
    success_url = reverse_lazy("post_list")

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'

    model = Post

    # In this case we want the view to show as the drafted posts, so we want to see only those whose published_date has not been set yet:
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

#################################################################

#                           COMMENT MODEL                       #

#################################################################

# The pk argument links the comment to a specific post
@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # Case when we are sending the information to set the comment:
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            # commit=False makes "form" to be able to be modified after the call of the line below:
            comment = form.save(commit=False)
            # The first post of the line below is the attribute of the Comment model that links that model to the Post model (check models.py) 
            comment.post = post
            comment.save()
            # The line below redirect the user to the post_detail page corresponding to the specified pk (primary key) after submit the 
            # comment information (POST request):
            return redirect('post_detail', pk=post.pk)
        # If the request is not a POST request, the user is sent to the comment form through the next 3 lines:
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', context={'form':form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    # Remember we previously created a method to approve the comments:
    comment.approve_comments()
    # We linked the Comment model to the Post model so we can get the pk of the corresponding post 
    # and send the user to that corresponding url after approve the comment: 
    return redirect("post_detail", pk = comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    # In this case we have to previously store the value of the pk of the corresponding post, 
    # as once we delete the comment, we would not be able to access that pk:
    post_pk = comment.post.pk
    comment.delete()
    return redirect("post_detail", pk=post_pk)