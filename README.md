# FruitBasketPython

A simple Python console application demonstrating fruit selection, list operations, and the Last In, First Out (LIFO) principle.

## Overview

FruitBasketPython is a beginner-friendly project that allows users to choose fruits for a basket and remove them one at a time.

Users first specify how many fruits they want to catch, then enter a letter corresponding to each fruit. After the basket is filled, they can press `E` to eat the last fruit added.

The project demonstrates basic Python concepts, including lists, dictionaries, loops, user input, conditional statements, and list methods.

## Features

- Supports four fruit choices: Apple, Orange, Mango, and Guava.
- Uses keyboard letters to select fruits.
- Allows users to choose how many fruits to add.
- Displays the current contents of the basket.
- Removes the most recently added fruit when the user presses `E`.
- Detects when the basket becomes empty and displays a completion message.

## Technologies Used

- **Programming Language:** Python 3
- **Data Structures:** List and dictionary
- **Core Concepts:** Loops, user input, conditionals, and list operations

## Project Structure

```text
FruitBasketPython/
├── fruit_basket.py
└── README.md
```

## Supported Fruits

| Key | Fruit |
|---|---|
| `A` | Apple |
| `O` | Orange |
| `M` | Mango |
| `G` | Guava |

Fruit selection is case-insensitive, so lowercase and uppercase letters are accepted.

## How It Works

1. The program initializes an empty basket.
2. It displays the available fruit choices.
3. The user enters the number of fruits to catch.
4. The user selects each fruit by entering its corresponding letter.
5. The program displays the basket contents.
6. The user presses `E` to eat the most recently added fruit.
7. The program removes the last fruit using `pop()`.
8. When the basket is empty, the program displays `No more Fruits.` and exits the eating loop.

### Understanding the LIFO Principle

The basket uses Python's list as a stack.

**Last In, First Out (LIFO)** means the last fruit added is the first fruit removed. For example, if the user adds Apple, then Mango, Mango is removed first when `E` is pressed.

## Requirements

- Python 3 installed on your computer.
- A terminal or command prompt.

The program uses Python's standard library and does not require third-party packages.

## How to Run

1. Clone or download the repository.
2. Open a terminal in the project directory.
3. Run the program:

   ```bash
   python fruit_basket.py
   ```

   On systems where Python 3 uses the `python3` command:

   ```bash
   python3 fruit_basket.py
   ```

4. Follow the on-screen prompts to select and eat fruits.

## Example Session

```text
Catch and eat any of these fruits:('apple', 'orange', 'mango', 'guava')
How many fruits would you like to catch? 3
Choose a fruit to catch. Press A, O, M or G.
Fruit 1 of 3:A
Fruit 2 of 3:M
Fruit 3 of 3:G
Your basket now has : ['Apple', 'Mango', 'Guava']
Press E to eat Fruit :
e
Your basket now has : ['Apple', 'Mango']
Press E to eat Fruit :
e
Your basket now has : ['Apple']
Press E to eat Fruit :
e
No more Fruits.
```

## Current Limitations

- Only four predefined fruits are available.
- Invalid fruit letters can cause a `KeyError`.
- Non-numeric input for the fruit count can cause a `ValueError`.
- Negative fruit counts are not explicitly rejected.
- The eating loop accepts `E` as its removal command but has no separate quit option.
- The program removes fruits in reverse order of selection because it uses `list.pop()` without an index.

## Possible Improvements

- Validate fruit selections and prompt again when an invalid letter is entered.
- Ensure the fruit count is a valid nonnegative integer.
- Add an option to exit the eating loop.
- Improve the displayed instructions and spacing.
- Add a summary of the fruits eaten.
- Use a `while basket` loop to make the eating process easier to follow.

## Project Purpose

This project is an introductory Python exercise for learning user input, dictionaries, lists, and stack-like behavior through a simple fruit basket activity.

## Author

**Ichiro Yamazaki**

GitHub: [@ichiroyamazaki](https://github.com/ichiroyamazaki)

## License

No license is specified in the repository. Check with the repository owner before redistributing or reusing the source code.
