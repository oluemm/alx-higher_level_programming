#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        """Check if the defined name starts with __"""
        if name[0:2] != "__":
            print(name)