from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils import timezone

class Template(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Question(models.Model):
    template = models.ForeignKey(Template)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Request(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    template = models.ForeignKey(Template)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})

    def status(self):
        if not self.latest_revision():
            return {'text': "Pending approval", 'sort': 0}

        if self.latest_revision().rejected():
            return {'text': "Rejected", 'sort': 100}

        if any([revision.implemented < timezone.now() for revision in self.revision_set.all()]):
            return {'text': "Implemented", 'sort': 90}

        if self.latest_revision().approved():
            return {'text': "Pending implementation", 'sort': 10}
        else:
            return {'text': "Pending approval", 'sort': 0}

    def latest_revision(self):
        return self.revision_set.first()        

class Revision(models.Model):
    created = models.DateTimeField(auto_now_add=True)   
    request = models.ForeignKey(Request)
    implemented = models.DateTimeField()
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return "Revision %s of %s" % (str(self.created), self.request.name)

    def approved(self):
        for comment in self.comment_set.all():
            if comment.approves:
                return comment
            elif comment.rejects:
                return False

        return False

    def rejected(self):
        for comment in self.comment_set.all():
            if comment.approves:
                return False
            elif comment.rejects:
                return comment

        return False

    def reason(self):
        if self.rejected():
            return self.rejected()
        if self.approved():
            return self.approved()

        return ""

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)   
    revision = models.ForeignKey(Revision)
    user = models.ForeignKey(User)
    approves = models.NullBooleanField(null=True)
    rejects = models.NullBooleanField(null=True)
    text = models.TextField()

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return "%s: %s" % (self.user, self.text)

class Answer(models.Model):
    revision = models.ForeignKey(Revision)
    question = models.ForeignKey(Question)
    text = models.TextField()

    def __unicode__(self):
        return self.question.name