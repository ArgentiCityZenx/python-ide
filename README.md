# Python IDE

A simple Python Integrated Development Environment (IDE) built using `tkinter` and `customtkinter`. This IDE features syntax highlighting, a console for output, and basic functionality to open and run Python scripts.

## Features

- **Code Editor**: Edit Python code with line numbers and basic syntax highlighting.
- **Console Output**: View the output of your code directly in the IDE's console.
- **Open and Run Files**: Open existing Python files and run them within the IDE.

## Requirements

- Python 3.6 or later
- `tkinter` (usually included with Python)
- `customtkinter`
- `Pillow` (for icon support)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ArgentiCityZenx/python-ide.git
   ```

2. Navigate to the project directory:
   ```bash
   cd python-ide
   ```

3. Install the required packages:
   ```bash
   pip install customtkinter Pillow
   ```

## Usage

1. **Run the IDE**:
   ```bash
   python pythonide.py
   ```

2. **Using the IDE**:
   - **Open a File**: Click the "Open" button to select and open a Python file.
   - **Edit Code**: Write or modify Python code in the editor.
   - **Run Code**: Click the "Run" button to execute the code. The output will be displayed in the console.

## Customization

- **Icon**: The IDE icon is set to `iconpy.png`. Ensure this file is located in the same directory as the script, or modify the path in the `set_icon` method of `pythonide.py`.

## Code Structure

- `pythonide.py`: The main script that creates and manages the IDE window.
- `iconpy.png`: The icon file used for the IDE window. Replace with your own `.png` or `.ico` file if needed.

## Troubleshooting

- **Icon Issues**: If the icon does not appear, make sure `iconpy.png` is a valid image file and located in the same directory as `pythonide.py`.
- **Library Issues**: Ensure all required libraries (`customtkinter`, `Pillow`) are installed. Use `pip` to install them.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- `customtkinter` for modern `tkinter` widgets.
- `Pillow` for image handling in `tkinter`.

```
