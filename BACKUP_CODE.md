# rozne sposoby na renderowanie forms, ostatecznie zdecydowalem sie na prosta implementacje z django-crispy-bootstrap5 forms

## Rozne wersje:

1. z wlasnorecznie napisanym html form z wlasnymi labelami, inputami:

```
def new_topic(request):

    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']

        user = User.objects.first()

        topic = models.Topic.objects.create(
            name=name,
            description=desc,
            author=user
        )

        return redirect('forum:home')
    
    return render(request, 'forum/new_topic.django-html')

```

2. z ModelForm z podstawowym generowanym form .as_p
```
def new_topic_form(request):

    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        user = User.objects.first()

        if form.is_valid():
            # dodawanie samo 
            # topic = form.save()
            
            # tutaj dodawanie dodatkowych pol typu related
            topic = form.save(commit=False)
            topic.author = user
            topic.save()

            return redirect('forum:home')
    else:
        form = NewTopicForm()
    return render(request, 'forum/new_topic_form.django-html', {'form': form})
```

3. wersja z crispy - taka jak wyzej tylko inny html
4. same
