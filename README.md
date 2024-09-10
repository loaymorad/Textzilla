```markdown
# File Divider and Combiner

This project provides two main functionalities: dividing a large text file into smaller batches and combining multiple text files into a single file. It’s a simple command-line utility implemented in Python.

## Features

- **Divider**: Splits a given text file into smaller files of a specified batch size.
- **Combiner**: Merges multiple text files into one larger text file.
- **Command-Line Interface**: Easy to use from the command line with simple menu options.

## Requirements

- Python 3.x
- No additional packages are required.

## Installation

1. Clone the repository or download the source code.
2. Navigate to the project directory.

```bash
git clone https://github.com/loaymorad/Textzilla.git
cd textzilla
```

## Usage

To run the script, use the command line:

### Divider

To divide a text file into smaller files:

```bash
python main.py divider <file.txt> <NumberOfDivision>
```

- `<file.txt>`: The name of the file you want to divide.
- `<NumberOfDivision>`: The number of lines each divided file should contain.

### Combiner

To combine multiple text files into a single file:

```bash
python main.py compiner <file1.txt> <file2.txt> ... <fileN.txt>
```

### Menu

You can also run the script without parameters to see a menu:

```bash
python main.py
```

From the menu, you can choose to use the divider or combiner, or exit the program.

## Example

1. **Dividing a file**:

   ```bash
   python main.py divider example.txt 100
   ```

   This command will create a folder named `example` containing multiple text files with 100 lines each.

2. **Combining files**:

   ```bash
   python main.py compiner part1.txt part2.txt part3.txt
   ```

   This command will create a file named `big.txt` that combines the contents of `part1.txt`, `part2.txt`, and `part3.txt`.

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or new features!
