# Awesome Graphical Tic Tac Toe Game
    #### Video Demo:  <URL HERE>
    #### Description: An implementation of the classic Tic Tac Toe game using Python and Tkinter.
---

## Installation

1. Make sure you have Python installed on your system.
2. Clone this repository or download the source code.
3. Navigate to the project directory.

## Usage

1. Run the `project.py` script.
2. Click on the tiles to make your moves (alternating between "X" and "O").
3. The game checks for winning combinations and displays the winner when the game is over.
4. You can restart the game by clicking anywhere or change the background image using the buttons.

## Code Explanation

### `Ticktacktoe` Class

- Extends the `Tk` class and handles game logic and aesthetics.
- Initializes the game window, sets up the game tiles, and handles player moves.
- Checks for winning combinations and displays the winner.
- Provides options to restart the game or change the background image.

### Constants

- `WIDTH` and `HEIGHT`: Dimensions of the game window.
- Paths to various images used in the game (e.g., "x.png", "o.png", "def.png").
- Background images ("bg.png" and "bp.png").
- Icons and winning images ("X_WIN.png" and "O_WIN.png").

## Running Tests

To run the test suite, execute the following command:

```bash
pytest test_project.py
```

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests.

---


## Tic Tac Toe Game Explanation

### 1. Import Statements
```python
import itertools
from tkinter import Tk, Canvas, font, CENTER
import Constants
from PIL import Image, ImageTk
```
- The code begins by importing necessary modules:
    - `itertools`: Used for creating combinations of moves.
    - `Tk` and `Canvas` from `tkinter`: Used for creating the game window and drawing the grid.
    - `font`: Used for setting the font style.
    - `Constants`: This module likely contains paths to image files and other constants.
    - `Image` and `ImageTk` from `PIL`: Used for working with images.

### 2. `Ticktacktoe` Class
- The main class that extends `Tk` and handles the game logic and aesthetics.
- Initializes the game window, sets up the game tiles, and handles player moves.
- Checks for winning combinations and displays the winner.
- Provides options to restart the game or change the background image.

### 3. Constants
- Constants related to the game, such as window dimensions, image paths, and simplified winning combinations.

### 4. `initialize_coordination` Method
- Sets up the game tiles (cells) on the canvas.
- Determines the coordinates for each cell based on its position (0 to 8).
- Binds a mouse click event to each cell, allowing players to make moves.

### 5. `clicked` Method
- Handles the logic when a player clicks on a cell.
- Determines which player's turn it is (X or O).
- Updates the cell with the corresponding image (X or O).
- Keeps track of already clicked cells.
- Calls the `check_win` method to see if there's a winner.

### 6. `check_win` Method
- Checks if any player has won.
- Compares the current moves (X or O) with predefined winning combinations.
- If a winning combination is found, displays the winner's image and a message.
- Allows players to play again by clicking anywhere.

### 7. `alternate_background` Method
- Changes the background image when the "Change Background" button is clicked.
- Alternates between two background images (gray and pink).

### 8. `main` Function
- Creates an instance of the `Ticktacktoe` class and runs the game.
- Calls other helper functions to get text, background color, and clicked cells.

### 9. Test Functions
- Test functions check various aspects of the game (e.g., win combinations, background change, restart).
- These functions ensure the correctness of the game logic.

## Conclusion
This code provides a functional implementation of the Tic Tac Toe game using Python and Tkinter. Players can interact with the graphical interface, make moves, and enjoy the classic game. Feel free to explore and modify the code further to enhance or customize your game! 😊
