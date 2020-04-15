from tkinter import Tk
from idlelib.TreeWidget import ScrolledCanvas, FileTreeItem, TreeNode
import os

root = Tk()
root.title('File Browser')

sc = ScrolledCanvas(root, bg='white', highlightthickness=0, takefocus=1)
sc.frame.pack(expand=1, fill='both', side='left')

item = FileTreeItem(os.getcwd())
node = TreeNode(sc.canvas, None, item)
node.expand()

root.mainloop()
