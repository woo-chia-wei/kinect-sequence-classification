import sys
from tkinter import *
import tkinter.ttk as ttk

def set_Tk_var():
    global action
    action = StringVar()
    global subject
    subject = StringVar()
    global trial
    trial = StringVar()
    global actions_list
    actions_list = ['1. right arm swipe to the left',
                    '2. right arm swipe to the right',
                    '3. right hand wave',
                    '4. two hand front clap',
                    '5. right arm throw',
                    '6. cross arms in the chest',
                    '7. basketball shooting',
                    '8. draw x',
                    '9. draw circle (clockwise)',
                    '10. draw circle (counter clockwise)',
                    '11. draw triangle',
                    '12. bowling (right hand)',
                    '13. front boxing',
                    '14. baseball swing from right',
                    '15. tennis forehand swing',
                    '16. arm curl (two arms)',
                    '17. tennis serve',
                    '18. two hand push',
                    '19. knock on door',
                    '20. hand catch',
                    '21. pick up and throw',
                    '22. jogging',
                    '23. walking',
                    '24. sit to stand',
                    '25. stand to sit',
                    '26. forward lunge (left foot forward)',
                    '27. squat']
    global subjects_list
    subjects_list = ['1. Female 1',
                    '2. Female 2',
                    '3. Female 3',
                    '4. Female 4',
                    '5. Male 1',
                    '6. Male 2',
                    '7. Male 3',
                    '8. Male 4']
    global trials_list
    trials_list = ['1. Trial 1',
                    '2. Trial 2',
                    '3. Trial 3',
                    '4. Trial 4']

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import depth_data_visualizer
    depth_data_visualizer.vp_start_gui()

