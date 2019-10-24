from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from concepts.models import Block
from .forms import BlockForm
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
from link.models import Link
from django.template.defaulttags import register
from django.contrib.auth.decorators import login_required



def add_block(request):
    User = get_user_model()
    block_data = {}
    if request.method == 'POST':
        add_valid = request.POST.get('add_valid')
        if add_valid:
            # If we are only adding a new element
            block_data['title'] = request.POST.get('title')
            block_data['num'] = request.POST.get('num_block')
            block_data['x_pos'] = request.POST.get('x_pos')
            block_data['y_pos'] = request.POST.get('y_pos')
            if request.user.is_authenticated:
                block_data['creator'] = request.user.get_username()
            else:
                block_data['creator'] = 'Anonymous'
            form_block = BlockForm(block_data)
            print(form_block)
            block = form_block.save()
            block_data['id'] = block.id
            # Add block to list of users blocks
            user = User.objects.get(username=request.user.username)
            user.blocks.append(block_data['num'])
            user.save()
            block_data['links'] = []
            if block.links:
                block_data['links'] = block.links
            return JsonResponse(block_data)

def update_block(request):
    block_data = {}
    if request.method == 'POST':
        update_valid = request.POST.get('update_valid')
        if update_valid:
            block_num = request.POST.get('num_block')
            block_id = request.POST.get('global_block_id')
            block = Block.objects.get(id=block_id)
            block_data['title'] = request.POST.get('title')
            block_data['num'] = block_num
            block.update(block_data)
            return JsonResponse(block_data)

def delete_block(request):
    User = get_user_model()
    if request.method == 'POST':
        delete_valid = request.POST.get('delete_valid')  # block delete
        if delete_valid:
            block_id = request.POST.get('block_id')
            print('Block id:' + block_id)
            block = Block.objects.get(id=block_id)
            # if request.user.is_authenticated:
            user = User.objects.get(username=request.user.username)
            # user.blocks.remove(request.POST.get('user_block_id'))
            block.delete()
            # Delete related links
            links = []
            try:
                links_start = Link.objects.get(starting_block=block_id)
                links_start = [links_start]
            except:
                links_start = Link.objects.filter(starting_block=block_id)
            #If there are any links for which this block is a starting block
            for link in links_start:
                links.append(link.id)
                # delete link from user
                if link.id in user.links:
                    user.links.remove(link.id)
                # delete link for corresponding ending block
                ending_block_corr = Block.objects.get(id=link.ending_block)
               # ending_block_corr.links.remove(link.id)
                ending_block_corr.save()
                # delete link
                link.delete()
            #except:
            #    print('Not a starting block')
            try:
                links_end = Link.objects.get(ending_block=block_id)
                links_end = [links_end]
            except:
                links_end = Link.objects.filter(ending_block=block_id)
            for link in links_end:
                links.append(link.id)
                if link.id in user.links:
                    user.links.remove(link.id)
                # delete link for corresponding starting block
                starting_block_corr = Block.objects.get(id=link.starting_block)
                print(starting_block_corr.links)
                #starting_block_corr.links.remove(link.id)
                starting_block_corr.save()
                link.delete()

            user.save()
            print(links)
            return JsonResponse({'links': links})

def drag_function(request):
    if request.method == 'POST':
        drag_valid = request.POST.get('drag_valid')
        if drag_valid:
            ids = []
            names = []
            starting_x_ = []
            ending_x_ = []
            starting_y_ = []
            ending_y_ = []
            style_ = []
            width_ = []
            starting_block_ = []
            ending_block_ = []
            #Save eand update block position
            block_id = request.POST.get('block_id')
            if Block.objects.get(id=block_id):
                block = Block.objects.get(id=block_id)
                block.x_pos = float(request.POST.get('x_pos')[:-2])
                block.y_pos = float(request.POST.get('y_pos')[:-2])+0.25*float(request.POST.get('drag_height'))
                block.save()
                #Change connected link information
                link_ids = block.links
                #Get block x and y
                for link_id in link_ids:
                    print(link_id)
                    link = Link.objects.get(id=link_id)
                    if str(block_id) == str(link.starting_block): #Is it the starting block? using global numbers
                        link.start_x = block.x_pos
                        link.start_y = block.y_pos
                    else: #Or the ending block...
                        link.end_x= block.x_pos
                        link.end_y = block.y_pos
                    link.save()
                    #update links connected to dragged block
                    ids.append(link.id)
                    starting_x_.append(link.start_x)
                    starting_y_.append(link.start_y)
                    ending_x_.append(link.end_x)
                    ending_y_.append(link.end_y)
                    starting_block_.append(link.starting_block)
                    ending_block_.append(link.ending_block)
            return JsonResponse({'id':ids,'start_x':starting_x_,'start_y':starting_y_,'end_x':ending_x_,'end_y':ending_y_,'starting_block':starting_block_,'ending_block':ending_block_})

