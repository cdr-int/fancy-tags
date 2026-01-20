# fancy.py - A Simple Library for Formatted Tag-Based Printing

`fancy.py` allows you to easily print messages with custom tags and color formatting. You can set custom colors for specific tags and print formatted messages with them. If the `rich` library is installed, color formatting will be applied, otherwise, no formatting will be used.

## Requirements

- **`rich`** (optional but recommended): Used for color formatting.

To install `rich` (if not already installed):
```bash
pip install rich
````

## Features

* **Tag-Based Printing**: Print messages with various pre-defined or custom tags.
* **Customizable Colors**: Set colors for tags either as RGB tuples or using named colors.
* **Rich Library Support**: If `rich` is installed, color formatting will be applied, otherwise, the output will be plain text.

## Preview

<img width="500" height=auto alt="terminal preview" src="https://github.com/user-attachments/assets/cb528909-30f7-406c-af73-2eddcc514fba" />


## Default Tags

The following default tags are included with the library, each with a pre-defined color:

* **error**: (220, 50, 47) - Bright red
* **warning**: (255, 193, 7) - Amber
* **success**: (46, 204, 113) - Emerald green
* **info**: (52, 152, 219) - Sky blue
* **debug**: (155, 89, 182) - Purple
* **critical**: (192, 57, 43) - Dark red
* **ok**: (39, 174, 96) - Green
* **fail**: (231, 76, 60) - Red
* **skip**: (26, 188, 156) - Turquoise
* **note**: (52, 172, 224) - Light blue
* **todo**: (241, 196, 15) - Yellow
* **done**: (34, 153, 84) - Forest green
* **start**: (93, 109, 255) - Indigo
* **end**: (108, 92, 231) - Violet

## Custom Tags

You can define your own tags with specific colors:

```python
# Set custom tags with RGB values or named colors
print.set("newtag0", (255, 100, 200))  # RGB
print.set("newtag1", "bright_cyan")    # Named color
```

## Usage

1. **Initialize the Library**:

```python
from fancy import print
```

2. **Using Default Tags**:

```python
print.info("This is an informational message")
print.error("Something went wrong")
print.warning("Be careful!")
```

3. **Using Custom Tags**:

You can define custom tags with the `set` method and then print with them:

```python
print.set("custom", (255, 100, 200))  # Set RGB color
print.set("special", "bright_cyan")    # Set named color

print.custom("This is a custom RGB color!")
print.special("This is a special color!")
```

4. **Without Rich Installed**:

If `rich` is not installed, the color formatting will not be applied, but the tag-based printing will still work as plain text.

```bash
pip install rich  # If rich is not installed, color formatting won't work
```

## Example

```python
# Example usage
if __name__ == "__main__":
    print.info("Informational message")
    print.error("Error message!")
    print.success("Success message!")
    print.warning("Warning message!")
    
    # Using custom colors
    print.set("custom", (255, 100, 200))  # Custom RGB color (Pink)
    print.set("highlight", "yellow")      # Named color
    
    print.custom("Custom color message!")
    print.highlight("Highlighted message!")
```
**Photo Example**:

<img width="500" height=auto alt="preview" src="https://github.com/user-attachments/assets/31993a78-508b-41ab-a4d0-54cf38932671" />

## How It Works

1. **Tag Creation**: Each time a tag is accessed (like `print.info`), a function is dynamically created that prints the tag with its corresponding color.
2. **Color Formatting**: If the `rich` library is available, the output is printed with the appropriate color using `rich.console.Console` and `rich.text.Text`. If `rich` is not available, the color formatting will be omitted, and only the tag and message are printed as plain text.
3. **Custom Tags**: You can easily add custom tags with specific colors by using the `set()` method. You can pass either an RGB tuple (e.g., `(255, 100, 50)`) or a named color (e.g., `"bright_blue"`) as the color value.

## Set Custom Tags Example

You can add your own custom tags with any color you prefer:

```python
print.set("my_custom_tag", (200, 150, 50))  # Custom RGB
print.set("highlight", "bright_magenta")    # Named color

# Now you can use the tags to print with custom colors:
print.my_custom_tag("This is a custom RGB color tag!")
print.highlight("This is a bright magenta tag!")
```

## Advanced Configuration

You can customize the maximum tag length to adjust the spacing between the tag and the message. By default, it is set to the longest tag. If you want to change it manually, you can adjust the `max_tag_len` attribute.

```python
# Adjust the max tag length
print.max_tag_len = 20  # Set a custom maximum tag length
```

## Installation

Simply download or clone this repository to your project, and then import `TaggedPrint` to start using it:

```bash
git clone https://github.com/yourusername/fancy.py.git
```

Then, in your script, use:

```python
from fancy import TaggedPrint

print = TaggedPrint()
```

### Example Project Structure

```plaintext
your-project/
│
├── fancy.py         # This is the library file
└── main.py          # Your main Python script that uses fancy.py
```

## License

This library is licensed under the MIT License. See `LICENSE` for more information.

## Contributing

Feel free to fork this project, submit issues, or make pull requests. Contributions are always welcome!

---
