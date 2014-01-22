import uncompyle2
with open("file.py", "wb") as fileobj:
    uncompyle2.uncompyle_file("ps6_verify_movement27.pyc", fileobj)