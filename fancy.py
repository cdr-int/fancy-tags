"""
fancy.py - A simple library for formatted tag-based printing

rich must be installed to use colour formatting, if rich is not installed no formatting wil be applied

Default tags:

* error: (220, 50, 47) Bright red
* warning: (255, 193, 7) Amber
* success: (46, 204, 113) Emerald green
* info: (52, 152, 219) Sky blue
* debug: (155, 89, 182) Purple
* critical: (192, 57, 43) Dark red
* ok: (39, 174, 96) Green
* fail: (231, 76, 60) Red
* skip: (26, 188, 156) Turquoise
* note: (52, 172, 224) Light blue
* todo: (241, 196, 15) Yellow
* done: (34, 153, 84) Forest green
* start: (93, 109, 255) Indigo
* end: (108, 92, 231) Violet

Add custom file specific tags (define before calling)

print.set("newtag0", (255, 100, 200))
print.set("newtag1", "bright_cyan")

"""

class TaggedPrint:
    def __init__(self):
        self.tags = {}
        self._rich_available = False
        self._tag_colours = {}
        
        try:
            from rich.console import Console
            self.console = Console()
            self._rich_available = True
        except ImportError:
            self.console = None
        
        self._set_defaults()
        
        self.max_tag_len = max(len(tag) for tag in self._tag_colours.keys()) if self._tag_colours else 0
    
    def _set_defaults(self):
        self.set("error", (220, 50, 47))        # Bright red
        self.set("warning", (255, 193, 7))      # Amber
        self.set("success", (46, 204, 113))     # Emerald green
        self.set("info", (52, 152, 219))        # Sky blue
        self.set("debug", (155, 89, 182))       # Purple
        self.set("critical", (192, 57, 43))     # Dark red
        self.set("ok", (39, 174, 96))           # Green
        self.set("fail", (231, 76, 60))         # Red
        self.set("skip", (26, 188, 156))        # Turquoise
        self.set("note", (52, 172, 224))        # Light blue
        self.set("todo", (241, 196, 15))        # Yellow
        self.set("done", (34, 153, 84))         # Forest green
        self.set("start", (93, 109, 255))       # Indigo
        self.set("end", (108, 92, 231))         # Violet
    
    def set(self, tag_name, colour):
        """
        Set a specific colour for a tag (requires Rich)
        
        Args:
            tag_name: Name of the tag
            colour: Can be a colour name string, RGB tuple (r, g, b), or Rich colour string
        
        Examples:
            print.set("custom", (255, 100, 50))  # RGB
            print.set("custom", "bright_blue")   # Colour name
        """
        if not self._rich_available:
            return
        
        tag = tag_name.upper()
        
        if isinstance(colour, tuple) and len(colour) == 3:
            r, g, b = colour
            colour = f"rgb({r},{g},{b})"
        
        self._tag_colours[tag] = colour
    
    def __getattr__(self, tag_name):
        tag = tag_name.upper()
        
        if tag not in self.tags:
            self.tags[tag] = True
            self.max_tag_len = max(self.max_tag_len, len(tag))
        
        def print_with_tag(message=""):
            padding = self.max_tag_len - len(tag)
            spaces = " " * padding
            
            tag_text = f"[{tag}{spaces}]"
            
            if self._rich_available:
                from rich.text import Text
                
                colour = self._tag_colours.get(tag, "")
                style = f"bold {colour}".strip()
                
                tag_part = Text()
                tag_part.append("[", style="")
                tag_part.append(tag + spaces, style=style)
                tag_part.append("]", style="")
                
                if message:
                    self.console.print(tag_part, message)
                else:
                    self.console.print(tag_part)
            else:
                if message:
                    print(f"{tag_text} {message}")
                else:
                    print(tag_text)
        
        return print_with_tag


print = TaggedPrint()

# Example usage
if __name__ == "__main__":
    print.tag("hello world!")
    print.testing("")
    print.info("This is an informational message")
    print.error("Something went wrong")
    print.warning("Be careful!")
    
    # Custom colours are easy to set with RGB or colour names
    print.set("custom", (255, 100, 200))  # RGB hex (pink)
    print.set("special", "bright_cyan")    # Colour name
    
    print.custom("Custom RGB colour!")
    print.special("Special colour!")