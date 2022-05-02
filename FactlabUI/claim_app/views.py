from django.shortcuts import render, redirect

from claim_app.decorators import unauthenticated_user
from .forms import claimForm
from .models import claim
from .filters import Searchclaim
from .decorators import unauthenticated_user
from django.db import connection

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, 'claim_app/landingpage.html')

@login_required(login_url='login')
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
        checker_name = request.POST.get('checkername')
        verdictsimplified = request.POST.get('verdictsimplified')
        c = claim()

     


        #claim table
        c.project = project.upper().strip()
        c.claim_source = claim_source.upper().strip()
        c.claim = claim1.upper().strip()
        c.claim_publish_date = claim_published
        c.claim_receive_date = claim_received
        c.description = description.upper().strip()
        c.verdict = verdict.upper().strip()
        c.media_type = mediatype.upper().strip()
        c.media_link_path = media_link_int.strip()
        c.claimant = claimant.upper().strip()
        c.party = party.upper().strip()
        c.topic = topic.upper().strip()
        c.sub_category = subcategory.upper().strip()
        c.source_link = media_link_ext.strip()
        c.who_lodged_info = wholodgeinfo.upper().strip()
        c.status = status.upper().strip()
        c.checker_name = checker_name.upper().strip()
        c.verdict_simplified = verdictsimplified.upper().strip()

        c.save()        

        return redirect("/home")
    else:
        return render(request, 'claim_app/dbupdate.html')

@login_required(login_url='login')
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

    if request.POST.get('status').upper() == 'ANY':
        query_s_flag_dict['status'] = 0
    else:
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
 
    
    print(type(claim_list))
    d = {"el":claim_list}
    return render(request, 'claim_app/results.html',{"body":claim_list})

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username= username, password = password)

        if user is not None:
            login(request, user)
            print("Yess")
            return redirect('home')
        
        else:
            messages.info(request,' Username or password incorrect')
            return render(request, 'claim_app/login.html')
    return render(request, 'claim_app/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dbupdate(request):

    form = claimForm()
    context = {'form':form}

    return render(request,'claim_app/dbupdate.html', context)

@login_required(login_url='login')
def dbfetch(request):
    return render(request, 'claim_app/dbfetch.html')

@login_required(login_url='login')
def dbsearchNew(request):
    myFliter = Searchclaim(request.GET)

    context = {"myFilter":myFliter}
    return render(request, 'claim_app/a.html',context)
