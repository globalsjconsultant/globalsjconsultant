# from ckeditor.fields import RichTextField
from django.db import models
# from django.utils import timezone


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.CharField(max_length=200)
    replied = models.BooleanField(default=False)
    dated = models.DateTimeField(auto_now=True)

"""
class About(models.Model):
    content = RichTextField()

class MapLink(models.Model):
    link = models.CharField(max_length=1000)

STACKS_CATEGORY = (
    ('BACKEND', 'Back-end'),
    ('FRONTEND', 'Front-end'),
    ('DATABASE', 'Database'),
    ('FRAMEWORK', 'Framework'),
    ('CLOUD', 'Cloud'),
    ('LIBS', 'libraries'),
    ('TOOL', 'Tool'),
)


class CATEGORY(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100)
    template = models.ImageField(upload_to='project_templates')
    category = models.ForeignKey(CATEGORY, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
    link = models.URLField()
    github = models.URLField()

    def __str__(self) -> str:
        return self.title.title()


class ProjectDetail(models.Model):
    project = models.ForeignKey("Project", related_name="detail", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='thumb', default='')
    gif = models.ImageField(upload_to='thumb', default='')
    video = models.URLField()

    def __str__(self) -> str:
        return self.title.title()


class Stack(models.Model):
    projects = models.ManyToManyField('Project', related_name='stack')
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icon_stack')
    category = models.CharField(max_length=100, choices=STACKS_CATEGORY)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name.title()


class Service(models.Model):
    icon = models.FileField(upload_to='svgs')
    headline = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.headline


class Testimonial(models.Model):
    user = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='users')
    message = models.CharField(max_length=500)
    date = models.DateField(default=timezone.now)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.user


class Client(models.Model):
    logo = models.FileField(upload_to='logos')
    company = models.CharField(max_length=100)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.company
"""

