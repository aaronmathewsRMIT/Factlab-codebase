import re
from django.http import HttpResponse
from django.shortcuts import render, redirect
from numpy import source
from .models import claim
from django.db.models import Count
from django.http import JsonResponse

# Create your views here.
def dbupdate(request):
    return render(request,'dbupdate.html')


def add_record(request):
    if request.method == 'POST':

        project = request.POST.get('project')
        claim_source = request.POST.get('source')
        claim1 = request.POST.get('claim')
        claim_published = request.POST.get('claim_published')
        print(claim_published)
        claim_received = request.POST.get('claim_received')
        description = request.POST.get('description')
        verdict = request.POST.get('verdict')
        mediatype = request.POST.get('mediatype')
        media_link_int = request.POST.get('media_link_int')
        claimant = request.POST.get('claimant')
        party = request.POST.get('party')
        topic = request.POST.get('topic')
        subcategory = request.POST.get('subcategory')
        media_link_ext = request.POST.get('media_link_ext')
        wholodgeinfo = request.POST.get('wholodgeinfo')
        status = request.POST.get('status')
        checker_name = request.POST.get('checkername')
        verdictsimplified = request.POST.get('verdictsimplified')
        c = claim()

     


        #claim table
        c.project = project.upper()
        c.claim_source = claim_source.upper()
        c.claim = claim1.upper()
        c.claim_publish_date = claim_published
        c.claim_receive_date = claim_received
        c.description = description.upper()
        c.verdict = verdict.upper()
        c.media_type = mediatype.upper()
        c.media_link_path = media_link_int
        c.claimant = claimant.upper()
        c.party = party.upper()
        c.topic = topic.upper()
        c.sub_category = subcategory.upper()
        c.source_link = media_link_ext
        c.who_lodged_info = wholodgeinfo.upper()
        c.status = status.upper()
        c.checker_name = checker_name.upper()
        c.verdict_simplified = verdictsimplified.upper()

        c.save()        

        return redirect("/home")
    else:
        return render(request, 'dbupdate.html')

def dbmodify(request):
    return render(request, 'claimupdate.html')

def update_record(request):
    
    claim_id_flag = 0
    claim_ids =request.POST.get('claim_ids')    
    if claim_ids == 'ALL':
        claim_id_flag = 0
    else:
        claim_id_flag = 1
    
    if claim_id_flag:
        query =  'SELECT * FROM claim WHERE claim_id IN ('
        claim_ids = claim_ids.split(',')
        query = query + ", ".join(claim_ids) + ") AND status = 'UNCHECKED'"
        print(query)
        claim_list = claim.objects.raw(query)
    {"body":claim_list}

    dataList = []

    for i in claim_list:
	    dataList.append({'claim id':i.claim_id, 'result':i.project, 'id':i.claim_source})
    print(dataList)
    return JsonResponse(dataList, safe=False)
    #return render(request, 'updateform.html',{"body":claim_list})