import tkinter as tk
def LabelME(root):

    labelok= tk.Label(root, fg='red', text="test me", width=40, height=2)

    labelok.grid(row=9, rowspan=1, columnspan=2, )
def klkl(a,b):
    return a+b;


class LabelMEClass:
    def __init__(self,root ):
        self.root = root;   #Frame
        self.labelMM =0;

    def LabelSet(self):
        self.labelMM= tk.Label(self.root, fg='red', text="test out", width=40, height=2)
        self.labelMM.grid(row=10, rowspan=1, columnspan=2, )


class LabelMETEST:
    def __init__(self,root ):
        self.root = root;   #Frame
        self.labelMM =0;

    def LabelSet(self):
        self.labelMM= tk.Label(self.root, fg='red', text="test out", width=40, height=2)
        self.labelMM.grid(row=3, rowspan=1, columnspan=2, )