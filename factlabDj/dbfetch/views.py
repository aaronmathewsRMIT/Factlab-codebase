from django.shortcuts import render, redirect
from dbupdate.models import claim

from django.db import connection


# Create your views here.
def dbfetch(request):
    return render(request,'dbfetch.html')


from django.db.models import Q

def fetchrecord(request):


    myDict = dict(request.POST.lists())
    myDict.pop('csrfmiddlewaretoken')
    print(myDict, type(myDict))
    ####
    query_s_flag_dict = {}
    query_l_flag_dict ={}
    query_para_dict = {}
    print(myDict['project'],type(myDict['project']))


    if request.POST.get('project').upper() == 'ANY':
        query_s_flag_dict['project'] = 0
    else:
        query_s_flag_dict['project'] = 1
        project = request.POST.get('project').upper()
        query_para_dict['project'] = request.POST.get('project').upper()

    if request.POST.get('source').upper() == 'ANY':
        query_s_flag_dict['claim_source'] = 0
    else:
        query_s_flag_dict['claim_source'] = 1
        claim_source = request.POST.get('source').upper()
        query_para_dict['claim_source'] = request.POST.get('source').upper()

    
    if request.POST.get('claim').upper() == "":
        query_l_flag_dict['claim'] =0
    else:
        query_l_flag_dict['claim'] = 1
        claim1 = request.POST.get('claim').upper()
        claim1 = claim1.split(',')
        claim1 = [s.strip() for s in claim1]
        query_para_dict['claim'] = claim1

        print(claim1)

    #query_flag_dict['claim_published_from'] = 1
    claim_published_from = request.POST.get('claim_published_from')
    #query_flag_dict['claim_published_to'] = 1
    claim_published_to = request.POST.get('claim_published_to')

    if request.POST.get('description') == "":
        query_l_flag_dict['description'] = 0
    else:
        query_l_flag_dict['description'] = 1
        description = request.POST.get('description').upper()
        description = description.split(',')
        description = [s.strip() for s in description]
        query_para_dict['description'] = description


    if request.POST.get('verdict').upper() == 'ANY':
        query_s_flag_dict['verdict'] = 0
    else:
        query_s_flag_dict['verdict'] = 1
        verdict = request.POST.get('verdict').upper()
        query_para_dict['verdict'] = request.POST.get('verdict').upper()

    query_s_flag_dict['claimant'] = 1
    query_para_dict['claimant'] = request.POST.get('claimant').upper().strip()
    query_s_flag_dict['party'] = 1
    party = request.POST.get('party').upper().strip()
    query_para_dict['party'] = request.POST.get('party').upper().strip()

    if request.POST.get('topic').upper() == "":
        query_l_flag_dict['topic']=0
    else:
        query_l_flag_dict['topic']=1
        topic = request.POST.get('topic').upper()
        topic = topic.split(',')
        topic = [s.strip() for s in topic]
        query_para_dict['topic'] = topic

    if request.POST.get('subcategory').upper() == "":
        query_l_flag_dict['sub_category']=0
    else:
        query_l_flag_dict['sub_category']=1
        subcategory = request.POST.get('subcategory').upper()
        subcategory = subcategory.split(',')
        subcategory = [s.strip() for s in subcategory]
        query_para_dict['sub_category'] = subcategory

    query_s_flag_dict['status']=1
    query_para_dict['status'] = request.POST.get('status').upper()

    print(query_s_flag_dict)
    print(query_l_flag_dict)
    print("$$$$", query_para_dict)
    #checklist =['claim','description','topic','subcategory']
    query_l = ""
    for key in query_l_flag_dict:
        if query_l_flag_dict[key]:
            query_l = query_l + key + " SIMILAR TO '%%("  
            query_l = query_l +"".join( f"{w}|"for w in query_para_dict[key])
            query_l = query_l[:-1]
            query_l = query_l +")%%' AND "

    query_l =query_l[:-4]
    ##print("!!!!!!")
    print(query_l)        

    query_s =""
    for key in query_s_flag_dict:
        if query_s_flag_dict[key]:
            query_s = query_s + key + " = "  +f"'{query_para_dict[key]}'"
            #print("--",query_s)      
            #query_s = query_s +", ".join( f"'{w}'"for w in query_para_dict[key])

            query_s = query_s +" AND "
            #print("$$$&",query_s)
    #print("8888")
    query_s = query_s[:-1]
    #print(query_s+" "+query_l)        
    query = query_s+" "+query_l
    date_query = " claim_publish_date >= '"+claim_published_from +"' AND claim_publish_date <= '"+claim_published_to+"' AND "
    query = " SELECT * FROM claim WHERE "+date_query + query
    print("&&&&&")
    print(query)
    #query =  " SELECT * FROM claim WHERE project = 'FACEBOOK' AND description SIMILAR TO '%%(SCOTT)%%'"
    print(query)
    claim_list = claim.objects.raw(query)
    print(connection.queries)
    print(type(claim_list))
 
    #
    #claimid,project, claim_source, claim, claim_publish_date, claim_receive_date, description, verdict, media_type,media_link_path, claimant, party, topic, sub_category, source_link, who_lodged_info, status,claim.checker_id, checker_name, verdict_simplified FROM claim LEFT JOIN individual ON claim.individual_id = individual.individual_id LEFT JOIN factchecker ON claim.checker_id = factchecker.checker_id")
    #print(type(x))
    #cursor = connection.cursor()
    #cursor.execute(f''' SELECT claim_id,project, claim_source, claim, claim_publish_date, claim_receive_date, description,
    #       verdict, media_type,media_link_path, claimant, party, topic, sub_category,
    #        source_link, who_lodged_info, status,claim.checker_id, checker_name, verdict_simplified 
    #FROM claim
    #LEFT JOIN individual ON claim.individual_id = individual.individual_id
    #LEFT JOIN factchecker ON claim.checker_id = factchecker.checker_id
    #WHERE 
    #    project = 'TIPLINE' ''')
    #data = cursor.fetchall()
    #print(data,type(data))
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
    print(type(claim_list))
    d = {"el":claim_list}
    return render(request, 'results.html',{"body":claim_list})