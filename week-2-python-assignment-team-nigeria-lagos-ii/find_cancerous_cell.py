# Break and Continue in Loops: Finding First Cancerous Cell
# Filename: find_cancerous_cell.py
# Write a function `find_cancerous_cell(cells)` that loops through a list of cell samples and:
# - Uses `break` to stop once a cancerous cell is found.
# - Uses `continue` to skip unlabeled cells (None values).

def find_cancerous_cell(cells):
    for i in cells:
        if i == "cancerous":
            return "cancerous"
            break
        if i is None:
            continue