from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from item.models import Item

@login_required
def Index(request):
    items = Item.objects.filter(created_by=request.user)  

    return render(request, 'dashboard/Index.html', {
    'items': items,
})



