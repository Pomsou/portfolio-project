from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=30)
    post_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def summary(self):
        return self.body[:60] + '...'

    def post_date_field(self):
        return self.post_date.strftime('%A %e, %Y')
