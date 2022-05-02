from django.db import models

# Create your models here.



class claim(models.Model):
    PROJECT = (
            ('Facebook', 'Facebook'),
            ('Election', 'Election'),
            ('Climate', 'Climate'),
            ('Tipline', 'Tipline')
    )
    CLAIM_SOURCE =(
            ('Facebook', 'Facebook'),
            ('Twitter', 'Twitter'),
            ('Instagram', 'Instagram'),
            ('Web', 'Web'),
            ('Email', 'Email'),
            ('YouTube', 'YouTube'),
            ('TikTok', 'TikTok'),        
    )
    MEDIA_TYPE = (
        ('Video','Video'),
        ('Text','Text'),
        ('Audio','Audio'),        
        ('Tweet','Tweet'),
        ('Pamphlet','Pamphlet'),        
    )
    STATUS = (
        ('Checked','Checked'),
        ('Unchecked','Unchecked'),
    )
    VERDICT = (
        ('TRUE','TRUE'),
        ('FALSE','FALSE'),
        ('UNKNOWN','UNKNOWN'),
    )
    
    VERDICT_SIMPLIFIED = (
        ('Positive','Positive'),
        ('Negative','Negative'),
        ('In_Between','In_Between'),
    )
    

    claim_id = models.AutoField(primary_key=True)
    project=models.CharField(max_length=50, null=True, blank=True, choices=PROJECT)
    claim_source=models.CharField(max_length=50,null=True, blank=True, choices = CLAIM_SOURCE)
    claim=models.CharField(max_length=5000)
    claim_publish_date = models.DateTimeField()
    claim_receive_date = models.DateTimeField()
    description = models.CharField(max_length=5000)
    verdict = models.CharField(max_length=10,null=True, blank=True, choices = VERDICT)
    media_type = models.CharField(max_length=20,null=True, blank=True, choices = MEDIA_TYPE)
    media_link_path = models.CharField(max_length=200, null=True, blank=True)
    claimant = models.CharField(max_length=20,null=True, blank=True)
    party = models.CharField(max_length=20,null=True, blank=True)
    topic = models.CharField(max_length=50,null=True, blank=True)
    sub_category = models.CharField(max_length=100,null=True, blank=True)
    source_link = models.CharField(max_length=100,null=True, blank=True)
    who_lodged_info = models.CharField(max_length=50,null=True, blank=True)
    status = models.CharField(max_length=9,null=True, blank=True, choices = STATUS)
    checker_name = models.CharField(max_length=50,null=True, blank=True)
    verdict_simplified = models.CharField(max_length=10,null=True, blank=True, choices= VERDICT_SIMPLIFIED)
    
    class Meta:
        db_table = 'claim'

    def __str__(self):
        return self.claim
