import re
from django.shortcuts import render, redirect
from numpy import source
from .models import individual, factchecker, claim
from django.db.models import Count

# Create your views here.
def dbupdate(request):
    return render(request,'dbupdate.html')


def add_record(request):
    if request.method == 'POST':

        project = request.POST.get('project')
        claim_source = request.POST.get('source')
        claim1 = request.POST.get('claim')
        claim_published = request.POST.get('claim_published')
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
        checkername = request.POST.get('checkername')
        checkerid = request.POST.get('checkerid')
        verdictsimplified = request.POST.get('verdictsimplified')
        e = individual()
        f = factchecker()
        c = claim()

        

        # counting
        c_count = individual.objects.all().filter(claimant=claimant,party=party).aggregate(Count('individual_id'))
        if c_count['individual_id__count'] ==0:
            print('Yes1')
            e.claimant = claimant.upper()
            e.party = party.upper()
            e.save()
            c.individual_id = e
        
        else:
            a = individual.objects.all().values('individual_id').filter(claimant=claimant,party=party)
            temp_obj =individual.objects.get(pk=a[0]['individual_id'])
            c.individual_id= temp_obj
            #print(temp_obj)

        #factcheckers
        f_count = factchecker.objects.all().filter(checker_id=checkerid).aggregate(Count('checker_id'))
        if f_count['checker_id__count'] ==0:
            print('Yes2')
            f.checker_id = checkerid.upper()
            f.checker_name = checkername.upper()
            f.save()
            c.checker_id = f
        else:
            f_count = factchecker.objects.all().values('checker_id').filter(checker_id=checkerid)
            temp_obj =factchecker.objects.get(pk=f_count[0]['checker_id'])
            c.checker_id = temp_obj


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
        c.topic = topic.upper()
        c.sub_category = subcategory.upper()
        c.source_link = media_link_ext
        c.who_lodged_info = wholodgeinfo.upper()
        c.status = status.upper()
        c.verdict_simplified = verdictsimplified.upper()

        c.save()        

        return redirect("/home")
    else:
        return render(request, 'dbupdate.html')