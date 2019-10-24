from django.shortcuts import render,redirect
from users.forms import CustomUserCreationForm
from django.contrib.auth import  authenticate
from concepts.models import Block
from concepts.forms import BlockForm
from link.models import Link
from link.forms import LinkForm
from django.contrib.auth import get_user_model




def login(request):
    return render(request, "registration/login.html")

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, "signup.html",{'form':form})

def clear_CAM(request):
    User = get_user_model()
    block = Block()
    form_block = BlockForm()
    form_link = LinkForm()
    link = Link()
    block_data = {}
    clear_cam_valid = request.POST.get('clear_cam_valid')  # clear cam
    if clear_cam_valid:
        # clear blocks associated with user
        blocks = Block.objects.filter(creator=request.user.username)
        for block in blocks:
            block.delete()
        # clear links associated with user
        links = Link.objects.filter(creator=request.user.username)
        for link in links:
            link.delete()
        # clear user blocks and links
        user = User.objects.get(username=request.user.username)
        user.blocks = []
        user.links = []
        user.save()
        content = {
            'user': user,
            'block': block,
            'form_block': form_block,
            'new_block': block_data,
            'link': link,
            'form_link': form_link
        }
        return render(request, 'index.html', content)

def save_CAM(request):
    save_cam_valid = request.POST.get('save_cam_valid')  # save cam
    if save_cam_valid:
        blocks = request.POST.getList('blocks[]')
        blocks_x = request.POST.getList('blocks_x[]')
        blocks_y = request.POST.getList('blocks_y[]')