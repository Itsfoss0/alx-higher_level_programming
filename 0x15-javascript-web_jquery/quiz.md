![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)
> Web Jquery Quizes

#### Question #0
In the following code snippet, does the selector called ('#my_header') access the HTML tag <header>:

(using `document.querySelector or $(...))`?

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header class="my_header"> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```
- [ ] Yes
- [X] No

#### Question #1
In the following code snippet, does the selector called `('#my_header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header class="my_header"> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul id="my_header">
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```
- [ ] Yes
- [X] No


#### Question #2
In the following code snippet, does the selector called `('header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```
* [X] Yes
* [ ] No

#### Question #3
In the following code snippet, does the selector called ```('#header')``` access the HTML tag ```<header>```:

(using `document.querySelector` or `$(...)`)?
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

* [ ] Yes
* [X] No

#### Question #4
In the following code snippet, does the selector called `('HeAdER')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```
* [X] Yes
* [ ] No

> ### Tips:
> Selectors are case insensitive

#### Question #5
How many HTML tags are present in the following HTML code?

    `<!DOCTYPE html>` is not an HTML tag
    `<head></head>` is considered one HTML tag.
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <ul>
        <li>Home</li>
        <li>Admission</li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```
* [ ] 13
* [ ] 11
* [X] 12
* [ ] 14

#### Question #6
How many HTML tags are present in the following HTML code?

    `<!DOCTYPE html>` is not an HTML tag
    `<head></head>` is considered one HTML tag.
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```
* [ ] 18
* [X] 15
* [ ] 16
* [ ] 20

#### Question #7
In the following code snippet, does the selector called `('#my_header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header id="my_header"> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

* [X] Yes
* [ ] No

#### Question #8
How many HTML tags are present in the following HTML code?

    `<!DOCTYPE html>` is not an HTML tag
    `<head></head>` is considered one HTML tag.
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```
* [X] 6
* [ ] 4
* [ ] 5
* [ ] 7

#### Question #9
In the following code snippet, does the selector called `('section.my_header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header class="my_header"> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```
* [X] No
* [ ] Yes

#### Question #10
In the following code snippet, does the selector called `('header.my_header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header class="my_header"> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```
* [X] Yes
* [ ] No

#### Question #11
In the following code snippet, does the selector called `('body header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```
* [X] Yes
* [ ] No

#### Question #12
In the following code snippet, does the selector called `('.my_header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header class="my_header"> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```
* [X] Yes
* [ ] No

#### Question #13
In the following code snippet, does the selector called `('.header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```
* [X] No
* [ ] Yes