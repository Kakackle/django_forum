# Aplikacja wlasnych globalnych styli a biblioteki

Generalnie wiekszosc umozliwia, wiadomo, ale szczegolnie wrazliwe sa czesto na globalne zmiany wielkosci czlonki - wewnetrzne skalowanie kompletnie sie gubi, przewaznie teksty sa bardzo male


# Sposob na przesylanie form submit w django (wykonywanie funkcji) bez reloadu strony

Tzn, musisz skorzystac z Jscript, np z Jquery aby moc wykorzystac Ajax, ktory:
przy kliknieciu "submit" z form wysle post request do form ktore zaktualizuje dane i zwroci do strony

najwazniejsze / z czym bylo najwiecej problemow to odpowiednie przeslanie danych z form w htmlu do django, gdzie formy tworzone byly w for loopie

co oznaczalo, ze z kazdym trzeba powiazac unikalne wartosci, w tym wypadku ktorego postu dotyczy klikniety przycisk, ktory post ma zostac polubiony

zatem w html:
dodatkowo jako ukryte pola przekazywane moga byc inne dane jak slug postu do odczytania w Django z tresci requestu

ALE:

wlasciwie to chcemy reload
zeby zaktualizowalo stan wyswietlany...

brak reloadu zalatwia glownie 'e.preventDefault()'

html:

```
<form method="post" id="like-form">
                        {% csrf_token %}
                        <input type="hidden" name="post_slug" value="{{post.slug}}">
                        {% comment %} <a href="javascript:" class="function-link hover" data-postslug="{{post.slug}}" role=button>Like {{post.like_count}}</a> {% endcomment %}
                        <button type="submit" id="like_button" data-postslug="{{post.slug}}" class="likes function-link hover">Like {{post.like_count}}</button>
                    </form>
```

a w js:
```
<script
  src="https://code.jquery.com/jquery-3.7.0.min.js"
  integrity="sha256-2Pmvv0kuTBOenSvLm6bvfBSSHrUJ+3A7x6P5Ebd07/g="
  crossorigin="anonymous">
</script>

```

```
<script>
    {% comment %} let thread_slug = {{thread}} {% endcomment %}
    
    $(document).on('submit','#like-form',function(e){
        e.preventDefault();
        let topic_slug = "{{thread.topic.slug}}";
        let thread_slug = "{{thread.slug}}";
        // console.log(`target: ${e.target.getElementsByTagName('button').item(0).dataset.postslug}`);
        // let post_slug = $('input[name=post_slug]').val();
        // let post_slug = $(this).data('postslug');
        // let post_slug = e.target.dataset.postslug;
        let post_slug = e.target.getElementsByTagName('button').item(0).dataset.postslug;
        console.log(`post_slug: ${post_slug}`);
        
        $.ajax({
            type:'POST',
            url: `{% url 'forum:like_post' topic_slug=thread.topic.slug thread_slug=thread.slug post_slug=1234 %}`.replace(/1234/, post_slug.toString()),
            data:
            {
                'slug': post_slug,
                'csrfmiddlewaretoken': '{{csrf_token}}'
            },
            success:function(){
                  alert('Likes changed?');
                    }
            })
        });

</script>
```