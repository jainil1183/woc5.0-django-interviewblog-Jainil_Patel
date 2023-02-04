from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect,get_object_or_404
from .models import User
from .models import experience
from .models import comment
from customer.models import customer
from .forms import experienceForm
from django.template.defaultfilters import slugify
from django.contrib import messages


# Create your views here.


def home(request):
    if request.user.is_authenticated:
        try:
            details = customer.objects.get(username=request.user)
        except customer.DoesNotExist:
            details = None
        params = {'details':details}
        print(details)
        return render(request,'home.html/',params)
    else:
        return render(request, 'ano_user.html/')

def all_exp(request):
    if request.user.is_authenticated:
        temp = {}
        allexp = experience.objects.all()
        for i in allexp:
            if i.bookmark.filter(id=request.user.id).exists():
                temp[i.id] = 1
        params = {'allexp':allexp,'isbook':temp}
        print(temp)
        return render(request,'all_exp.html/',params)
    else:
        return render(request, 'ano_user.html/')

def my_exp(request):
    if request.user.is_authenticated:
        temp = {}
        allexp = experience.objects.filter(username=request.user)
        for i in allexp:
            if i.bookmark.filter(id=request.user.id).exists():
                temp[i.id] = 1
        params = {'allexp': allexp, 'isbook': temp}
        return render(request,'my_exp.html/',params)
    else:
        return render(request, 'ano_user.html/')


def expslug(request,slug):
    if request.user.is_authenticated:
        exp = experience.objects.filter(slug=slug).first()
        is_booked = False
        if exp.bookmark.filter(id=request.user.id).exists():
            is_booked = True
        exp = experience.objects.filter(slug=slug).first()
        comments = comment.objects.filter(exp=exp,parent=None)
        replies = comment.objects.filter(exp=exp).exclude(parent=None)
        re_dict = {}
        for reply in replies:
            if reply.parent.id not in re_dict.keys():
                re_dict[reply.parent.id] = [reply]
            else:
                re_dict[reply.parent.id].append(reply)
        params = {'exp': exp, 'is_booked': is_booked,'comments':comments,'replies':re_dict}
        return render(request, 'exp.html', params)
    else:
        return render(request, 'ano_user.html/')

def add_exp(request):
    if request.user.is_authenticated:
        submitted = False
        if request.method == "POST":
            form = experienceForm(request.POST, request.FILES)
            if form.is_valid():
                exp = form.save(commit=False)
                exp.username = request.user  # logged in user
                exp.slug = slugify(exp.title)
                exp.save()
                return HttpResponseRedirect('?submitted=True')
        else:
            form = experienceForm
            if 'submitted' in request.GET:
                submitted = True
        return render(request, 'add_exp.html', {'form': form, 'submitted': submitted})
    else:
        return render(request, 'ano_user.html/')

def edit_exp(request,slug):
    if request.user.is_authenticated:
        submitted = False
        exp = experience.objects.get(slug=slug)
        form = experienceForm(instance=exp)
        if request.method == "POST":
            form = experienceForm(request.POST, instance=exp)
            if form.is_valid():
                exp = form.save(commit=False)
                exp.username = request.user  # logged in user
                exp.slug = slugify(exp.title)
                exp.save()
                return HttpResponseRedirect('?submitted=True')
        else:
            if 'submitted' in request.GET:
                submitted = True
        return render(request, 'edit_exp.html', {'form': form, 'submitted': submitted})
    else:
        return render(request, 'ano_user.html/')

def delete_exp(request,slug):
    if request.user.is_authenticated:
        submitted = False
        exp = experience.objects.get(slug=slug)
        if request.method == "POST":
            exp.delete()
            messages.success(request, "Successfully deleted!!")
            return redirect('/home/my_exp/')
        else:
            if 'submitted' in request.GET:
                submitted = True
        return render(request, 'delete_exp.html', {'exp':exp, 'submitted': submitted})
    else:
        return render(request, 'ano_user.html/')

def add_bookmark(request,pk):
    if request.user.is_authenticated:
        exp = get_object_or_404(experience,id=pk)
        if exp.bookmark.filter(id=request.user.id).exists():
            exp.bookmark.remove(request.user)
            messages.success(request, "Successfully Removed Bookmark!!")
        else:
            exp.bookmark.add(request.user)
            messages.success(request, "Successfully Added Bookmark!!")
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        return render(request, 'ano_user.html/')

def my_bookmarks(request):
    if request.user.is_authenticated:
        my_books = User.objects.get(id=request.user.id).bookmark.all()
        params = {'my_books': my_books}
        return render(request, 'my_bookmarks.html/', params)
    else:
        return render(request, 'ano_user.html/')

def PostComment(request):
    if request.method=='POST':
        this_comment = request.POST.get("content")
        user = request.user
        exp_id = request.POST.get('exp_id')
        exp = experience.objects.get(id=exp_id)
        parent = request.POST.get("parent_id")

        if(parent==""):
            comment_obj = comment(writer=user, content=this_comment, exp=exp)
            comment_obj.save()
            messages.success(request, "Successfully Added Comment!!")
        else:
            parent_obj = comment.objects.get(id=parent)
            comment_obj = comment(writer=user,content=this_comment,exp=exp,parent=parent_obj)
            comment_obj.save()
            messages.success(request, "Successfully Added Reply!!")

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
