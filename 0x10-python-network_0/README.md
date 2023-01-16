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
- [**Advanced Task**](#advanced-task)
	- [Task - 013](link_to_file)
	- [Task - 014](link_to_file)

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
