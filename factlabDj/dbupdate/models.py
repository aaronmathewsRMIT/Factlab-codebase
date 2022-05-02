from django.db import models

# Create your models here.

class claim(models.Model):
    claim_id = models.AutoField(primary_key=True)
    project=models.CharField(max_length=50, null=True)
    claim_source=models.CharField(max_length=50,null=True)
    claim=models.CharField(max_length=5000)
    claim_publish_date = models.DateTimeField()
    claim_receive_date = models.DateTimeField()
    description = models.CharField(max_length=5000)
    verdict = models.CharField(max_length=10,null=True)
    media_type = models.CharField(max_length=20,null=True)
    media_link_path = models.CharField(max_length=100,null=True)
    claimant = models.CharField(max_length=20,null=True)
    party = models.CharField(max_length=20,null=True)
    topic = models.CharField(max_length=50,null=True)
    sub_category = models.CharField(max_length=100,null=True)
    source_link = models.CharField(max_length=100,null=True)
    who_lodged_info = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=9,null=True)
    checker_name = models.CharField(max_length=50,null=True)
    verdict_simplified = models.CharField(max_length=10,null=True)
    
    class Meta:
        db_table = 'claim'
    
    def __str__(self):
        return self.claim

