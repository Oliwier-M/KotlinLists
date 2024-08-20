import nib
import numpy as np
import matplotlib.pyplot as plt

img = nib.load('clinical_1_PET.nii')
img_data = img.get_fdata()

print(type(img_data))
print(img_data.dtype)
print(img_data.shape)

img_data = img_data/np.max(img_data)


def plot_slices(img_data, cmap=plt.cm.gray, vmin=0.0, vmax=1.0):
    """Plots a 3d-array-like object as roughly square 2d grid of slices.

    Args:
      img_data (3d-array-like object): intended to represent a medical image
      cmap (Colormap): Matplotlib color map, default: cm.gray
      vmin (float): minimum pixel intesity, default 0.0
      vmax (float): maximum pixel intesity, default 1.0

    Returns:
      Figure: Matplotlib figure object
    """

    ncols = int(np.ceil(img_data.shape[0]**0.5))
    nrows = int(np.ceil(img_data.shape[0]/ncols))

    fig, axes = plt.subplots(ncols=ncols, nrows=nrows,
                             constrained_layout=True)
    i = 0
    for ax in axes.flatten():
        if i < img_data.shape[0]:
            ax.imshow(img_data[i], cmap=cmap, vmin=vmin, vmax=vmax)
        ax.axis('off')
        i += 1
    return fig


plot_slices(img_data)