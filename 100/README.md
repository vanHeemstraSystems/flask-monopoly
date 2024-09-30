# 100 - Introduction

## 100 - Origin

Flask monopoly is semestral project of [Krzysztof Welc](https://github.com/KrzysztofWelc) for web programming classes in year 2020/2021. 

It is web service allowing user to play monopoly-like game in three modes:
- hot seats
- vs ai
- online agaist another player

## technologies used:
- html/scss/js
- python (flask, sqlAlchemy, etc...)
- web sockets

## 200 - How to Register a New User

1) From the Home page of the game (```/```), choose from the navigation bar the menu item **Register**.

2) On the Registration page (```/auth/register```), fill in the form providing:

- username
- email address
- password (2x)

Submit the form to sign up.

3) If successful, you will be redirected to the Home page (```/```) and a message will state: ```account created for [ username ]```. If the username or the email address are already registered, an error will be returned.

4) The number of registered user will now include you as a registered user.

5) Once registered you can now login.

## 300 - How to Login as a Registered User

MORE