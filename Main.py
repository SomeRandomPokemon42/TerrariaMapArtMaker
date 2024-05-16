import tkinter, tkinter.filedialog
import PIL.Image
import PIL.ImageTk
import imageio
import ImageToBlocks
import numpy


take5YearsToProcess = False

window = tkinter.Tk()
window.wm_resizable(width= False, height= False) # ban resizing
tkelements = []
tkelements.append(tkinter.Label(window, text="Getting Image"))
tkelements[-1].pack()
window.update_idletasks()
window.update()


imageFileTypes = [("Image Files", ("*.PNG", "*.png", "*.jpeg", "*.JPEG", "*.jpg", "*.JPG"),)]
filePath = tkinter.filedialog.askopenfilename(initialdir="/", title= "Open a image file", filetypes= imageFileTypes)
# Update UI with image reading
tkelements[-1].configure(text="Reading image")
tkelements[-1].pack()
window.update_idletasks()
window.update()
# Read the image
file = imageio.v3.imread(filePath)


imageSize = (len(file), len(file[0]))
if imageSize[0] > imageSize[1]:
    largeEndImage = imageSize[0]
else:
    largeEndImage = imageSize[1]
# calculate the window size
pixelsPerTile = 0
screenSize = (window.winfo_screenheight(), window.winfo_screenwidth())
if screenSize[0] > screenSize[1]:
    smallEnd = screenSize[0]
else:
    smallEnd = screenSize[1]
perferredSize = smallEnd / 2
pixelsPerTile = round(perferredSize / largeEndImage)
del perferredSize, smallEnd, screenSize


if (take5YearsToProcess):
    NewImage = []
    for x in range(0, imageSize[0]):
        # Start row
        NewImage.append([])
        # Update UI
        tkelements[-1].configure(text = str(x) + " out of " + str(imageSize[0]))
        tkelements[-1].pack()
        window.update_idletasks()
        window.update()
        # Actually do the row
        for y in range(0, imageSize[1]):
            NewImage[-1].append(list(ImageToBlocks.GetClosestColorInt(file[x][y])))
    # Load the image on the screen
    NewImage = numpy.array(NewImage)
else:
    NewImage = numpy.array(file)


NewImageFile = PIL.Image.fromarray(NewImage.astype(numpy.uint8))
NewImageFile.save("output.png")


print(pixelsPerTile)
TKImage = PIL.ImageTk.Image.open(fp="output.png")
#TKImage.resize((imageSize[0] * pixelsPerTile, imageSize[1] * pixelsPerTile))
TKImage = PIL.ImageTk.PhotoImage(TKImage)


def Draw(event):
    #mouse = (round(event.x/pixelsPerTile), round(event.y/pixelsPerTile))
    mouse = (event.x, event.y)
    hoverObject = "null"
    try:
        hoverObject = ImageToBlocks.GetClosestColor(NewImage[mouse[0]][mouse[1]])
    except IndexError:
        hoverObject = "null"
    tkelements[-1].configure(text= str(mouse) + "  " + str(hoverObject))
    tkelements[-1].pack()


# load the final ui
tkelements[-1].destroy()
tkelements = []
tkelements.append(tkinter.Label(window, bd=0))

tkelements[-1].configure(image = TKImage)
tkelements[-1].pack()
tkelements[-1].bind('<Motion>', Draw)
tkelements.append(tkinter.Label(window))
tkelements[-1].configure(text="Position")
tkelements[-1].pack()


window.mainloop()