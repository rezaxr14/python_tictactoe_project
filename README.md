# Awesome Graphical Tic-Tac-Toe Game

#### Video Demo: [https://youtu.be/otDqchy0o4s](https://youtu.be/otDqchy0o4s)

This is an implementation of the classic Tic-Tac-Toe game with a graphical user interface built using **Python** and **Tkinter**. Challenge a friend and see who can get three in a row first!

***

## Features

* **Classic Gameplay**: Enjoy the timeless fun of Tic-Tac-Toe.
* **Interactive UI**: A user-friendly graphical interface that's easy to navigate.
* **Visual Feedback**: The game clearly indicates the winner or a draw with winning images.
* **Restart Option**: Instantly start a new game at any time by clicking a button or clicking anywhere on the screen after a game ends.
* **Customizable Background**: Personalize your gaming experience by switching between two different background images using a dedicated button.

***

## Installation

Getting the game up and running is simple.

1.  Make sure you have **Python** installed on your system.
2.  Clone this repository or download the source code.
    ```bash
    git clone [https://github.com/rezaxr14/python_tictactoe_project.git](https://github.com/rezaxr14/python_tictactoe_project.git)
    ```
3.  Navigate to the project directory and run the following command to install the necessary libraries from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

***

## How to Play

1.  Run the `project.py` script from your terminal:
    ```bash
    python project.py
    ```
2.  Click on any empty tile to place your "X" or "O". The game alternates between "X" and "O" players.
3.  The game automatically checks for winning combinations and will display the winner when a player gets three in a row.
4.  If all tiles are filled and no one has won, a "no winner" image is displayed.
5.  After a game is over, you can **restart** it by clicking anywhere on the screen. You can also use the **restart button** at any time.
6.  Use the **change background button** to toggle between the two available background images.

***

## Project Structure

The project is organized into the following files and directories:
```
├── project.py
├── Constants.py
├── test_project.py
├── requirements.txt
└── resources/
    ├── bg.png
    ├── bp.png
    ├── change.png
    ├── def.png
    ├── icon.ico
    ├── NO_WINNER_IMG.jpg
    ├── o.png
    ├── O_WIN.png
    ├── restart.png
    ├── x.png
    └── X_WIN.png
```
***

## Code Overview

### `project.py`

This is the main file that runs the game. It uses several libraries:
* `itertools` for creating combinations of moves.
* `tkinter` for the game window (`Tk`), drawing the grid (`Canvas`), and styling text (`font`).
* `PIL` (Pillow) for handling and displaying images.
* `Constants` to import game-specific variables like image paths.

The file contains the **`Ticktacktoe` class**, which extends the `Tk` class and manages all the game logic and aesthetics.

* **`Ticktacktoe` Class**: Initializes the game window, sets up game tiles, and handles all player moves. It's responsible for checking for winning combinations, displaying the winner, and providing options to restart the game or change the background image.
* **`initialize_coordination` Method**: This method sets up the game tiles on the canvas. It calculates the coordinates for each of the 9 cells and binds a mouse click event to each one to register player moves.
* **`clicked` Method**: This function handles the logic when a player clicks on a cell. It determines whose turn it is, updates the cell with the correct "X" or "O" image, and keeps track of which cells have already been clicked. After a move, it calls `check_win`.
* **`check_win` Method**: This method checks if any player has won the game. It compares the current moves against a list of predefined winning combinations. If a winner is found, it displays the appropriate winner's image and a message, allowing players to start a new game.
* **`alternate_background` Method**: This function is triggered by the "Change Background" button and alternates the window's background image between two different styles.

### `Constants.py`

This file stores all the constant values used in the game. This includes:
* `WIDTH` and `HEIGHT` for the game window dimensions.
* File paths for all images, such as "x.png," "o.png," the background images ("bg.png," "bp.png"), and the winning images ("X_WIN.png," "O_WIN.png").
* A list of simplified winning combinations (`WIN`).

### `test_project.py`

This file contains the tests for the game to ensure that everything is working as expected. The test functions check various aspects of the game, such as winning combinations, the background change feature, and the restart logic, ensuring the correctness of the game's functionality.

***

## Running Tests

To run the built-in test suite, execute the following command in your terminal:

```bash
pytest test_project.py