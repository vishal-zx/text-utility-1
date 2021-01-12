#This file is created by me - Vishal
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'text-analyze.html')

def output(request):
    mytext = request.GET.get('mytext', 'def')
    punct = request.GET.get('punc', 'off')
    upper = request.GET.get('upper', 'off')
    nline = request.GET.get('nline', 'off')
    space = request.GET.get('space', 'off')
    charcnt = request.GET.get('chrcnt', 'off')

    # mytext = request.GET.get('mytext', 'def')
    # choice = request.GET.get('choice', 'none')

    # print(upper)
    cnt=0
    
    if punct == "on":
        analyzed_text = ''
        punctuations = '''!()-[}]{;:'"'\',<>./?@#$%^&*_~'''
        for _ in mytext:
            if _ not in punctuations:
                analyzed_text += _
        mytext = analyzed_text
        pi = {'raw_data':mytext, 'analyzed_text':mytext}
        # return render(request, 'options.html', pi)
    
    if upper == "on":
        analyzed_text = ''
        for _ in mytext:
            analyzed_text += _.upper()
        mytext = analyzed_text
        pi = {'raw_data':mytext, 'analyzed_text':mytext}
        # return render(request, 'options.html', pi)
    
    if nline == "on":
        analyzed_text = ''
        for _ in mytext:
            if(_ != '\n'):
                analyzed_text += _
        mytext = analyzed_text
        pi = {'raw_data':mytext, 'analyzed_text':mytext}
        # return render(request, 'options.html', pi)
    
    if space == "on":
        analyzed_text = ''
        for idx in range(len(mytext) -1):
            if(not(mytext[idx]==' ' and mytext[idx+1]==' ')):
                analyzed_text += mytext[idx]
        if(mytext[-1]!=' '):
            analyzed_text += mytext[-1]
        mytext = analyzed_text
        pi = {'raw_data':mytext, 'analyzed_text':mytext}
        # return render(request, 'options.html', pi)
    
    if charcnt == "on":
        for _ in mytext:
            cnt+=1
        pi = {'raw_data':mytext,'analyzed_text':mytext, 'cnt':"Total characters are: "+str(cnt)}
        # return render(request, 'options.html', pi)
        
    else:
        print("ok")
        analyzed_text = mytext
        pi = {'raw_data':mytext, 'analyzed_text':mytext}
    
    return render(request, 'options.html', pi)

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')
