from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Contact,Blogs
# sending email
from django.conf import settings
from django.core.mail import send_mail
from django.core import mail
from django.core.mail.message import EmailMessage


def home(request):
    return render(request, 'home.html')


def search(request):
        query=request.GET['search']
        if len(query)>100:
            allPosts=Blogs.objects.none()
        else:
            allPoststitle=Blogs.objects.filter(title__icontains=query)
            allPostsdescribtion=Blogs.objects.filter(describtion__icontains=query)
            allPosts=allPoststitle.union(allPostsdescribtion)
        if allPosts.count()==0:
            messages.warning(request,"No Search Results")
        params={'allPosts':allPosts,'query':query}
            
        return render(request,'search.html',params)


def about(request):
    return render(request, 'about.html')


def handleblogs(request):
    if not request.user.is_authenticated:
        messages.warning(request,"hey just login and Use my Website")
        return redirect('/login')
    allposts=Blogs.objects.all()
    context={'allPost':allposts}
    print(allposts)
    return render(request, 'blog.html',context)


def contact(request):
    if request.method == "POST":
        fname = request.POST.get("name")
        femail = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        query = Contact(name=fname, email=femail,
                        phonenumber=phone, description=desc)
        query.save()
        # email sending start from here
        from_email = settings.EMAIL_HOST_USER
        connection = mail.get_connection()
        connection.open()
        email_message = mail.EmailMessage(
            f'Email From {fname}', f'UserEmail:{femail}\nUserPhoneNumber:{phone}\n\n\n QUERY:{desc}', from_email, ['yrohilla603@gmail.com','yashrohilla136@gmail.com'],connection=connection)

        email_clint = mail.EmailMessage ('ArkProcoder Response','Thanks for Reachingus \n\narkprodcoder.tech\n123456789\naneesh@prodcoder.tech',from_email,[femail],connection=connection)

        connection.send_messages([email_message,email_clint])
        connection.close()
        messages.info(
            request, "Thanks For Reaching Us! We will get back you soon...")
        return redirect('/contact')

    return render(request, 'contact.html')


def service(request):
    return render(request, 'service.html')


def handlelogout(request):
    logout(request)
    messages.info(request, "Logout Success")
    return redirect('/login')


def handlelogin(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pass1 = request.POST.get("pass1")
        myuser = authenticate(username=uname, password=pass1)

        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Success")
            return redirect('/')

        else:
            messages.warning(request, "invaild Crdentials")
            return redirect('/login')

    return render(request, 'login.html')


def handlesignup(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("Pass1")
        confirmpassword = request.POST.get("Pass2")
        # print(uname,email,password,confirmpassword)
        if password != confirmpassword:
            messages.warning(request, "Password is Incorrect")
            return redirect('/signup')

        try:
            if User.objects.get(username=uname):
                messages.info(request, "Username is Taken")
                return redirect('/signup')

        except:
            pass

        try:
            if User.objects.get(email=email):
                messages.info(request, "Email is taken")
                return redirect('/signup')
        except:
            pass

        myuser = User.objects.create_user(uname, email, password)
        myuser.save()
        messages.success(request, "Signup succcess Please Login !")
        return redirect('/login')

    return render(request, 'signup.html')
