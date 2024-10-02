from django.db import models


class Portfolio(models.Model):
    """A portfolio will contain details about a project."""
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=400)
    text = models.TextField()
    source_code_url = models.CharField(max_length=400)
    live_site_url = models.CharField(max_length=400)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.title
