from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
<<<<<<< HEAD
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile
=======
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, InvestmentForm
from .models import Profile, Investment
from .utils import get_stock_price
>>>>>>> 7aacba6 (Implemented users feature)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
<<<<<<< HEAD
            username = form.cleaned_data.get('username')
=======
>>>>>>> 7aacba6 (Implemented users feature)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
<<<<<<< HEAD
                login(request, user)
=======
                auth_login(request, user)
>>>>>>> 7aacba6 (Implemented users feature)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        auth_logout(request)
        messages.success(request, "You have successfully logged out.")
<<<<<<< HEAD
        return redirect('login')  # Redirect to the login page after logout
    return render(request, 'users/logout.html')

#User profile

# @login_required
# def profile_view(request):
#     return render(request, 'users/profile.html')

@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    investments = profile.investments
    return render(request, 'users/profile.html', {'profile': profile, 'investments': investments})

#Investment feature

# @login_required
# def invest_view(request):
#     if request.method == 'POST':
#         stock_name = request.POST.get('stock_name')
#         amount = int(request.POST.get('amount'))
#         profile = Profile.objects.get(user=request.user)
#         if profile.coins >= amount:
#             profile.coins -= amount
#             if stock_name in profile.investments:
#                 profile.investments[stock_name] += amount
#             else:
#                 profile.investments[stock_name] = amount
#             profile.save()
#             messages.success(request, 'Investment successful!')
#         else:
#             messages.error(request, 'Insufficient coins!')
#         return redirect('profile')
#     return render(request, 'users/invest.html')
=======
        return redirect('login')
    return render(request, 'users/logout.html')

@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    investments = Investment.objects.filter(user=request.user)
    investments_with_values = []
    for investment in investments:
        current_value = investment.current_value()  #Calculate current value
        profit_or_loss = investment.profit_or_loss()  #Calculate profit or loss
        investments_with_values.append({
            'investment': investment,
            'current_value': current_value,
            'profit_or_loss': profit_or_loss
        })
    return render(request, 'users/profile.html', {
        'profile': profile,
        'investments_with_values': investments_with_values
    })

#API from AlphaVantage
api_key = "OWSXIPKVLK7APWRW"
>>>>>>> 7aacba6 (Implemented users feature)

@login_required
def invest_view(request):
    if request.method == 'POST':
<<<<<<< HEAD
        # Handle the investment logic here
        stock = request.POST.get('stock_name')
        amount = int(request.POST.get('amount'))
        
        profile = Profile.objects.get(user=request.user)
        if profile.coins >= amount:
            profile.coins -= amount
            profile.investments[stock] = profile.investments.get(stock, 0) + amount
            profile.save()
            return redirect('profile')
        else:
            messages.error(request, "Not enough coins to invest.")

    return render(request, 'users/invest.html')
=======
        form = InvestmentForm(request.POST)
        if form.is_valid():
            investment = form.save(commit=False)
            investment.user = request.user
            investment.shares = investment.amount_invested / get_stock_price(investment.stock_symbol)
            profile = Profile.objects.get(user=request.user)
            if profile.coins >= investment.amount_invested:
                investment.save()
                profile.coins -= investment.amount_invested
                profile.save()
                return redirect('profile')
            else:
                messages.error(request, "Not enough coins to invest.")
    else:
        form = InvestmentForm()
    return render(request, 'users/invest.html', {'form': form})
>>>>>>> 7aacba6 (Implemented users feature)
