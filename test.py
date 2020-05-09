

root = tk.Tk()
s = ttk.Style(root)
s.theme_use('clam')

ttk.Button(root, text='Calendar', command=calendar_view).pack(padx=10, pady=10)
ttk.Button(root, text='DateEntry', command=dateentry_view).pack(padx=10, pady=10)

root.mainloop()