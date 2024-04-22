# FeastFriend Application

## Overview
FeastFriend is a Python application designed to manage meal categories and participants for events. The application allows users to add, view, and delete events, as well as manage meal categories and participant details.

## Features
- Register and manage events with different meal categories: starters, main meals, drinks, and desserts.
- Add and remove participants from events.
- Interactive GUI built with Tkinter.

## How to Run
Ensure you have Python and Tkinter installed on your system. You can run the application by executing the script in a Python environment.

```bash
python main.py
```

## Code Structure
The application's structure is based on the Tkinter GUI toolkit for Python:
- **Main Window Setup**: The `root` window is configured with a title, dimensions, and a background color.
- **Meal Categories**: A dictionary `meal_cat` defines various meal categories and their participants.
- **Event Management**: Uses deep copying of dictionaries to manage different events and their respective details.
- **Dynamic GUI Components**: Labels, buttons, and frames dynamically update based on user interaction.
- **Event Handlers**: Functions are bound to GUI components to handle events such as mouse hover, clicks, and selection changes.

## Creator
**Michael Nyanyuie**
- Role: Developer of FeastFriend
- Responsibilities: Designing, coding, and testing the application.
- Contact: [mnyanyuie@gmail.com]

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
- Thanks to everyone who has contributed to testing and providing feedback for the application.