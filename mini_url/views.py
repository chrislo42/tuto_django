from django.shortcuts import render, redirect, get_object_or_404
from .models import MiniURL
from .forms import MiniURLForm
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

def miniurl_list(request):
    miniurls = MiniURL.objects.order_by('-access')
    return render(request, 'mini_url/miniurl_list.html', {'miniurls':miniurls})

@login_required
def miniurl_edit(request):
    if request.method == "POST":
        form = MiniURLForm(request.POST)
        if form.is_valid():
            myurl = form.save(commit=False)
            myurl.code = myurl.generer(6)
            myurl.save()
            return redirect('miniurl_list')
    else:
        form = MiniURLForm()
    return render(request, 'mini_url/miniurl_edit.html', {'form': form})

def miniurl_redir(request, code):
    miniurl = get_object_or_404(MiniURL, code=code)
    miniurl.access += 1
    miniurl.save()
    return redirect(miniurl.longUrl, permanent=False)

class URLUpdate(UpdateView):
    model = MiniURL
    template_name = 'mini_url/miniurl_edit.html'
    form_class = MiniURLForm
    success_url = reverse_lazy(miniurl_list)

class URLDelete(DeleteView):
    model = MiniURL
    context_object_name = "mini_url"
    template_name = 'mini_url/miniurl_del.html'
    success_url = reverse_lazy(miniurl_list)
