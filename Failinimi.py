from tkinter import filedialog
from tkinter import messagebox
def teadasaama():
    failinimi = filedialog.askopenfilename()
    if failinimi:
      messagebox.showinfo("Fail", failinimi)
      teadasaama()
teadasaama()
