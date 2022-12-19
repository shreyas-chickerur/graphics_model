from data_ingestion import ingest_data
from tkinter import *

vert_dict, line_list = ingest_data('object.txt')

root = Tk()

c = Canvas(root, width=750, height=750, background='white')
c.grid(row=0,column=0)

def create_circle(x, y, r, canvas):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, fill='black')

triangle = line_list[0]
all_pts = list()
for triangle in line_list:
    pts = list()
    for val in triangle:
        vertex = vert_dict[val]
        pts.append(int(vertex[0]) * 100 + 300)
        pts.append(int(vertex[1]) * 100 + 300)
    pts.append(int(vert_dict[triangle[0]][0]) * 100 + 300)
    pts.append(int(vert_dict[triangle[0]][1]) * 100 + 300)
    all_pts.append(pts)
for pts in all_pts:
    c.create_line(pts,fill='black', width=5)
    i = 0
    while (i < len(pts) - 1):
        x = pts[i]
        y = pts[i + 1]
        create_circle(x,y,10, c)
        # c.create_oval(x,y,x,y,fill="black", width=10)
        i += 2
root.mainloop()



