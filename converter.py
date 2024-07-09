import moviepy.editor
from tkinter.filedialog import *

path = askopenfilename()
select = moviepy.editor.VideoFileClip(path)
covert = select.audio

convert.write_audiofile("saved.mp3")
print("audio converted successfully ! ")
