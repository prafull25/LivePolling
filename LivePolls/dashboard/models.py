from django.contrib.auth.models import User
from django.db import models


class DailyRank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total_score = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-total_score', 'date']  # Order ranks by total_score (high to low), then by date (oldest to newest)

    def __str__(self):
        return f"{self.user.username} ({self.total_score} points) - {self.date}"
