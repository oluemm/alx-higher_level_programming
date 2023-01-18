<h1 style="text-align: center;"> 0x11-Python-Network_1</h1>


## Project Overview

- [**Mandatory Task**](#mandatory-task)
	- [0. What's my status? #0](0-hbtn_status.py)
	- [1. Response header value #0](1-hbtn_header.py)
	- [2. POST an email #0](2-post_email.py)
	- [3. Error code #0](3-error_code.py)
	- [4. What's my status? #1](4-hbtn_status.py)
	- [5. Response header value #1](5-hbtn_header.py)
	- [6. POST an email #1](6-post_email.py)
	- [7. Error code #1](7-error_code.py)
	- [8. Search API](8-json_api.py)
	- [9. My GitHub!](10-my_github.py)
- [**Advanced Task**](#advanced-task)
	- [10. Time for an interview!](100-github_commits.py)

---



<h2 style="text-align: center;">Tasks</h2>

### Mandatory Task
#### 0. What's my status? #0

**Problem:** Write a Python script that fetches `https://alx-intranet.hbtn.io/status`

**Requirements:**
* You must use the package `urllib`
* You are not allowed to import any packages other than `urllib`
* The body of the response must be displayed like the following example (tabulation before `-`)
* You must use a `with` statement
```
imitor＠excalibur»/0x11-python-network_1(main)➜ ./0-hbtn_status.py | cat -e         					(↻ 205?)3.10.7
Body response:$
    - type:<class 'bytes'>$
    - content:b'OK'        $
    - utf8 content:OK$
```
- [x] *File:* [0-hbtn_status.py](0-hbtn_status.py)

---

#### 1. Response header value #0

**Problem:** Write a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.

**Requirements:**
* You must use the packages `urllib` and `sys`
* You are not allow to import packages other than `urllib` and sy`s
* The value of this variable is different for each request
* You don’t need to check arguments passed to the script (number or type)
* You must use a `with` statement

```
imitor＠excalibur»0x11-python-network_1(main)✗ ./1-hbtn_header.py https://alx-intranet.hbtn.io
5d72bae6-de97-4cd4-937d-ff3806edd7a6
imitor＠excalibur»0x11-python-network_1(main)➜ ./1-hbtn_header.py https://alx-intranet.hbtn.io
6e3f93a7-b987-40d2-880e-96aa6b2a8ca3
```
- [x] *File:* [1-hbtn_header.py](1-hbtn_header.py)


---

#### 2. POST an email #0

**Problem:** Write a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)

**Requirements:**
* The email must be sent in the `email` variable
* You must use the packages `urllib` and `sys`
* You are not allowed to import packages other than `urllib` and `sys`
* You don’t need to check arguments passed to the script (number or type)
* You must use the `with` statement

```
root@664b640ac343:/# ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
root@664b640ac343:/# 
```
- [x] *File:* [2-post_email.py](2-post_email.py)


---

#### 3. Error code #0

**Problem:** Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).

**Requirements:**
* You have to manage `urllib.error.HTTPError` exceptions and print: `Error code:` followed by the HTTP status code
* You must use the packages `urllib` and `sys`
* You are not allowed to import other packages than `urllib` and `sys`
* You don’t need to check arguments passed to the script (number or type)
* You must use the `with` statement
```
root@664b640ac343:/# ./3-error_code.py http://0.0.0.0:5000
Index
root@664b640ac343:/# ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
root@664b640ac343:/# ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
root@664b640ac343:/# ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
root@664b640ac343:/# ./3-error_code.py http://httpbin.org/status/501
Error code: 501
```
- [x] *File:* [3-error_code.py](3-error_code.py)


---

#### 4. What's my status? #1

**Problem:** lorem ipsum

**Requirements:**
* You must use the package `requests`
* You are not allow to import packages other than `requests`
* The body of the response must be display like the following example (tabulation before `-`)

```
imitor＠excalibur»0x11-python-network_1(main)➜ ./4-hbtn_status.py     
Body response:        
        - type: <class 'str'>            
        - content: OK
```
- [x] *File:* [4-hbtn_status.py](4-hbtn_status.py)


---

#### 5. Response header value #1

**Problem:** Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header

**Requirements:**
* You must use the packages `requests` and `sys`
* You are not allow to import other packages than `requests` and `sys`
* The value of this variable is different for each request
* You don’t need to check script arguments (number and type)
```
imitor＠excalibur»0x11-python-network_1(main)✗ ./5-hbtn_header.py https://alx-intranet.hbtn.io
c94bac9a-10d5-47b7-b6d6-fffc945494c2
imitor＠excalibur»0x11-python-network_1(main)➜ ./5-hbtn_header.py https://alx-intranet.hbtn.io
d6b3b27e-0f1e-4331-8551-901f83e8993a
```
- [x] *File:* [5-hbtn_header.py](5-hbtn_header.py)


---

#### 6. POST an email #1

**Problem:** Write a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response.

**Requirements:**
* The email must be sent in the variable `email`
* You must use the packages `requests` and `sys`
* You are not allowed to import packages other than `requests` and `sys`
* You don’t need to error check arguments passed to the script (number or type)
```
root@664b640ac343:/# ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
root@664b640ac343:/# ./6-post_email.py http://0.0.0.0:5000/post_email imitor@gmail.com
Your email is: imitor@gmail.com
```
- [x] *File:* [6-post_email.py](6-post_email.py)


---

#### 7. Error code #1


**Problem:** Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

**Requirements:**
* If the HTTP status code is greater than or equal to 400, print: `Error code:` followed by the value of the HTTP status code
* You must use the packages `requests` and `sys`
* You are not allowed to import packages other than `requests` and `sys`
* You don’t need to check arguments passed to the script (number or type)
```
root@664b640ac343:/# ./7-error_code.py http://0.0.0.0:5000
Index
root@664b640ac343:/# ./7-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
root@664b640ac343:/# ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
root@664b640ac343:/# ./7-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
root@664b640ac343:/#
```
- [x] *File:* [7-error_code.py](7-error_code.py)


---

#### 8. Search API

**Problem:** Write a Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.

**Requirements:**
* The letter must be sent in the variable `q`
* If no argument is given, set `q=""`
* If the response body is properly JSON formatted and not empty, display the `id` and `name` like this: `[<id>] <name>`
* Otherwise:
	* Display `Not a valid JSON` if the JSON is invalid
	* Display `No result` if the JSON is empty
* You must use the package `requests` and `sys`
* You are not allowed to import packages other than `requests` and `sys`
```
root@664b640ac343:/# ./8-json_api.py  as
[2024] asjctsgrfbxp
root@664b640ac343:/# ./8-json_api.py
No result
root@664b640ac343:/# ./8-json_api.py  aswwwwwwwwwwwwwwwwwwwwww
[9242] aswwwwwwwwwwwwwwwwwwwwwwgltwkxgcsz
root@664b640ac343:/# ./8-json_api.py 23
No result
```
- [x] *File:* [8-json_api.py](8-json_api.py)


---

#### 9. My GitHub!

**Problem:** Write a Python script that takes your GitHub credentials (username and password) and uses the `GitHub API` to display your `id`

**Requirements:**
* You must use `Basic Authentication` with a `personal access token as password` to access to your information (only `read:user` permission is needed)
* The first argument will be your `username`
* The second argument will be your `password` (in your case, a `personal access token as password`)
* You must use the package `requests` and `sys`
* You are not allowed to import packages other than `requests` and `sys`
* You don’t need to check arguments passed to the script (number or type)

```
guillaume@ubuntu:~/0x11$ ./10-my_github.py papamuziko cisfun
2531536
guillaume@ubuntu:~/0x11$ ./10-my_github.py papamuziko wrong_pwd
None
```
- [x] *File:* [10-my_github.py](10-my_github.py)


---
### Advanced Task

---
#### 10. Time for an interview!
**Problem:** The Holberton School staff evaluates candidates applying for a back-end position with multiple technical challenges, like this one:
```
Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
```
Write a Python script that takes 2 arguments in order to solve this challenge.

**Requirements:**
* The first argument will be the `repository name`
* The second argument will be the `owner name`
* You must use the packages `requests` and `sys`
* You are not allowed to import packages other than `requests` and `sys`
* You don’t need to check arguments passed to the script (number or type)
```
imitor＠excalibur»0x11-python-network_1(main)➜ ./100-github_commits.py alx-higher_level_programming fashemma007
e3cbaeb438ca0925be8bde0ae58df521fabfcb9e: Emmanuel Fasogba
f92b29905086e1dbd491e7b8e715045b2023b177: Emmanuel Fasogba
4cdaff0e538fc4512e69f17fe574affd0b6b95ac: Emmanuel Fasogba
71b1f9c13ef50d5fe700d14e084e8c0554ccaee7: Emmanuel Fasogba
cbbbd14074c81c307a18c773574e5da927ea92b9: Emmanuel Fasogba
98c7b46a77491138efa751d6314e4da5fe152e78: Emmanuel Fasogba
e12c2e28eefdf139a86194ec61ba7e1517fe1cdb: Emmanuel Fasogba
bb4462d1af3b0d1bc10e7ff843f3c0368eb4d78c: Emmanuel Fasogba
d6695767d7f76f3e3ec2b9bfb8e2332dc1a12411: Emmanuel Fasogba
ba0eb7ca7ca1fb80899f2071a55ff754d4f3bb4f: Emmanuel Fasogba
```
- [x] *File:* [100-github_commits.py](100-github_commits.py)

---

<h2 style="text-align: center;">Collaborative Author(s)</h2>

[**Emmanuel Fasogba**](https://www.linkedin.com/in/emmanuelofasogba/)
- GitHub - [fashemma007](https://github.com/fashemma007)
- Twitter - [@tz_emiwest](https://www.twitter.com/tz_emiwest)
