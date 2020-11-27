from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from pets.forms.comment_form import CommentForm
from pets.forms.forms import CreatePetForm
from pets.models import Pet, Like, Comment


def pets_index(request):
    context = {
        'pets': Pet.objects.all(),
    }
    return render(request, 'pet_list.html', context)


@login_required
def pets_details(request, pk):
    pet_obj = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet_obj,
            'form': CommentForm(),
            'permissions': request.user == pet_obj.user.user,
            'like_comment_permissions': request.user != pet_obj.user.user,
            'has_liked': pet_obj.like_set.filter(user_id=request.user.userprofile.id).exists()
        }
        return render(request, 'pet_detail.html', context)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = Comment(comment=form.cleaned_data['comment'])
        comment.pet = pet_obj
        comment.user = request.user.userprofile
        comment.save()
        return redirect('pets details', pet_obj.pk)
    context = {
        'pet': pet_obj,
        'form': form,
    }
    return render(request, 'pet_detail.html', context)


@login_required
def pets_likes(request, pk):
    like = Like.objects.filter(user_id=request.user.userprofile.id, pet_id=pk).first()
    if like:
        like.delete()
    else:
        pet_obj = Pet.objects.get(pk=pk)
        #zakachai kum user, a ne user profile
        like = Like(user=request.user.userprofile)
        like.pet = pet_obj
        like.save()
    return redirect('pets details', pk)


@login_required
def pets_edit(request, pk):
    pet_obj = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        form = CreatePetForm(instance=pet_obj)
        context = {
            'form': form,
            'pet': pet_obj,
        }
        return render(request, 'pet_edit.html', context)
    form = CreatePetForm(request.POST, instance=pet_obj)
    if form.is_valid():
        form.save()
        return redirect('pets details', pet_obj.pk)
    context = {
        'form': form,
        'pet': pet_obj,
    }
    return render(request, 'pet_edit.html', context)


@login_required
def pets_delete(request, pk):
    pet_obj = Pet.objects.get(pk=pk)
    if pet_obj.user.user != request.user:
        pass
    if request.method == 'GET':
        context = {
            'pet': pet_obj,
        }
        return render(request, 'pet_delete.html', context)
    pet_obj.delete()
    return redirect('pets index')


@login_required
def pets_create(request):
    if request.method == 'GET':
        context = {
            'form': CreatePetForm(),
        }
        return render(request, 'pet_create.html', context)
    form = CreatePetForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('pets index')
    context = {
        'form': form,
        'pet': Pet(),
    }
    return render(request, 'pet_create.html', context)
