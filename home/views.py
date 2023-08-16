from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,HttpResponse,redirect
from django.http import Http404, HttpResponse
# Create your views here.
from django.utils.timezone import now
from django.views import View
from django.views.generic import TemplateView,ListView
# Mixin Classes are the helper classes which can be used along with other class to provide extra functionality for class based views.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.views import LoginView , LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
# for class based views every class must be subclassed View class

class SignUpView(CreateView):
    template_name = 'home/signup.html'
    form_class = UserCreationForm
    success_url = '/'
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('Home')
        return super().get(request,*args,**kwargs)
    
    def form_valid(self, form):
        messages.success(self.request,'Your Account has been created Successfully!')
        return super().form_valid(form)








class HomeView(TemplateView):
    template_name = './home/home.html'
    extra_context = {'today':now}




# Mixin class should be passed befor the TemplateView class
class Authorized(LoginRequiredMixin,TemplateView):
    template_name = './home/authorized.html'
    login_url = '/admin'

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request,user)
#             messages.success(request,'Successfully logged in!')
#             return redirect(reverse('Home'))
#         else:
#             messages.warning(request,'User Not Found ')
#             return redirect(reverse('login'))
#     return render(request, 'home/login.html')

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('Home')
        return super().get(request, *args, **kwargs)
    def form_valid(self,form):
        messages.success(self.request,'Successfully logged in!')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.warning(self.request,'User Not Found! ')
        return super().form_invalid(form)

class LogoutIntefaceView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        # Display a success message
        messages.success(self.request, 'You have been logged out successfully.')
        
        # Call the parent class's dispatch method to perform logout
        response = super().dispatch(request, *args, **kwargs)
        
        return response
    