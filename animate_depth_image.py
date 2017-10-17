import scipy.io
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pathlib import Path

# Configure action, subject and trial
action = 18 # Range from 1 to 27
subject = 6 # Range from 1 to 8
trial = 1 # Range from 1 to 4

# To update the data being passed to the next plot 
def animate(*args):
    global frame
    if frame == data.shape[2]: frame = 0
    im.set_array(data[:,:,frame])
    frame = frame + 1
    return im,

# Initialization 
frame = 0
fig = plt.figure()

# Check if file exists. If file is not found, exit the program.
filename = f'data/Depth/a{action}_s{subject}_t{trial}_depth.mat'
if Path(filename).is_file():
    mat = scipy.io.loadmat(filename)
    data = mat['d_depth']
else:
    print(f'File {filename} is not found!.')
    sys.exit()

# Create animated plot 
im = plt.imshow(data[:,:,0], animated=True, cmap='gray')
ani = animation.FuncAnimation(fig, animate, interval=33, blit=True)
plt.show()