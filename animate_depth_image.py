import sys
import scipy.io
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pathlib import Path

def animate_depth_data(action, subject, trial):
    # To update the data being passed to the next plot 
    def update_fig(*args):
        nonlocal frame
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
        print(f'Error: Kinect file {filename} is not found.')
        sys.exit()

    # Create animated plot 
    im = plt.imshow(data[:,:,0], animated=True, cmap='seismic')
    ani = animation.FuncAnimation(fig, update_fig, interval=33, blit=True)
    plt.show()

if __name__ == "__main__":
    if(len(sys.argv) != 4):
        print("Error: 3 parameters are expected.")
        sys.exit()
    try:
        action = int(sys.argv[1]) # ranged from 1 to 27
        subject = int(sys.argv[2]) # ranged from 1 to 8
        trial = int(sys.argv[3]) # ranged from 1 to 4
    except ValueError:
        print("Error: Integer parameter is expected.")
        sys.exit()
    animate_depth_data(action, subject, trial)