from django.shortcuts import render, redirect
from dbupdate.models import claim

from django.db import connection


# Create your views here.
def dbfetch(request):
    return render(request,'dbfetch.html')



def fetchrecord(request):


    myDict = dict(request.POST.lists())
    myDict.pop('csrfmiddlewaretoken')
    print(myDict, type(myDict))
    ####

    print(myDict['project'],type(myDict['project']))
    project = request.POST.get('project').upper()
    claim_source = request.POST.get('source').upper()
    claim1 = request.POST.get('claim').upper()
    


    claim_published_from = request.POST.get('claim_published_from')
    claim_published_to = request.POST.get('claim_published_to')
    description = request.POST.get('description').upper()
    verdict = request.POST.get('verdict').upper()
    claimant = request.POST.get('claimant').upper()
    party = request.POST.get('party').upper()
    topic = request.POST.get('topic').upper()
    subcategory = request.POST.get('subcategory').upper()
    status = request.POST.get('status').upper()

    print(project,claim_source,claim1,claim_published_from,claim_published_to, description, verdict, claimant,party,topic,subcategory,status)
    i_mappings = {'individual_id':'individual_id', 'claimant':'claimant', 'party':'party'} 
    x = claim.objects.raw("SELECT * FROM individual",translations=i_mappings)
    
    #
    print(x)
    #
    #claimid,project, claim_source, claim, claim_publish_date, claim_receive_date, description, verdict, media_type,media_link_path, claimant, party, topic, sub_category, source_link, who_lodged_info, status,claim.checker_id, checker_name, verdict_simplified FROM claim LEFT JOIN individual ON claim.individual_id = individual.individual_id LEFT JOIN factchecker ON claim.checker_id = factchecker.checker_id")
    print(type(x))
    cursor = connection.cursor()
    cursor.execute(f''' SELECT claim_id,project, claim_source, claim, claim_publish_date, claim_receive_date, description,
           verdict, media_type,media_link_path, claimant, party, topic, sub_category,
            source_link, who_lodged_info, status,claim.checker_id, checker_name, verdict_simplified 
    FROM claim
    LEFT JOIN individual ON claim.individual_id = individual.individual_id
    LEFT JOIN factchecker ON claim.checker_id = factchecker.checker_id
    WHERE 
        project = 'TIPLINE' ''')
    data = cursor.fetchall()
    print(data,type(data))
    #x = claim.objects.raw(f''' SELECT claimid,project, claim_source, claim, claim_publish_date, claim_receive_date, description,
    '''       verdict, media_type,media_link_path, claimant, party, topic, sub_category,
            source_link, who_lodged_info, status,claim.checker_id, checker_name, verdict_simplified 
    FROM claim
    LEFT JOIN individual ON claim.individual_id = individual.individual_id
    LEFT JOIN factchecker ON claim.checker_id = factchecker.checker_id
    WHERE 
        project = 'TIPLINE'
    AND
        claim_source = 'YOUTUBE'
    AND
        claim like '%SENATOR%'
    AND
        claim_publish_date >='2017-05-19' AND claim_publish_date <='2017-07-19'
    AND
        description like '%SENATOR%'
    AND
        verdict = 'FALSE'
    AND
        claimant LIKE '%CORY%'
    AND 
        party LIKE '%%'
    AND
        topic LIKE '%%'
    AND
        sub_category LIKE '%%'
    AND
        who_lodged_info LIKE '%%'
    AND
        status = 'CHECKED'
    AND
        claim.checker_id = '2'
    AND
        checker_name LIKE '%John Doe%'
    AND
        verdict_simplified = 'IN_BETWEEN'  '''
    elist =claim.objects.all()
    d = {"el":x}
    return render(request, 'results.html',d)