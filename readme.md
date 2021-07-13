# Identify and Rank Texas Hold'em Poker Hands

# CHANGES
# CHANGE2


Hello there! I’m glad you could join us. Although I’m not sure who you are, you’re presumably here
because you heard about the quantum supremacy experiment recently published by a collaboration
from Google, NASA Ames, UC Santa Barbara, and a host of other teams from around the world
[12]. You may have seen the articles declaring a “quantum supremacy breakthrough,” and had
some sense that something momentous had occurred. We’ve finally produced a quantum computer
that can outperform a classical computer! In fact, “outperform” is a bit of a misnomer here; since
the task completed by the quantum computer would take a state-of-the-art supercomputer about
10,000 years, it’s more accurate to say that a classical computer could never effectively match the
quantum compute


![](./Iman/giphy.gif)

<img src="./Iman/giphy.gif" width="100" height="100" />

![As shown here](./Iman/2021-07-11.png "Desktop")

|Name|Name|
|----|-----|
|<img src="./Iman/2021-07-11.png" width="100" height="100" />|<img src="./Iman/2021-07-11.png" width="100" height="100" />|


![photo](./Iman/2021-07-11.png)

This program reads the community cards and each player's hand. Then, the program identifies each hand and rank them according to the Texas Hold'em rules.

[![Little red ridning hood](http://i.imgur.com/7YTMFQp.png)](https://vimeo.com/3514904 "Little red riding hood - Click to Watch!")

## How to run

This program accepts data with two different methods. Because of that, it has two main (main.py and main_txt.py).
If you have text file use main_txt.py, otherwise main.py

If you enter a different format or duplicate a card, you will receive an error message.

### main_txt.py

This file reads a text file that  contains community and hand cards. The first line will contain the five community cards. Each line after that will have a player's name followed by their two cards.


First, you should create a text file with the following format:

```
KS AD 3H 7C TD
John 9H 7S
Sam AC KH
Becky JD QC
```
Then, put the file in the root of the project. After that run the program with this command:

```
python main_txt.py
```

It will ask you to enter the file name, press enter. 
After that the result will be shown as:

```
1 Becky Straight Ace
2 Sam Two Pair Ace King
3 John Pair 7
```
### main.py 

When you run this file, it will ask you to enter community cards and after that player's hands.

Run the program with this command:

```
python main.py
```
Then, it asks to enter community cards and after that player's hands.

Format of community cards:

```
KS AD 3H 7C TD
```
Format of player's hand:

```
John 9H 7S
```

As soon as you enter the first hand, you will be able to press "s" to stop the program and see the rank and evaluation.

### Prerequisites

To run this program you need Python 3.9

### Authors

* **Iman Hejazi** 

