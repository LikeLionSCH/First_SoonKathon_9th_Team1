from django.db import models

# Create your models here.
COLOR_CHOICES = {
      ('ivory','아이보리'), #오른쪽에 있는 것이 화면에 보인다.
      ('black', '블랙'),
      ('not-specified', 'Not Specified')
  }
class Team1(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    sale_price = models.CharField(max_length=50)
    sale_period = models.CharField(max_length=50)
    color = models.CharField(max_length=80,choices=COLOR_CHOICES, null=True)
    number = models.CharField(max_length=50)
    img = models.ImageField(upload_to = "team1/", blank=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    team1 = models.ForeignKey(Team1, on_delete=models.CASCADE)

    def __str__(self):
        return self.content