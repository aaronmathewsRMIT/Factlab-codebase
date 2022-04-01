from django.db import models

# Create your models here.

class claim(models.Model):
    claim_id = models.AutoField(primary_key=True)
    project=models.CharField(max_length=50)
    claim_source=models.CharField(max_length=50)
    claim=models.CharField(max_length=50)
    claim_publish_date = models.DateTimeField()
    claim_receive_date = models.DateTimeField()
    description = models.CharField(max_length=500)
    verdict = models.CharField(max_length=10)
    media_type = models.CharField(max_length=20)
    media_link_path = models.CharField(max_length=100)
    claimant = models.CharField(max_length=20)
    party = models.CharField(max_length=20)
    topic = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=100)
    source_link = models.CharField(max_length=100)
    who_lodged_info = models.CharField(max_length=50)
    status = models.CharField(max_length=9)
    checker_name = models.CharField(max_length=50)
    verdict_simplified = models.CharField(max_length=10)
    
    class Meta:
        db_table = 'claim'
    
    def __str__(self):
        return self.claim_id

