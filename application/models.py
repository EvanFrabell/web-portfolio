from django.db import models


class Baseball(models.Model):
    player = models.CharField(max_length=50, blank=True, null=True)
    team = models.CharField(max_length=50, blank=True, null=True)
    yearid = models.IntegerField(blank=True, null=True)
    games = models.CharField(max_length=10, blank=True, null=True)
    ab = models.CharField(max_length=10, blank=True, null=True)
    r = models.CharField(max_length=10, blank=True, null=True)
    h = models.CharField(max_length=10, blank=True, null=True)
    oneb = models.CharField(max_length=10, blank=True, null=True)
    twob = models.CharField(max_length=10, blank=True, null=True)
    threeb = models.CharField(max_length=10, blank=True, null=True)
    hr = models.CharField(max_length=10, blank=True, null=True)
    rbi = models.CharField(max_length=10, blank=True, null=True)
    sb = models.CharField(max_length=10, blank=True, null=True)
    cs = models.CharField(max_length=10, blank=True, null=True)
    bb = models.CharField(max_length=10, blank=True, null=True)
    so = models.CharField(max_length=10, blank=True, null=True)
    ibb = models.CharField(max_length=10, blank=True, null=True)
    hbp = models.CharField(max_length=10, blank=True, null=True)
    sh = models.CharField(max_length=10, blank=True, null=True)
    sf = models.CharField(max_length=10, blank=True, null=True)
    gidp = models.CharField(max_length=10, blank=True, null=True)
    obp = models.CharField(max_length=10, blank=True, null=True)
    slg = models.CharField(max_length=10, blank=True, null=True)
    ops = models.CharField(max_length=10, blank=True, null=True)
    mops = models.CharField(max_length=10, blank=True, null=True)
    woba = models.CharField(max_length=10, blank=True, null=True)
    twoba = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'baseball'

    def __str__(self):
        return self.player