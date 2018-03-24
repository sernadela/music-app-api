# MusicApp API 
(Django Rest Framework)

## Documentation

### Run

Create a virtualenv to isolate your package dependencies locally
```
virtualenv env
source env/bin/activate 
```

Install project requirements:
```
pip install -r requirements.txt
```

Create DB
```
python manage.py migrate
```

Run Django server at [http://localhost:8000](http://localhost:8000)
```
python manage.py runserver
```

### REST API

**List all songs available:**

```
GET /api/v1/songs/ HTTP/1.1
Content-Type: application/json
```

**Add Song:**

```
POST /api/v1/songs/ HTTP/1.1
Content-Type: application/json

{
	"title":"my_song_title",
	"artist":"my_song_artist",
	"album":"my_song_album"
}

```

**Remove Song:**

```
DELETE /api/v1/songs/<song_id> HTTP/1.1
```

**List all users available:**

```
GET /api/v1/users/ HTTP/1.1
Content-Type: application/json
```

**Add Song:**

```
POST /api/v1/users/ HTTP/1.1
Content-Type: application/json

{
	"username":"<my_username>",
	"email":"<my_email@mail.com>"
}

```

**Remove User:**

```
DELETE /api/v1/users/{user_id} HTTP/1.1
```

**Get User Favorite Songs:**

```
GET /api/v1/fav/user/<user_id> HTTP/1.1
Content-Type: application/json

```

**Add Favorite Song to User:**

```
POST /api/v1/fav/user/<user_id>/song HTTP/1.1
Content-Type: application/json

{
    "id": "<song_id>"
}

```

**Rm Favorite Song from User:**

```
DELETE /api/v1/fav/user/<user_id>/song/<song_id> HTTP/1.1
Content-Type: application/json

```
