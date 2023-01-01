#!/usr/bin/python3
def text_indentation(text):
    try:
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        else:
            for character in text.strip():
                if character not in [".", "?", ":"]:
                    print(character, end="")
                else:
                    print()
                    print()
    except Exception as exc:
        return exc

print(text_indentation("I hate John Doe so much.I'd really love to kill him and his: "))