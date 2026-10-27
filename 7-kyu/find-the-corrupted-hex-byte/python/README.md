## Task

A hexadecimal dump should contain only valid hexadecimal bytes.

A valid byte:

- consists of exactly two characters.
- contains only hexadecimal digits (`0-9`, `A-F`).
- uses uppercase letters only.

Return the index of the first corrupted byte.

If every byte is valid, return `-1`.

### Examples

find_corrupted_byte(["48", "65", "6C", "6C", "6F"])
# -1

find_corrupted_byte(["48", "65", "6G", "6C", "6F"])
# 2

find_corrupted_byte(["48", "6", "6C"])
# 1

find_corrupted_byte(["48", "6c", "6F"])
# 1

### Notes

- The input is a list of strings.
- An empty list is considered valid.
- If multiple corrupted bytes exist, return the index of the first corrupted byte.
- Lowercase and mixed-case hexadecimal letters are invalid.