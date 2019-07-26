When you sign up for an account somewhere, some websites do not actually store your password in their databases.  Instead, they will transform your password into something else using a cryptographic hashing algorithm.

After the password is transformed, it is then called a *password hash*.  Whenever you try to login, the website will transform the password you tried using the same hashing algorithm and simply see if the password hashes are the same.

-----

Create the function that converts a given string into an `md5` hash.  The return value should be encoded in `hexadecimal`.

You will need to use the [NodeJS Crypto Module](http://nodejs.org/api/crypto.html) or [libcrypto](https://www.openssl.org/docs/man1.1.1/man3/MD5_Init.html) for the C and NASM versions.

###Code Examples
```javascript
passHash('password')
  //--> '5f4dcc3b5aa765d61d8327deb882cf99'

passHash('abc123')
  //--> 'e99a18c428cb38d5f260853678922e03'
```
```coffeescript
passHash "password"
    #--> '5f4dcc3b5aa765d61d8327deb882cf99'
passHash "abc123"
    #--> 'e99a18c428cb38d5f260853678922e03'
```
```c
passwd_hash("password")
    /* --> "5f4dcc3b5aa765d61d8327deb882cf99" */
passwd_hash("abc123")
    /* --> "e99a18c428cb38d5f260853678922e03" */
```
```nasm
.passwd:  db  "password",0h0
.abc123:  db  "abc123",0h0

mov rdi, .passwd
call passwd_hash    ; RAX <-- "5f4dcc3b5aa765d61d8327deb882cf99"
 
mov rdi, .abc123
call passwd_hash    ; RAX <-- "e99a18c428cb38d5f260853678922e03"
```
If you want to externally test a string, [look at this website](http://www.md5hasher.net/).

-----

If you are completely lost, I recommend you check out my previous [Introduction to NodeJS](http://www.codewars.com/kata/541db50c259d9c55c00007b9).

As a side note, `md5` can be exploited, so never use it for anything secure.  The reason I used it in this kata is simply because it is a very common hashing algorithm and many people will recognize the name.