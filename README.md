# Projekt solo Django - forum

aktualnie utknalem na generowaniu breadcrumbow dynamicznie poprzez include template do ktorego przekzywane sa nazwy breadcrumbow i linki, jedynie kwestia jest w jaki sposob przekazac odpowiednio link, bo jak jest prosty po name typu 'about' to mozna po prostu wsadzic 'about', ale jak jest cos typu 'topic' topic_slug czyli tak jak sie podaje argumenty do url to juz pojawily sie problemy jak to sformatowac by moc przekazac przez context, ale raczej da rade tylko kwestia czasu

silnie korzystane z oficjalnego tut django

i projektu z pulpitu z Udemy, bo ma wszystko prawie


i tam gdzies w historii masz part 1-7 tutoriala innego zewnetrznego


### + Docker
1. Listing available containers `docker ps`
2. Enter container system `docker exec -it {id} bash`
3. Rebuild container `docker-compose build {container name, eg. 'web'}` or just `docker-compose build`
OR, better yet, if changes were made: `docker-compose up --build` with optionally `--build {container name eg. weg}`
4. Launch container `docker-compose up`

extra:
clear docker cache `docker builder prune`


### Testing with coverage in nice html format

1. change database to local sqlite from postgres hosted in container
2. `python manage.py migrate`
3. `coverage run manage.py test`
4. `coverage html`


# Style, linting

Flake8 config in config.cfg

run `flake8`