from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE


# Create your models here.
class User(AbstractUser):
    pass

class Profile(models.Model):
    fullname = models.CharField(max_length=60)
    profile_pic = models.ImageField(upload_to = 'profile_photos/', null=True, blank=True)
    bio = models.TextField()
    user = models.ForeignKey(User, on_delete=CASCADE)

    def save_profile(self):
        self.save()

    def update_profile_bio(self, new_bio):
        previous_bio = self.bio
        self.bio = new_bio
        self.save()

class Tag(models.Model):
    tag = models.CharField(max_length=30)

    def __str__(self):
        return self.tag

    def save_tag(self):
        self.save()

    def delete_tag(self):
        self.delete()

    def update_tag(self, tag_name):
        previous = self.tag
        self.tag = tag_name
        self.save()

class Post(models.Model):
    image = models.ImageField(upload_to = 'posts/')
    caption = models.TextField(null=True, blank=True)
    likes = models.IntegerField(default=0)
    location = models.CharField(max_length=30, null=True, blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ['post_date']

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def update_caption(self, new_caption):
        previous = self.caption
        self.caption = new_caption
        self.save()
    
    def post_like(self):
        self.likes = self.likes+1
        self.save()

class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)
    
    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()
