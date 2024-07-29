# Module 4: Variable Number of Players

## Introduction

In this module, you will extend the card drawing app to allow users to input custom player names before starting the game.

## Requirements

- Python 3.x
- Flask

## Setup Instructions

1. Clone the repository or download the project files.

2. Navigate to the project directory:

   ```bash
   cd path/to/project
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   On Windows:

   ```bash
   venv\Scriptsctivate
   ```

   On macOS and Linux:

   ```bash
   source venv/bin/activate
   ```

5. Install the dependencies:

   ```bash
   pip install Flask
   ```

6. Ensure the `questions.txt` file is in the project directory and contains your questions.

7. Run the Flask application:

   ```bash
   python app.py
   ```

8. Open your web browser and go to [http://127.0.0.1:8080/](http://127.0.0.1:8080/) to view and interact with the application.

## How to use

- Click the "DRAW" button to draw a card from the deck.
- The drawn card will be displayed below the button.
- Select the player who won the point by choosing the appropriate radio button.
- Click "Enter" to submit the winner.
- The progress bars will update based on the players' scores.
- The first player to reach 3 points wins the game.
