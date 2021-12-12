def abs_to_rela(x1, y1, x2, y2):  # converts 2 absolute points to 1 and a width/height
    return x1, y1, x2 - x1, y2 - y1


def rela_to_abs(x, y, w, h):
    return x, y, x+w, y+h


def grab_snippet(mouse1, mouse2):
    import pyautogui
    from os.path import exists

    num = 1
    while exists("saved_images/new_image_" + str(num) + ".png"):
        num += 1
    return pyautogui.screenshot(region=abs_to_rela(mouse1[0], mouse1[1], mouse2[0], mouse2[1])).save(
        ("saved_images/new_image_" + str(num) + ".png"))


