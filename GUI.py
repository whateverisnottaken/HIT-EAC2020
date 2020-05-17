#GUI
#written by Zhao Zitian with AKKO 3018V2

import csv
import tkinter as tk
from tkinter import *
#import categorize

def center_window(self,w = 800, h = 600):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

def createFrame(self):

    self.frm = tk.LabelFrame(root)
    self.frm.grid(row = 1, column = 0, padx = 5, pady = 10)

    self.frm_label = tk.Label(self.frm, text='Enter code below:', font=('stencil', 15))
    self.frm_label.grid(row=0, column=0, padx=5, pady=10)

    self.frm_button_compile = tk.Button(self.frm, text='compile→', command=compile, font=('stencil', 15), background = 'green', foreground = 'white', bd = 15, relief = RIDGE)
    self.frm_button_compile.grid(row=1, column=1, padx=25, pady=10)

    self.frm_lexical_label = tk.Label(self.frm, text='Lexical analysis', font=('stencil', 15))
    self.frm_lexical_label.grid(row=0, column=2, padx=5, pady=10)

    self.frm_lexical_canvas = tk.Text(self.frm, font=('consolas', 10), bg = 'white', bd = 2, width = 30)
    self.frm_lexical_canvas.grid(row=1, column=2, padx=5, pady=10)

    self.frm_trinity_label = tk.Label(self.frm, text='parse result', font=('stencil', 15))
    self.frm_trinity_label.grid(row=0, column=3, padx=5, pady=10)

    self.frm_trinity_canvas = tk.Text(self.frm, font=('consolas', 10), bg = 'white', bd = 2, width = 65)
    self.frm_trinity_canvas.grid(row=1, column=3, padx=5, pady=10)

    self.frm_symble_label = tk.Label(self.frm, text='symble table', font=('stencil', 15))
    self.frm_symble_label.grid(row=0, column=4, padx=5, pady=10)

    self.frm_symble_canvas = tk.Text(self.frm, font=('consolas', 10), bg = 'white', bd = 2, width = 30)
    self.frm_symble_canvas.grid(row=1, column=4, padx=5, pady=10)

    '''self.frm_button_quit = tk.Button(self.frm, text='     quit     ', command=root.quit, font=('stencil', 15), background = 'maroon', foreground = 'white',bd = 15, relief = RIDGE)
    self.frm_button_quit.grid(row=2, column=3, padx=25, pady=10)

    self.frm_button_clear = tk.Button(self.frm, text='    clear     ', command = clear_all, font=('stencil', 15), background = 'dark orange', foreground = 'white', bd = 15, relief = RIDGE)
    self.frm_button_clear.grid(row=2, column=0, padx=5, pady=10)

    self.frm_button_symble = tk.Button(self.frm, text='read', command = read_syntax, font=('stencil', 15), background = 'purple', foreground = 'white', bd = 15, relief = RIDGE)
    self.frm_button_symble.grid(row=2, column=4, padx=5, pady=10)'''

headers = ['id', 'polarity']

rows = []

csv_file = open('test.csv', 'w', newline = '')

f = csv.writer(csv_file)
f.writerow(headers)
f.writerows(rows)

root = tk.Tk()
root.title('Compilation system lab3')

center_window(root)
createFrame(root)

root.mainloop()