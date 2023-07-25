from django.shortcuts import render,redirect
from .models import*
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.db.models import Q


from django.contrib import messages



# Create your views here.




def index(request):
    return render(request,'index.html')

@never_cache      
@login_required(login_url="login")      

def commenter(request,id):
    # show_comment = comment_user.objects.all()

    # all_image = profile.objects.all()
    
    cc = book_table.objects.get(id=id)
    print(cc)
    show_comment = comment_user.objects.filter(post_id=cc)
    print(show_comment,"g")
        
    return render(request,'comment.html',{'show_comment':show_comment})

    

@never_cache      
@login_required(login_url="login")      

def home(request):
    return render(request,'home.html')


@login_required(login_url='login')
@never_cache

def about(request):
    return render(request,'about.html')

@login_required(login_url='login')
@never_cache
def courses(request):
    c_data=courses_data.objects.all()
    return render(request,'courses.html',{'c':c_data})

    

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        au=authenticate(username=username, password=password)  
        print(au    )
        if au is not None:
            user1 = User.objects.get(username = au)
            
            user_profile1 = profile.objects.filter(user=user1)
        
            if user_profile1:
                for i in user_profile1:
                            if i.is_active is True:
                                print("tt")
                                auth.login(request,au)
                                return redirect('home')
                            else:
                                messages.error(request,"You Are Temprary Banned From Website ... ")
                                return redirect('login')
                        
            else:
                auth.login(request,au)
                return redirect('home')
            
            
                
                
                
        else:
            return redirect("login")   
        
    else:
        return render(request,'login.html')
            
        
        
        

def logout(request):
    auth.logout(request)
    return redirect('index')



def signup(request):
        if request.method == 'POST':
            username=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            cpassword=request.POST['cpassword']
            if password==cpassword:
                if User.objects.filter(username=username).exists():
                 messages.error(request,'email Already exist')
                 return redirect('login')
                else:
                   User.objects.create_user(username=username,email=email,password=password)
                   messages.success(request,'sucessfully Signup')
                   return render(request,'login.html')
               
            else:
                messages.error(request,'Passeword does not Matched  try again')
                return redirect('signup')
        else:
            return render(request,'signup.html')




# def signup(request):
#     if request.method == 'POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         cpassword=request.POST['cpassword']
#         if password==cpassword:
#           User.objects.create_user(username=username,password=password,)
#           return redirect('login')
#         else:
#             return render(request,'signup.html')
    
#     else:
#         return render(request,'signup.html')


    





@login_required(login_url='login')
@never_cache
def contact_user(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        misg=request.POST['misg']
        contact.objects.create(name=name,email=email,subject=subject,misg=misg)
        messages.success(request,'Your message has been sent. Thank you!')
        return  redirect('home')
        
    else:
        return render(request,'contact.html')
        
    
def person():
    user=User.objects.filter(username=user)
    
    
@login_required(login_url='login')
def book_cat(request,cat):
    data = Category.objects.get(book_category=cat)
    books = book_table.objects.filter(book_type=data)
    print(books)
    return render(request,"book_cat.html",{'books':books})
    
@login_required(login_url='login')
def book_click(request):
    Category_data=Category.objects.all()
    return render(request,'base.html',{'Category_data':Category_data})


@login_required(login_url='login')
def profile_update(request):
        user_n = User.objects.get(username = request.user)
        p = profile.objects.filter(user = user_n)
        
        if p:
            return redirect('profile_user')
        else:
    
            if request.method == "POST":
                user = request.user
                username=request.POST['fname']
                lname=request.POST['lname']
                mobile=request.POST['mobile']
                email=request.POST['email']
                user_profile=request.FILES['image']
                profile.objects.create(user=user,first_name=username,Last_name=lname,email=email,mobile_no=mobile,user_image=user_profile)
                messages.success(request,'Update Successfully')
                return redirect('profile_update')
            else:
                    
                #   sd=profile.objects.all().values('first_name','Last_name','mobile_no')
                return render(request,'profile_update.html')
            # else:
           #  return redirect('profile_user')
@never_cache      
@login_required(login_url="login")      
def show_profile(request):
    return render(request,'profile_user.html')
    
    
    
def profile_user(request):
    user_n = User.objects.get(username = request.user)
    p = profile.objects.filter(user = user_n)
    s = profile.objects.all()
    return render(request,'d.html',{'p':p,'s':s})
    
@login_required(login_url='login')
def book_read(request,id):
    books = book_table.objects.get(id=id)
    # show_comment = comment_user.objects.filter(
    #         Q(user=request.user)&Q(post_id=books.id))
    # print(show_comment,"g")
    # show_comment = comment_user.objects.all()
    return render(request,"book_content.html",{'books_read':books,
                                               })



def comnt(request):
   
    if request.method=='POST':
        
        post_id=request.POST['post_id']
        user=request.POST['user']
        cmnt=request.POST['comment']
        new_user = profile.objects.get(user=request.user)
        hh = book_table.objects.get(id=post_id)
        comment_user.objects.create(post_id=hh,user=new_user,com=cmnt)

        return redirect(f"book_read/{post_id}")
        
    else:
        return render(request,'comment.html',)
        
@never_cache      
@login_required(login_url="login")      
       
def likepost(request):
    if request.method=='POST':
        
        post_id=request.POST['post_id']
        user=request.POST['user']
        cmnt=request.POST['comment']
        
        new_user = profile.objects.get(user=request.user)
        hh = book_table.objects.get(id=post_id)
        comment_user.objects.create(post_id=hh,user=new_user,com=cmnt)

        return redirect(f"book_read/{post_id}")
    
    
@never_cache      
@login_required(login_url="login")      
def delit_comment(request,id):
    d=comment_user.objects.get(id=id)
    d.delete()
    return redirect("comnt")

@never_cache      
@login_required(login_url="login")      
      
def search(request):
        if request.method=='POST':
         s=request.POST['search']
         print(s)
         if s!=None:
          v=book_table.objects.filter(Q(book_name__icontains=s) | Q(Author__icontains=s))
          return render(request,'search_item.html',{'v':v})

            
        else:
            return redirect('/')

@never_cache      
@login_required(login_url="login")      
def searched_book(request,id):
    searched_book = book_table.objects.get(id=id)
    return render(request,"book_content.html",{'books_read':searched_book,
                                               }) 


@login_required(login_url='login')
def pton_start(request):
    return render(request,"pyton.html")


@login_required(login_url='login')
def pton_data(request,topic):
    data = fpd.objects.get(f=topic)
    pton_f = pb.objects.filter(fd=data)
    print(pton_f)
    return render(request,'peton.html',{'pton_f':pton_f})





    



    

    
    
    
    
        





