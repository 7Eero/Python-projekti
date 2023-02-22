import json
import tkinter as tk

root = tk.Tk()
root.title("Binary and Decimal Converter")

try:
    with open("history.jon") as jsonHistory:
        data = json.load(jsonHistory)
except:
    data = {"inputs": [], "outputs": []}
    with open("history.jon", "w") as jsonHistory:
        json.dump(data, jsonHistory)

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack()
for i in range(len(data["inputs"])):
    listbox.insert(tk.END, f"{data['inputs'][i]} = {data['outputs'][i]}")

inputLabel = tk.Label(root, text="Decimal:")
inputLabel.pack(side=tk.TOP)
inputEntry = tk.Entry(root, width=40)
inputEntry.pack(side=tk.TOP)

outputLabel = tk.Label(root, text="Binary:")
outputLabel.pack(side=tk.TOP)
outputEntry = tk.Entry(root, width=40, state="disabled")
outputEntry.pack(side=tk.TOP)

def binary_to_decimal():
    binary = inputEntry.get()
    decimal = int(binary, 2)
    outputEntry.config(state="normal")
    outputEntry.delete(0, tk.END)
    outputEntry.insert(0, decimal)
    outputEntry.config(state="disabled")
    data["inputs"].append(binary)
    data["outputs"].append(decimal)
    with open("history.jon", "w") as jsonHistory:
        json.dump(data, jsonHistory)
    listbox.insert(tk.END, f"{binary} = {decimal}")

def decimal_to_binary():
    decimal = int(inputEntry.get())
    binary = bin(decimal)[2:]
    outputEntry.config(state="normal")
    outputEntry.delete(0, tk.END)
    outputEntry.insert(0, binary)
    outputEntry.config(state="disabled")
    data["inputs"].append(binary)
    data["outputs"].append(decimal)
    with open("history.jon", "w") as jsonHistory:
        json.dump(data, jsonHistory)
    listbox.insert(tk.END, f"{binary} = {decimal}")

def switch_mode():
    current_mode = mode.get()
    if current_mode == "binary":
        mode.set("decimal")
        inputLabel.config(text="Decimal:")
        outputLabel.config(text="Binary:")
        convertButton.config(text="Convert", command=decimal_to_binary)
    else:
        mode.set("binary")
        inputLabel.config(text="Binary:")
        outputLabel.config(text="Decimal:")
        convertButton.config(text="Convert", command=binary_to_decimal)
    inputEntry.delete(0, tk.END)
    outputEntry.delete(0, tk.END)

def clear_entry():
    inputEntry.delete(0, tk.END)
    outputEntry.config(state="normal")
    outputEntry.delete(0, tk.END)
    outputEntry.config(state="disabled")

mode = tk.StringVar(value="decimal")

convertButton = tk.Button(root, text="Convert", command=decimal_to_binary)
convertButton.pack(side=tk.TOP)

pickMode = tk.Button(root, text="Switch Mode", command=switch_mode)
pickMode.pack(side=tk.TOP)

clearButton = tk.Button(root, text="Clear", command=clear_entry)
clearButton.pack(side=tk.TOP)

root.mainloop()