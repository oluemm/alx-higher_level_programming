<h1 style="text-align: center;">0x10-Python-Network_0</h1>

## Learning Objectives
* What a URL is
* What HTTP is
* How to read a URL
* The scheme for a HTTP URL
* What a domain name is
* What a sub-domain is
* How to define a port number in a URL
* What a query string is
* What an HTTP request is
* What an HTTP response is
* What HTTP headers are
* What the HTTP message body is
* What an HTTP request method is
* What an HTTP response status code is
* What an HTTP Cookie is
* How to make a request with cURL
* What happens when you type google.com in your browser (Application level)

## Resources
* [HTTP, Request & Response](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html)
* [HTTP Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)


## Project Overview

- [**Mandatory Task**](#mandatory-task)
	- [0. cURL body size](0-body_size.sh)
	- [1. cURL to the end](1-body.sh)
	- [2. cURL Method](2-delete.sh)
	- [3. cURL only methods](3-methods.sh)
	- [4. cURL headers](4-header.sh)
	- [5. cURL POST parameters](5-post_params.sh)
	- [6. Find a peak](6-peak.py)
- [**Advanced Task**](#advanced-task)
	- [7. Only status code](100-status_code.sh)
	- [8. cURL a JSON file](101-post_json.sh)
	- [9. Catch me if you can!](102-catch_me.sh)

---



<h2 style="text-align: center;">Tasks</h2>

### Mandatory Task
#### 0. cURL body size

**Problem:** Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

**Requirements:**
* The size must be displayed in bytes
* You have to use `curl`
Please test your script in the sandbox provided, using the web server running on port 5000
```
root@c74915c52729:/# curl -s -I 0.0.0.0:5000 | awk '/^Content-Length/ { print $2 }'
10
root@c74915c52729:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
```
- [x] *File:* [Task 0](0-body_size.sh)

---

#### 1. cURL to the end

**Problem:** Write a Bash script that takes in a URL, sends a `GET` request to the URL, and displays the body of the response

**Requirements:**
* Display only body of a `200` status code response
* You have to use curl
```
root@c74915c52729:/# ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
root@c74915c52729:/#
```
- [x] *File:* [1-body.sh](1-body.sh)

---

#### 2. cURL Method

**Problem:** Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

**Requirements:**
* You have to use `curl`
* Please test your script in the sandbox provided, using the web server running on port 5000

```
root@c74915c52729:/# ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
root@c74915c52729:/#
```
- [x] *File:* [2-delete.sh](2-delete.sh)

---

#### 3. cURL only methods

**Problem:** Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

**Requirements:**
* You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000

```
root@c74915c52729:/# ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
root@c74915c52729:/#
```
- [x] *File:* [3-methods.sh](3-methods.sh)

---

#### 4. cURL headers

**Problem:** Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response

**Requirements:**
* A header variable `X-School-User-Id` must be sent with the value `98`
* You have to use `curl`

```
root@c74915c52729:/# ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello School!
root@c74915c52729:/# 
```
- [x] *File:* [4-header.sh](4-header.sh)

---

#### 5. cURL POST parameters

**Problem:** Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response.

**Requirements:**
* A variable `email` must be sent with the value `test@gmail.com`
* A variable `subject` must be sent with the value `I will always be here for PLD`
* You have to use `curl`
```
root@c74915c52729:/# ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: test@gmail.com
    subject: I will always be here for PLD
root@c74915c52729:/# 
```
- [x] *File:* [5-post_params.sh](5-post_params.sh)

---

#### 6. Find a peak

**Problem:** Write a function that finds a **peak** in a list of unsorted integers

**Requirements:**
* Prototype: `def find_peak(list_of_integers):`
* You are not allowed to import any module
* Your algorithm must have the lowest complexity (hint: you don’t need to go through all numbers to find a peak)
* `6-peak.py` must contain the function
* `6-peak.txt` must contain the complexity of your algorithm: `O(log(n))`,` O(n)`, `O(nlog(n))` or `O(n2)`
* **Note**: there may be more than one peak in the list

```
root@c74915c52729:/0x10$ cat 6-main.py
#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))

root@c74915c52729:/0x10$ ./6-main.py
6
3
2
None
2
4
root@c74915c52729:/0x10$ wc -l 6-peak.txt 
2 6-peak.txt
root@c74915c52729:/0x10$ 
```
- [ ] *File:* [6-peak.py](6-peak.py)

---

### Advanced Task

---
#### 7. Only status code
**Problem:** lorem ipsum

**Requirements:**
* lorem ipsum
* lorem ipsum

```
code sample
```
- [ ] *File:* [100-status_code.sh](100-status_code.sh)

---

#### 8. cURL a JSON file

**Problem:** lorem ipsum

**Requirements:**
* lorem ipsum
* lorem ipsum

```
code sample
```
- [ ] *File:* [101-post_json.sh](101-post_json.sh)

---

#### 9. Catch me if you can!

**Problem:** lorem ipsum

**Requirements:**
* lorem ipsum
* lorem ipsum

```
code sample
```
- [ ] *File:* [102-catch_me.sh](102-catch_me.sh)

---

<h2 style="text-align: center;">Collaborative Author(s)</h2>

[**Emmanuel Fasogba**](https://www.linkedin.com/in/emmanuelofasogba/)
- GitHub - [fashemma007](https://github.com/fashemma007)
- Twitter - [@tz_emiwest](https://www.twitter.com/tz_emiwest)
