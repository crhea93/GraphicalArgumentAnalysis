from django.shortcuts import render
from concepts.models import Block
from link.models import Link

# Create your views here.


def index(request):
    if request.method == 'POST':
        print('nope!')
    else: #request.method = "GET"
        user = request.user
        blocks = Block.objects.filter(creator=user.username)
        blocks_ = []
        for block in blocks:
            blocks_.append(block)
        lines = Link.objects.filter(creator=user.username)
        lines_ = []
        for line in lines:
            lines_.append(line)
        content = {
            'user': user,
            'existing_blocks': blocks_,
            'existing_lines': lines_
        }
        return render(request, 'index.html', content)
