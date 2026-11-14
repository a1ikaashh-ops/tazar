from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Challenge, UserChallenge, Team

def challenges_list(request):
    challenges = Challenge.objects.all()
    return render(request, 'challenges/list.html', {'challenges': challenges})

def challenge_detail(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    return render(request, 'challenges/detail.html', {'challenge': challenge})

@login_required
def take_challenge(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    user_challenge, created = UserChallenge.objects.get_or_create(
        user=request.user,
        challenge=challenge
    )
    return render(request, 'challenges/detail.html', {
        'challenge': challenge,
        'user_challenge': user_challenge
    })

@login_required
def teams_list(request):
    teams = Team.objects.all()
    return render(request, 'challenges/teams.html', {'teams': teams})

@login_required
def team_detail(request, pk):
    from django.shortcuts import get_object_or_404
    team = get_object_or_404(Team, pk=pk)
    return render(request, 'challenges/team_detail.html', {'team': team})

@login_required
def teams_list(request):
    teams = Team.objects.all()
    return render(request, 'challenges/teams.html', {'teams': teams})

@login_required
def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    return render(request, 'challenges/team_detail.html', {'team': team})

@login_required
def create_team(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        team = Team.objects.create(
            name=name,
            description=description,
            created_by=request.user
        )
        team.members.add(request.user)
        return redirect('team_detail', pk=team.pk)
    return render(request, 'challenges/create_team.html')

@login_required
def join_team(request, pk):
    team = get_object_or_404(Team, pk=pk)
    team.members.add(request.user)
    return redirect('team_detail', pk=team.pk)

@login_required
def leave_team(request, pk):
    team = get_object_or_404(Team, pk=pk)
    team.members.remove(request.user)
    return redirect('teams_list')

@login_required
def delete_team(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if team.created_by == request.user:
        team.delete()
    return redirect('teams')

@login_required
def add_member(request, pk):
    team = get_object_or_404(Team, pk=pk, created_by=request.user)
    if request.method == 'POST':
        from django.contrib.auth import get_user_model
        from django.contrib import messages
        User = get_user_model()
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            team.members.add(user)
            messages.success(request, f'✅ {username} добавлен в команду!')
        except User.DoesNotExist:
            messages.error(request, f'❌ Пользователь "{username}" не найден!')
    return redirect('team_detail', pk=team.pk)

@login_required
def remove_member(request, pk, user_pk):
    team = get_object_or_404(Team, pk=pk, created_by=request.user)
    from django.contrib.auth import get_user_model
    User = get_user_model()
    user = get_object_or_404(User, pk=user_pk)
    if user != team.created_by:
        team.members.remove(user)
    return redirect('team_detail', pk=team.pk)
@login_required
def join_team(request, pk):
    from django.shortcuts import get_object_or_404
    team = get_object_or_404(Team, pk=pk)
    team.members.add(request.user)
    return redirect('team_detail', pk=team.pk)

@login_required
def leave_team(request, pk):
    from django.shortcuts import get_object_or_404
    team = get_object_or_404(Team, pk=pk)
    team.members.remove(request.user)
    return redirect('teams_list')