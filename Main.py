import tkinter, tkinter.filedialog
import PIL.Image
import imageio
import ImageToBlocks
import numpy


window = tkinter.Tk()
window.resizable(0,0) # ban resizing
tkelements = []


imageFileTypes = [("Image Files", ("*.PNG", "*.png", "*.jpeg", "*.JPEG", "*.jpg", "*.JPG"),)]
filePath = tkinter.filedialog.askopenfilename(initialdir="/", title= "Open a image file", filetypes= imageFileTypes)
file = imageio.v3.imread(filePath)


imageSize = (len(file), len(file[0]))
if imageSize[0] > imageSize[1]:
    largeEndImage = imageSize[1]
else:
    largeEndImage = imageSize[0]
# calculate the window size
pixelsPerTile = 0
screenSize = (window.winfo_screenheight(), window.winfo_screenwidth())
if screenSize[0] > screenSize[1]:
    smallEnd = screenSize[1]
else:
    smallEnd = screenSize[0]
perferredSize = smallEnd / 2
pixelsPerTile = round(perferredSize / largeEndImage)
del perferredSize, smallEnd, screenSize


NewImage = []
for x in range(0, imageSize[0]):
    NewImage.append([])
    for y in range(0, imageSize[1]):
        NewImage[-1].append(list(ImageToBlocks.GetClosestColorInt(file[x][y])))
NewImage = numpy.array(NewImage)
NewImageFile = PIL.Image.fromarray(NewImage.astype(numpy.uint8))
NewImageFile.save("output.png")

window.mainloop()