import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax1 = fig.add_subplot(111)
# global x_data,y_data
x1 = np.arange(0, 2 * np.pi, 0.1)
y1 = np.sin(x1)
y2 = np.cos(x1)


def onEnter(event):
    event.inaxes.patch.set_facecolor('yellow')
    event.canvas.draw_idle()


def onLeave(event):
    event.inaxes.patch.set_facecolor('white')
    event.canvas.draw_idle()


def onMousePress(event):
    if event.button == 1:
        ax1.clear()
        ax1.plot(x1, y1)
        event.canvas.draw()


def onMouseRelease(event):
    if event.button == 1:
        ax1.clear()
        ax1.plot(x1, y2)
        event.canvas.draw()


def onKeyPress(event):
    if event.key == 'c':
        ax1.clear()
        ax1.plot(x1, y2)
        event.canvas.draw()
    elif event.key == 'a':
        ax1.clear()
        ax1.plot(x1, y1)
        event.canvas.draw()
    else:
        pass


fig.canvas.mpl_connect('axes_enter_event', onEnter)
fig.canvas.mpl_connect('axes_leave_event', onLeave)
fig.canvas.mpl_connect('button_press_event', onMousePress)
fig.canvas.mpl_connect('button_release_event', onMouseRelease)
fig.canvas.mpl_connect('key_press_event', onKeyPress)
fig.canvas.mpl_connect('key_press_event', onKeyPress)
plt.show()

