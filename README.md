# 🕹️ Desert Adventure Game CS50 Final Project

## Introduction

I built this Desert Adventure Game for my CS50 Final project for the course of CS50 Introduction to Computer Science. This Game was built in Python using Pygame library as a submission for my CS50 final project. The idea for this game was thought of by me when I learned about pygame looking for projects for the CS50 Introduction to Computer Science course. I wanted to create a simple game using a library called pygame which is from Python. This game keeps the player engaged until they go through all of the decisions and outcomes in the game. The main concept is straightforward to many people; you are an adventurer and you go traveling and there are many options to choose from some very good, some very bad or dangerous, and some not affecting you in any way, shape, or form. The project has not oly helped me explore pygame more but to dive deeper into what projects people can do with python's library pygame for 2D game development. And I also implemented many things like different npcs, custom fonts, sounds and music when playing, adventurer movement, and blitting stuff onto the screen.

## 🎯 Objectives

The primary objectives of this project were:

1. To design and implement a working 2D game using Python's game library known as pygame.
2. To get an understand of the game loop (two examples are event handling and updates)
3. Keep testing, debugging the game, and adding new stuff.
4. Add elements such as images, sounds, and fonts.
5. Create reusable parts of the game for any pygame project similar to this one. An example would be like font and text handling.

## ✨ Features

This story game includes many features, some I mentioned earlier in this file.
Engaging features:

- Player movement: Smooth control with Arrow Keys and WASD. This is a crucial part for every game.
- Sound and Music: I added some sound effects from .mp3 files and i just got these sound effects from different websites like pixabay. Pixabay is only one website that gave me these type of sound effects for my game
- Different ending outcomes: I put different endings in my game and the choices you make as you go through the game affect what ending you land upon. Some endings are good, while others are dangerous or bad.
-Sprites: I have my adventurer sprite, my dangrous oasis creature sprite, my caravan man sprite, and my camel sprite.

## 🎮Controls

The controls for my Adventure Game are designed to be very simple so that players can focus on the story and decisions being made rather than worrying about complicated input. I implemented both the **Arrow Keys** and the **WASD keys** for movement which is preferable on all types of modern games on pc.

- **Arrow Keys / WASD** -> Move the adventurer across the screen
- **R** -> Restart the game after you finished and got to one ending.
- **Return/Enter** -> Move from your Main screen that tells you all the controls and what to do to your first option screen tha lets you pick an option.

Adding more controls helps me learn more about pygame and its event handling system.

## ⚙️ Development Process
Ok so how i built this game is i created a file called game.py in my CS50 Final folder and before I talk about some thing I want to mention how I got my font, imagesin every scene, and my sounds. I dwnloaded them from different websites and my sprites (aka npcs), I drew all of them on a website called piskel it is a website where you can create your own sprites for various reasons including a game like this. My sprites were 
.gifs and my images were .webps and .pngs when I downloaded them. I started my python game by importing pygame and doing the pygame.locals import * is a python import statement that defines what variables and functions in our loops are to the python file. and then I put all the story data in a story dictionary. And then I initialized my pygame and I called the images, fonts, and sounds. And then in my main loop I called everything else. And then i called dt = clock.tick(60) / 1000 which makes it go 60 frames every 1000 milliseconds which is 60 fps for this game. And then I did pygame.display.flip() which updates the entire screen to show what has been drawn to the entire surface. And finally to end the entire game I called pygame.quit().

## 🚧 Challenges Faced 
One of the biggest challenges I have faced while doing this project was learning pygame and game development for the first time there was lots of things I didnt know how to do but I gave some time to learning some stuff and thats how i came up with this game.

## 🔮 Future Improvements
If I had more time I would have added:
- A proper pause menu
- A healthbar for the adventurer
- More branching to the story
- Objects player has to move through or to pick up

## ▶️ How to Run the Game on MacOS 
1. Make sure you have python3 installed: python3 --version
2. After that you need to have pip3 installed (Python's package installer) by typing:
pip3 --version

If Python or pip are not installed, you may need to install Python 3 from the official Python website or through a package manager like Homebrew (brew install python3).

Install Pygame: Use pip to install Pygame by running one of the following commands in your terminal:
3. Recommended: pip3 install pygame
Alternative (if the above does not work): python3 -m pip install pygame

4. Verify Installation: After the installation completes, you can verify it by opening a Python interactive shell in the terminal: python3

5. Then, within the Python shell, type: import pygame

If no error messages appear and you see "Hello from the pygame community," Pygame has been successfully installed. You can then exit the Python shell by typing exit().

## 🎥 Demo  
Here is a short demo of my project: [YouTube Link](https://youtu.be/mBotwlQGMa4)  

## 🙏 Acknowledgments  
- Thanks to the CS50 staff for this incredible course and the chance to build this project.  
- Thanks to **ChatGPT** for helping me brainstorm, debug, and structure parts of this project and its documentation.  

## 📂 Project Structure
- `CS50Final/` →Folder for the whole entire Project
- `game.py` → Main Python game file  
- `fonts/` → Folder with font used
- `images/` → Folder with sprites and images
- `sounds/` → Folder with all sounds used '.wav' and '.mp3'
- `README.md` → Documentation (this file)  
