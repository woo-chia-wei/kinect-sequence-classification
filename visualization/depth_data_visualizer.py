import sys
import scipy.io
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter.ttk as ttk
from pathlib import Path
from tkinter import *

import depth_data_visualizer_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    depth_data_visualizer_support.set_Tk_var()
    top = Depth_Data_Visualizer (root)
    depth_data_visualizer_support.init(root, top)
    root.mainloop()

w = None
def create_Depth_Data_Visualizer(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    depth_data_visualizer_support.set_Tk_var()
    top = Depth_Data_Visualizer (w)
    depth_data_visualizer_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Depth_Data_Visualizer():
    global w
    w.destroy()
    w = None

class Depth_Data_Visualizer:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font12 = "-family {Times New Roman} -size 10 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font13 = "-family {Times New Roman} -size 11 -weight bold "  \
            "-slant italic -underline 0 -overstrike 0"

        top.geometry("536x468+663+322")
        top.title("Kinect Animator")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        def show_video():
            selected_action = self.lstAction.get(ANCHOR)
            if(selected_action not in depth_data_visualizer_support.actions_list): return
            action_index = depth_data_visualizer_support.actions_list.index(selected_action) + 1

            selected_subject = self.lstSubject.get(ANCHOR)
            if(selected_subject not in depth_data_visualizer_support.subjects_list): return
            subject_index = depth_data_visualizer_support.subjects_list.index(selected_subject) + 1

            selected_trial = self.lstTrial.get(ANCHOR)
            if(selected_trial not in depth_data_visualizer_support.trials_list): return
            trial_index = depth_data_visualizer_support.trials_list.index(selected_trial) + 1

            print(f'Animate (action={action_index}, subject={subject_index}, trial={trial_index})')
            animate_depth_data(action_index, subject_index, trial_index)

        self.btnVideo = Button(top)
        self.btnVideo.place(relx=0.69, rely=0.58, height=41, width=96)
        self.btnVideo.configure(activebackground="#d9d9d9")
        self.btnVideo.configure(activeforeground="#000000")
        self.btnVideo.configure(background="#d9d9d9")
        self.btnVideo.configure(disabledforeground="#a3a3a3")
        self.btnVideo.configure(foreground="#000000")
        self.btnVideo.configure(highlightbackground="#d9d9d9")
        self.btnVideo.configure(highlightcolor="black")
        self.btnVideo.configure(pady="0")
        self.btnVideo.configure(text='''Show''')
        self.btnVideo.configure(command=show_video)

        self.lstAction = Listbox(top)
        self.lstAction.place(relx=0.07, rely=0.09, relheight=0.38, relwidth=0.83)

        self.lstAction.configure(background="white")
        self.lstAction.configure(disabledforeground="#a3a3a3")
        self.lstAction.configure(font=font12)
        self.lstAction.configure(foreground="#000000")
        self.lstAction.configure(highlightbackground="#d9d9d9")
        self.lstAction.configure(highlightcolor="black")
        self.lstAction.configure(selectbackground="#c4c4c4")
        self.lstAction.configure(selectforeground="black")
        self.lstAction.configure(width=444)
        self.lstAction.configure(listvariable=depth_data_visualizer_support.action)
        self.lstAction.configure(exportselection=False)
        for item in depth_data_visualizer_support.actions_list:
            self.lstAction.insert(END, item)

        self.lstSubject = Listbox(top)
        self.lstSubject.place(relx=0.07, rely=0.56, relheight=0.38, relwidth=0.23)
        self.lstSubject.configure(background="white")
        self.lstSubject.configure(disabledforeground="#a3a3a3")
        self.lstSubject.configure(font=font12)
        self.lstSubject.configure(foreground="#000000")
        self.lstSubject.configure(highlightbackground="#d9d9d9")
        self.lstSubject.configure(highlightcolor="black")
        self.lstSubject.configure(selectbackground="#c4c4c4")
        self.lstSubject.configure(selectforeground="black")
        self.lstSubject.configure(width=124)
        self.lstSubject.configure(listvariable=depth_data_visualizer_support.subject)
        self.lstSubject.configure(exportselection=False)
        for item in depth_data_visualizer_support.subjects_list:
            self.lstSubject.insert(END, item)

        self.lstTrial = Listbox(top)
        self.lstTrial.place(relx=0.35, rely=0.56, relheight=0.38, relwidth=0.23)
        self.lstTrial.configure(background="white")
        self.lstTrial.configure(disabledforeground="#a3a3a3")
        self.lstTrial.configure(font=font12)
        self.lstTrial.configure(foreground="#000000")
        self.lstTrial.configure(highlightbackground="#d9d9d9")
        self.lstTrial.configure(highlightcolor="black")
        self.lstTrial.configure(selectbackground="#c4c4c4")
        self.lstTrial.configure(selectforeground="black")
        self.lstTrial.configure(width=124)
        self.lstTrial.configure(listvariable=depth_data_visualizer_support.trial)
        self.lstTrial.configure(exportselection=False)
        for item in depth_data_visualizer_support.trials_list:
            self.lstTrial.insert(END, item)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.07, rely=0.02, height=27, width=62)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font13)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Actions''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.35, rely=0.49, height=26, width=65)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font13)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Trials''')
        self.Label2.configure(width=65)

        self.Label3 = Label(top)
        self.Label3.place(relx=0.07, rely=0.49, height=26, width=55)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font13)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Subjects''')

        self.btnQuit = Button(top)
        self.btnQuit.place(relx=0.69, rely=0.71, height=41, width=96)
        self.btnQuit.configure(activebackground="#d9d9d9")
        self.btnQuit.configure(activeforeground="#000000")
        self.btnQuit.configure(background="#d9d9d9")
        self.btnQuit.configure(disabledforeground="#a3a3a3")
        self.btnQuit.configure(foreground="#000000")
        self.btnQuit.configure(highlightbackground="#d9d9d9")
        self.btnQuit.configure(highlightcolor="black")
        self.btnQuit.configure(pady="0")
        self.btnQuit.configure(text='''Quit''')
        self.btnQuit.configure(command=depth_data_visualizer_support.destroy_window)

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

if __name__ == '__main__':
    vp_start_gui()


