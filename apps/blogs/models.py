from django.db import models
from django.conf import settings


class Author(models.Model):
    full_name = models.CharField(max_length=128)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="authors")
    avatar = models.ImageField(upload_to="authors/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="blogs")
    categories = models.ManyToManyField(Category, related_name="blogs")
    tags = models.ManyToManyField(Tag, related_name="blogs", blank=True)

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="blogs/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.blog}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
