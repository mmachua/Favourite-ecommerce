
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
#from django.contrib.auth import update_session_auth_hash
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.forms import HomeForm, HomeCreate
from home.models import Post
from home.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
#def home(request):
 #   return render(request,'home/home.html')

class HomeView(TemplateView):
    template_name = 'home/home.html'    

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-date')
        users = User.objects.exclude(id=request.user.id)

        args = {'form': form, 'posts': posts, 'users': users}
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid(): 
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['post']
            form = HomeForm()
            #return redirect('home:home')
        args = {'form': form, 'text': text }
        return render(request, self.template_name, args)
    
    def Homeimage(self, request):
        form = HomeForm(request.POST)
        if form.is_valid(): 
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            
           
            #return redirect('home:home')
        
        return render(request, self.template_name)



class AboutView(TemplateView):
    template_name = 'home/About.html'  

#class ContactView(TemplateView):
#    template_name = 'home/contact.html'


#    def contact(self,request):
#        form_class = ContactForm(request.POST or None)
#        if form_class.is_valid():
#            print(request.POST)   
        
#        return render(request, self.template_name, {
#            'form': form_class,
#        })


#@login_required
def shop(request):
    #args = {'user': request.user}
    return render(request,('home/shop.html'), {'user': request.user})


#contact form views are here
def contact(request):
    title = contact
    form_class = ContactForm(request.POST or None)
    form = ContactForm(request.POST or None)
    confirm_message = None
    if form.is_valid():
        name = form.cleaned_data['Email']
        content = ( form.cleaned_data['Email'])
        subject = 'Message from MYSITE.com'
        message = '%s %s' %(content, name)
        emailFrom = ( form.cleaned_data['Email'])
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True )
        title = 'Thanks!'
        confirm_message ="Thanks for the message we will get back to  you"
        form = None

        context = {'title': title, 'form': form, 'confirm_message': confirm_message }
    return render(request, 'home/contact.html', {
        'form': form_class,
    })

    