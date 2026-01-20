"""
This is an example file and is not required for the library to function
"""
from fancy import print

# Use default tags
print.error("Error message")
print.warning("Warning")
print.success("Success!")

# Add custom tags
print.set("custom", (255, 100, 200)) # use hex codes
print.set("special", "bright_cyan") # use rich colour names


print.special("My custom blue tag!")

print.custom("My custom pink tag!")
