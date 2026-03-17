Battleship Game (Just Python)

A fully interactive console-based Battleship game built in Python using clean architecture and modular design.
This one was my first project. It was developed as part of a Data Science learning journey, focusing on:
Clean code structure
Input validation
Game logic design
User interaction

----------------------------------------------------------------

Features

Turn-based gameplay (2 players)
Coordinate-based shooting system (e.g., B7)
Random ship placement
Hit / Miss detection
Ship destruction detection
Restart game anytime (r or restart)
Play again after finishing
Hidden ships for opponent view
Emoji-based visual board

----------------------------------------------------------------


Project Structure
battleship_project/
│
├── main.py              # Game loop
├── requirements.txt
├── README.md
│
└── src/
    ├── __init__.py
    ├── board.py        # Board creation & display
    ├── ships.py        # Ship placement logic
    ├── game.py         # Game mechanics (shooting, win condition)
    └── utils.py        # Helpers (coordinates, screen clear)


How to Run
Clone the repository:
git clone https://github.com/your-username/battleship_project.git
cd battleship_project

Install dependencies:
pip install -r requirements.txt

Run the game:
python main.py


How to Play

Players take turns entering coordinates:


B7
A1
J10…




          Symbols:



Meaning
🌊
Water
🚢
Ship
💥
Hit
❌
Miss


During the game:  You can type r or restart → restart the match instantly


----------------------------------------------------------------



Key Concepts Applied
Modular programming (separation of concerns)
Input validation & error handling
Matrix manipulation with NumPy
Game loop design
Clean and readable code practices


Author
Developed by José Marín 
Aspiring Data Scientist & Python Developer

 If you like this project...
Give it a star  on GitHub and feel free to contribute, THANK YOU SO MUCH!

