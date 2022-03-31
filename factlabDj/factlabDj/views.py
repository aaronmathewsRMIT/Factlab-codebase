from django.shortcuts import render, HttpResponse

# Create your views here.
def landingpage(request):
    a = '''
    <h1>Welcome to Factlab DB!</h1>
    <h2><a href="dbupdate">Update Database</a> </h2>
    '''
    return HttpResponse(a)
    #return render(request,'landingpage.html')