from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        tit = request.POST.get('titulo')
        if len(Note.objects.all().filter(title=tit))==0:
            content = request.POST.get('detalhes')
            # Note.objects.create(title=title,content=content)
            note=Note()
            note.title=tit
            note.content=content
            note.save()
        else:
            note=Note.objects.get(title=tit)
            note.title=request.POST.get('titulo')
            note.content=request.POST.get('detalhes')
            note.save()
    

        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def delete(request,note_id):
    note_id=int(note_id)
    note=Note.objects.get(id=note_id)
    note.delete()
    return redirect('index')
    
# def update(request,note_id):
#     note_id=int(note_id)
#     note=Note.objects.get(id=note_id)
#     note.title=request.POST.get('titulo')
#     note.content=request.POST.get('detalhes')
#     note.save()
#     return redirect('index')
