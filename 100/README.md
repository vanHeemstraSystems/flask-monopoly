# 100 - Introduction

Flask monopoly is semestral project of [Krzysztof Welc](https://github.com/KrzysztofWelc) for web programming classes in year 2020/2021. It has been updated for 2024 by [Willem van Heemstra](https://github.com/wvanheemstra).

It is web service allowing user to play monopoly-like game in three modes:
- hot seats
- vs ai
- online agaist another player

### technologies used:
- html/scss/js
- python (flask, sqlAlchemy, etc...)
- web sockets

## 100 - How to go to the Home page

1) Browse to the website with the URL ending with (```/```).

2) **Note**: on most pages you can return to the Home Page by choosing **Home** from the navigation bar.

## 200 - How to Register a New User

1) From the Home page of the game (```/```), choose from the navigation bar the menu item **Register**.

2) On the Registration page (```/auth/register```), fill in the form providing:

- username
- email address
- password (2x)

Submit the form to sign up.

3) If successful, you will be redirected to the Home page (```/```) and a message will state: ```account created for [ username ]```. If the username or the email address are already registered, an error will be returned.

4) The number of registered users will now include you as a registered user.

5) Once registered you can now login.

## 300 - How to Login as a Registered User

1) From the Home page of the game (```/```), choose from the navigation bar the menu item **Login**.

2) On the Login page (```/auth/login```), fill in the form providing:

- email address
- password
- (Optional) remember me

Submit the form to login.

3) If successful, you will be redirected to the Home page (```/```) and a message will state: ```logged in```. If either the email address and/or the password are incorrect, a message will state ```error```.

4) Optionally, you can now logout by choosing from the navigation bar the menu item **Logout**.

5) Alternatively, you can either start a New game or Join an existing game.

## 400 - How to Logout as a Logged In User

1) From the Home page of the game (```/```), choose from the navigation bar the menu item **Logout**.

2) You will be logged out and redirected to the Home page (```/```).

## 500 - How to lookup the Profile of a Registered User

1) From the Home page of the game (```/```), choose from the navigation bar the menu item **[ username ]**.

2) You will be redirected to the Profile page (```auth/profile/[user id]```). It states your username and the pending games you are part of.

## 600 - How to start a New Game as a Logged In User

1) From the Home page of the game (```/```), choose from the navigation bar the menu item **New Game**.

2) You will be redirected to the start the Game's Menu page (```/menu```).

3) You can choose from one of three Game Modes:

- **Hot Seats Locally**: meaning you play with humans who are also playing locally (i.e. the button to progress is visible to all Players, taking turns).

- **Versus Computer**: meaning you play against a computer using Artificial Intelligence (i.e. the button to progress is visible only to the Player - Human or Computer - whose Turn it is, i.e. the Active Player).

- **Hot Seats Remotely:** meaning you play with humans who are playing over the Internet(i.e. the button to progress is visible only to the Online Player whose Turn it is, i.e. the Active Player).

4.A) Hot Seats Locally: See [How to Play a Hot Seats Locally Game?](#800---how-to-play-a-hot-seats-locally-game)

4.B) Versus Computer: See [How to Play a You Versus a Computer Game?](#900---how-to-play-a-you-versus-a-computer-game)

4.C) Hot Seats Remotely: See [How to Play a Hot Seats Remotely Game?](#1000---how-to-play-a-hot-seats-remotely-game)

## 700 - How to join an Existing Game as a Logged In User

1) From the Home page of the game (```/```), choose from the navigation bar the menu item **Join Game**.

2) You will be redirected to the join an Existing Game page (```/join_game```). 

3) Fill in the Join Code and submit the form with **Join**.

4) If the Join Code is **not** registered, you will be given a message: ```You cannot join this game```.

5) If the Join Code is registered, you will be redirected to ...

## 800 - How to play a Hot Seats Locally Game?

MORE

## 900 - How to play a You versus a Computer Game?

1) You will be have been redirected to the join an New or Existing Game page where you play against a computer (```/vs_ai```).

2) The Board will show all Fields (such as parking, [ cities ], and start).

3) You will be one of the Players. Each Player is given a number (e.g. 1) and a color (e.g. amber).

4) If you enter a City Field, you will be given the option to Buy, unless the City Field has already been bought. You can choose ```Yes``` or ```No```. If you decide to buy, the Field will be marked with your number (e.g. 1) and color (e.g. amber). **Note**: you can only buy if you have enough Money remaining versus the asking price of the City Field. If you do not have enough Money, you will not be asked to buy.

5) Click **Next Turn** if you want to continue the game.

6) As you are playing against a Computer, the Computer will move by its own choice, and buy a City Field is possible also by its own choice. You will see if a City Field has been bought by the Computer if it is marked by its number (e.g. 0) and color (e.g. red).

7) During the Game, the remaining Money of each Player (including the Computer) will be shown (e.g. Player 1: 3600).

8) Provided a Player steps on a City Field that belongs to another Player, (s)he has to pay an amount, depending on the presence of one or more Homes or a Hotel. The Money will be automatically taken out of her/his Account.

9) Who ever losses their Money first loses the Game. If all Players have lost their Money except for one (Human or Computer), the last Player with Money left wins the Game!

MORE

## 1000 - How to play a Hot Seats Remotely Game?

MORE

## 1100 - What is the Waiting Room?

When a Player choosieds to Join a Game, (s)he will have to wait in the Waiting Room until the Organizer allows the Player to play.

MORE

## 1200 - How to see Details of a City Field?

By clicking on a City Field, the details will be shown.

MORE