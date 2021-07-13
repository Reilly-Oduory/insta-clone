from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from .models import User, Comment, Profile, Tag, Post

# Create your tests here.
class TestProfileModel(TestCase):
    def setUp(self):
        self.user = User(username="reilly", email="test@gmail.com", password="paswerty1")
        self.user.save()
        self.reilly = Profile(bio="Lorem Ipsum", user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.reilly,Profile))

    def test_save_profile(self):
        self.reilly.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_update_bio(self):
        self.reilly.save_profile()
        self.reilly.update_profile_bio("This is my new bio")
        self.assertEqual(self.reilly.bio, "This is my new bio")

class TestTagModel(TestCase):
    def setUp(self):
        self.sky = Tag(tag="sky")

    def test_instance(self):
        self.assertTrue(isinstance(self.sky, Tag))
    
    def test_save_tag(self):
        self.sky.save_tag()
        tags = Tag.objects.all()
        self.assertTrue(len(tags) > 0)

    def test_delete_tag(self):
        self.sky.save_tag()
        tags = Tag.objects.all()
        self.sky.delete_tag()
        self.assertTrue(len(tags) == 0)

    def test_update_tag(self):
        self.sky.save_tag()
        self.sky.update_tag("rainbow")
        self.assertEqual(self.sky.tag, "rainbow")

class TestPostModel(TestCase):
    def setUp(self):
        self.user = User(username="reilly", email="test@gmail.com", password="paswerty1")
        self.user.save()
        # picture = SimpleUploadedFile(name="may31-8.jpg", content=open('C:\\Users\Work\Desktop\python\django-module\instagram-clone\media\profile_photos', "r"), content_type='image/jpeg')
        self.post = Post(image="C:\\Users\Work\Desktop\python\django-module\instagram-clone\media\profile_photos\may31-8.jpg", caption="This is a caption",likes=3,location="Kenya",user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_post(self):
        self.post.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_post(self):
        self.post.save_post()
        posts = Post.objects.all()
        self.post.delete_post()
        self.assertTrue(len(posts) == 0)

    def test_update_caption(self):
        self.post.save_post()
        self.post.update_caption("This is new sn")
        self.assertEqual(self.post.caption,"This is new sn")

class TestCommentModel(TestCase):
    def setUp(self):
        self.user = User(username="reilly", email="test@gmail.com", password="paswerty1")
        self.user.save()
        self.post = Post(image="C:\\Users\Work\Desktop\python\django-module\instagram-clone\media\profile_photos\may31-8.jpg", caption="This is a caption",likes=3,location="Kenya",user=self.user)
        self.post.save_post()
        self.comment = Comment(comment="Test Comment", post=self.post, user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_comment(self):
        self.comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) > 0)

    def test_delete_comment(self):
        self.comment.save_comment()
        comments = Comment.objects.all()
        self.comment.delete_comment()
        self.assertTrue(len(comments) == 0)