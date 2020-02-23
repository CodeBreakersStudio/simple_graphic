import time, os, sys

try:  # import as appropriate for 2.x vs. 3.x
   import tkinter as tk
except:
   import Tkinter as tk

_root = tk.Tk()
_root.withdraw()

_update_lasttime = time.time()