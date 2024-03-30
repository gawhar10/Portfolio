from django.db import models


class Portfolio(models.Model):
    """A portfolio will contain details about a project."""
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=400)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.title
