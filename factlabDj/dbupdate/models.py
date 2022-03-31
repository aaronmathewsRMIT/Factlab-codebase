from django.db import models

# Create your models here.

class individual(models.Model):
    individual_id = models.AutoField(primary_key=True)
    claimant = models.CharField(max_length=50)
    party = models.CharField(max_length=50)

    class Meta:
        db_table = 'individual'
    
    def __str__(self):
        return self.individual_id


class factchecker(models.Model):
    checker_id = models.CharField(max_length=10,primary_key=True)
    checker_name =models.CharField(max_length=50)

    class Meta:
        db_table = 'factchecker'
    
    def __str__(self):
        return self.checker_id


class claim(models.Model):
    claim_id = models.AutoField(primary_key=True)
    project=models.CharField(max_length=50)
    claim_source=models.CharField(max_length=50)
    claim=models.CharField(max_length=50)
    claim_publish_date = models.DateField()
    claim_receive_date = models.DateField()
    description = models.CharField(max_length=500)
    verdict = models.CharField(max_length=10)
    media_type = models.CharField(max_length=20)
    media_link_path = models.CharField(max_length=100)
    individual_id  = models.ForeignKey(individual, on_delete=models.CASCADE,db_column='individual_id')
    topic = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=100)
    source_link = models.CharField(max_length=100)
    who_lodged_info = models.CharField(max_length=50)
    status = models.CharField(max_length=9)
    checker_id = models.ForeignKey(factchecker,on_delete=models.CASCADE, db_column='checker_id')
    verdict_simplified = models.CharField(max_length=10)
    
    class Meta:
        db_table = 'claim'
    
    def __str__(self):
        return self.claim_id

