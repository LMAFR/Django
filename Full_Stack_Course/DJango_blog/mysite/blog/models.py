from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    # The line below automatically sets the author to be the logged user:
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    # The line below automatically sets the default value of this date variable to that specied in TIME_ZONE (in settings.py)
    created_date = models.DateTimeField(default=timezone.now)
    # The published date could be blank (we could not want to publish it yet) or null (we could not have a publish date for some odd reason):
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """
        This is a method to update the (blank/null by default) publish_date.
        """
        self.published_date = timezone.now() 
        self.save()

    def approve_comments(self):
        """
        In some moment we will have a list of comments for the posts, so we could want to have this method, which allows us to filter those
        comments that have been approved. 
        """
        # The argument we pass to the line below must be equal to the corresponding attribute defined in the Comment model.
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        # Returns the new url created for that post:
        return reverse("post_detail", kwargs={"pk":self.pk})

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    post = models.ForeignKey("blog.Post", related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def get_absolute_url(self):
        # After adding a comment we will go back to the comment list:
        return reverse("post_list")

    def approve_comments(self):
        self.approved_comment = True
        self.save()

    def __str__(self) -> str:
        return self.text