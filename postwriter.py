import tkinter as tk
import json
import datetime

posts_file = open("posts.json", "r")
posts = json.load(posts_file)

root = tk.Tk()
root.wm_geometry("400x400")
root_name = root.winfo_pathname(root.winfo_id())

label_title = tk.Label(root, text="Post title:")
label_title.pack(fill='x',padx=20, pady=10)
title = tk.Entry(root,width=20)
title.pack(fill='x', padx=20, pady=10, expand=True,anchor="n")

label_tags = tk.Label(root, text="Tags (separated by spaces):")
label_tags.pack(fill='x',padx=20, pady=10)
tags = tk.Entry(root,width=20)
tags.pack(fill='x', padx=20, pady=10, expand=True,anchor="n")

label_text = tk.Label(root, text="Post text:")
label_text.pack(fill='x',padx=20, pady=10,anchor="n")
text = tk.Text(root,width=80,height = 10)
text.pack(fill='x', padx=20, pady=10, expand=True,anchor="n")

def post():
    date = datetime.datetime.now()
    post = {}
    post["id"] = len(posts) + 1
    post["title"] = title.get()
    post["content"] = text.get("1.0",tk.END)
    post["date"] = f"{date.day}/{date.month}/{date.year} at {date.hour}:{date.minute}:{date.second}"
    post["tags"] = tags.get().split()

    posts.append(post)

    with open("posts.json", "w") as file:
        json.dump(posts, file, indent=2)
    
    dialog = tk.Toplevel(root)
    dialog_test = tk.Label(dialog, text="Post successful!")
    dialog_test.pack(fill='x',padx=20, pady=10,anchor="n")
    dialog_confirm_button = tk.Button(dialog, text= "OK", width= 10, command= root.destroy)
    dialog_confirm_button.pack()
    confirm_button.config(state = "disabled")  

confirm_button = tk.Button(root, text= "OK", width= 10, command= post)
confirm_button.pack()

cancel_button = tk.Button(root,text= "Quit", width= 10, command= root.destroy)
cancel_button.pack()

root.mainloop()