#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by the hidden_4 module."""
    import hidden_4

    module_names = [name for name in dir(hidden_4) if not name.startswith("__")]

    for name in module_names:
        print(name)
