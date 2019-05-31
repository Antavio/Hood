from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *
# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    profile = Profile.objects.all()
    all_posts = Post.objects.all()
    return render(request,'hood_app/index.html',{"all_posts":all_posts,"prof_info":profile})

@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.prof_user = current_user
            profile.profile_Id = request.user.id
            profile.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'profile/new_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile_edit(request):
    current_user = request.user
    if request.method == 'POST':
        logged_user = Profile.objects.get(prof_user=request.user)
        form = ProfileForm(request.POST, request.FILES, instance=logged_user)
        if form.is_valid():
            form.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request,'profile/edit_profile.html',{'form':form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    business = Business.objects.filter(business_owner = current_user)

    try:   
        prof = Profile.objects.get(prof_user=current_user)
    except ObjectDoesNotExist:
        return redirect('new_profile')

    return render(request,'profile/profile.html',{'profile':prof,'business':business})

@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.business_owner = current_user
            business.save()
        return redirect('home')
    else:
        form = BusinessForm()
    return render(request,"business/business_form.html",{"form":form})

@login_required(login_url='/accounts/login/')
def business(request):
    all_businesses = Business.objects.all()
    return render(request,'business/business_index.html',{"all_businesses":all_businesses})

def search_post(request):
    if 'post' in request.GET and request.GET ["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_project_by_title(search_term)
        message = f'{search_term}'

        return render(request, 'search/search.html', {"message":message, "post":searched_posts})

    else:
        message = "No search results yet!"
        return render (request, 'search/search.html', {"message": message})

@login_required(login_url='/accounts/login/')
def contact(request):
    contacts = ContactInfo.objects.all()
    return render(request,'hood_app/contact_info.html',{"contacts":contacts})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_owner = current_user
            post.save()
        return redirect('home')
    else:
        form = PostForm()
    return render(request,"posts/create_post.html",{"form":form})

