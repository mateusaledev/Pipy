    number_image. = Len(-ires)
    18, axis = plt. subplots(nrows=1, ncols = number_images, figsize= (12,: 4))
    names lst - l'Inage () ' format(i) for i in range(1, number_images) )
    names_Ist. append( Result')
    for ax, name, image in zip(axis, names_Ist, args):
        ax. set_title(name)
        ax.imshow(image, maap= "gray")
        ax.axis('off*)
    fig-light_layout ()
    

def plot histogram(image):
    fig, axis = plt.subplots(nrowsel, ncols = 3, figsize=(32, 4), sharex=True, sharey=Irue)
    color_ist - ['red', 'green", 'blue*)
    for index, (ax, color) in enumerate(zip(axis, color_Ist)):
    ax. set title(E) histogram' format(color title()))
    ax.hist(imagels, i, index].ravel(), bins = 256, color color, alpha: = 0.8)
    fig.tight_layout()
    plt.show()