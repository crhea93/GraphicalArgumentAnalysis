from concepts.models import Block
from django.contrib.auth import get_user_model
from django.http import  JsonResponse
from link.models import Link
from link.forms import LinkForm

def add_link(request):
    User = get_user_model()
    link_data = {}
    if request.method == 'POST':
        link_valid = request.POST.get('link_valid')
        if link_valid:
            # If we are only adding a new element
            link_data['starting_block'] = request.POST.get('start_global_id')
            link_data['ending_block'] = request.POST.get('end_global_id')
            # Check if a link with these blocks already exists. If so, then delete
            links_already = Link.objects.filter(starting_block=request.POST.get('starting_block')
                                                ,ending_block=request.POST.get('ending_block'))
            link_data['already'] = False  # Is there already a link?
            if links_already:
                link_data['already'] = True
                links_already.delete()

            if request.user.is_authenticated:
                link_data['creator'] = request.user.get_username()
            else:
                link_data['creator'] = 'Anonymous'
            form_link = LinkForm(link_data)
            link = form_link.save()
            #link_data['name'] = link.id
            link_data['num_link'] = link.id
            link_data['id'] = link.id
            user = User.objects.get(username=request.user.username)
            user.links.append(link.id)
            user.save()
            # Add lines to blocks
            start_block = Block.objects.get(id=request.POST.get('start_global_id'))
            start_block.links.append(link.id)
            start_block.save()
            end_block = Block.objects.get(id=request.POST.get('end_global_id'))
            end_block.links.append(link.id)
            end_block.save()
            # Now add block info to the link...
            link.start_x = start_block.x_pos
            link.start_y = start_block.y_pos
            link.end_x = end_block.x_pos
            link.end_y = end_block.y_pos
            link.save()
            return JsonResponse(link_data)

def update_link(request):
    link_data = {}
    if request.method == 'POST':
        print(request.POST.get("link_id"))
        link = Link.objects.get(id=request.POST.get("link_id"))
        link_data['warrant'] = bool_trans(request.POST.get('warrant'))
        print(link_data['warrant'])
        link.update(link_data)
        # Get all info to pass
        link_data['start_x'] = link.start_x; link_data['start_y'] = link.start_y
        link_data['end_x'] = link.end_x; link_data['end_y'] = link.end_y
        link_data['id'] = link.id
        return JsonResponse(link_data)

def delete_link(request):
    if request.method == 'POST':
        print(request.POST.get('link_id'))
        link_delete_valid = request.POST.get('link_delete_valid')
        if link_delete_valid:
            link = Link.objects.get(id=request.POST.get('link_id'))
            if request.user.is_authenticated:
                #Delete link from block list
                print(link.id)
                start_block = Block.objects.get(id=link.starting_block)
                print(start_block.links)
                start_block.links.remove(str(link.id))
                start_block.save()
                end_block = Block.objects.get(id=link.ending_block)
                end_block.links.remove(str(link.id))
                end_block.save()
                #Delete Link
                link.delete()
            return JsonResponse({})


def bool_trans(bool_val):
    if bool_val == 'true':
        bool_val = True
    else:
        bool_val = False
    return bool_val