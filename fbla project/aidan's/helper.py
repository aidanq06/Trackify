def open_help_window():
    def close_help_window():
        help_frame.place_forget()
        help_button['image'] = help_image

    if (help_button.cget('image')=='pyimage2'):
        help_frame.place(x= 1800, y= 25, anchor=NE)
        help_button['image'] = help2_image
    else:
        close_help_window()