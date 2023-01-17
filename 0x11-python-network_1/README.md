<h1 style="text-align: center;"> 0x11-Python-Network_1</h1>


## Project Overview

- [**Mandatory Task**](#mandatory-task)
	- [0. What's my status? #0](0-hbtn_status.py)
	- [1. Response header value #0](1-hbtn_header.py)
	- [2. POST an email #0](2-post_email.py)
	- [3. Error code #0](3-error_code.py)
	- []()
	- []()
	- []()
	- []()
	- []()
	- []()
- [**Advanced Task**](#advanced-task)
	- [Task - 013](link_to_file)
	- [Task - 014](link_to_file)

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

#### Task

**Problem:** lorem ipsum

**Requirements:**
* lorem ipsum
* lorem ipsum

```
code sample
```
- [ ] *File:* [Task 1](link_to_file)


---

#### Task

**Problem:** lorem ipsum

**Requirements:**
* lorem ipsum
* lorem ipsum

```
code sample
```
- [ ] *File:* [Task 1](link_to_file)


---

#### Task

**Problem:** lorem ipsum

**Requirements:**
* lorem ipsum
* lorem ipsum

```
code sample
```
- [ ] *File:* [Task 1](link_to_file)


---

#### Task

**Problem:** lorem ipsum

**Requirements:**
* lorem ipsum
* lorem ipsum

```
code sample
```
- [ ] *File:* [Task 1](link_to_file)


---

#### Task

**Problem:** lorem ipsum

**Requirements:**
* lorem ipsum
* lorem ipsum

```
code sample
```
- [ ] *File:* [Task 1](link_to_file)


---

#### Task

**Problem:** lorem ipsum

**Requirements:**
* lorem ipsum
* lorem ipsum

```
code sample
```
- [ ] *File:* [Task 1](link_to_file)


---
### Advanced Task

---
#### Task - 013
**Problem:** lorem ipsum

**Requirements:**
* lorem ipsum
* lorem ipsum

```
code sample
```
- [ ] *File:* [Task 1](link_to_file)

---

#### Task - 014

**Problem:** lorem ipsum

**Requirements:**
* lorem ipsum
* lorem ipsum

```
code sample
```
- [ ] *File:* [Task 1](link_to_file)

---

<h2 style="text-align: center;">Collaborative Author(s)</h2>

[**Emmanuel Fasogba**](https://www.linkedin.com/in/emmanuelofasogba/)
- GitHub - [fashemma007](https://github.com/fashemma007)
- Twitter - [@tz_emiwest](https://www.twitter.com/tz_emiwest)
