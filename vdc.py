from typing import Literal
from pynput.keyboard import Listener
from pyvda import AppView, VirtualDesktop, get_virtual_desktops

pressed_keys: list = []
last_key = None


def get_pressed_keys() -> list[str]:
    return [str(x) for x in pressed_keys]


def navigate_desktops(desktop: int) -> None:
    if len(get_virtual_desktops()) >= desktop:
        VirtualDesktop(number=desktop).go()
    else:
        new_vd: VirtualDesktop = VirtualDesktop(1).create()
        new_vd.go()


def move_window_navigate_desktops(desktop: int) -> None:
    if len(get_virtual_desktops()) >= desktop:
        AppView.current().move(VirtualDesktop(desktop))
        VirtualDesktop(desktop).go()
    else:
        new_vd: VirtualDesktop = VirtualDesktop(1).create()
        AppView.current().move(VirtualDesktop(new_vd.number))
        new_vd.go()


def on_press(key) -> None:
    global last_key, pressed_keys
    if str(key) == last_key:
        return
    if str(key) in (
        "Key.alt_l",  # Left Alt
        "Key.ctrl_l",  # Left Ctrl
        "'1'",
        "'2'",
        "'3'",
        "'4'",
        "'5'",
        "'6'",
        "'7'",
        "'8'",
        "'9'",
        "'0'",
        "<49>",  # 1
        "<50>",  # 2
        "<51>",  # 3
        "<52>",  # 4
        "<53>",  # 5
        "<54>",  # 6
        "<55>",  # 7
        "<56>",  # 8
        "<57>",  # 9
        "<48>",  # 0
        "<81>",  # q
    ):
        pressed_keys.append(str(key))
    last_key = str(key)
    match get_pressed_keys():
        case ["Key.alt_l", "'1'"]:
            navigate_desktops(1)
        case ["Key.alt_l", "'2'"]:
            navigate_desktops(2)
        case ["Key.alt_l", "'3'"]:
            navigate_desktops(3)
        case ["Key.alt_l", "'4'"]:
            navigate_desktops(4)
        case ["Key.alt_l", "'5'"]:
            navigate_desktops(5)
        case ["Key.alt_l", "'6'"]:
            navigate_desktops(6)
        case ["Key.alt_l", "'7'"]:
            navigate_desktops(7)
        case ["Key.alt_l", "'8'"]:
            navigate_desktops(8)
        case ["Key.alt_l", "'9'"]:
            navigate_desktops(9)
        case ["Key.alt_l", "'0'"]:
            navigate_desktops(10)
        case ["Key.alt_l", "Key.ctrl_l", "<49>"]:
            move_window_navigate_desktops(1)
        case ["Key.alt_l", "Key.ctrl_l", "<50>"]:
            move_window_navigate_desktops(2)
        case ["Key.alt_l", "Key.ctrl_l", "<51>"]:
            move_window_navigate_desktops(3)
        case ["Key.alt_l", "Key.ctrl_l", "<52>"]:
            move_window_navigate_desktops(4)
        case ["Key.alt_l", "Key.ctrl_l", "<53>"]:
            move_window_navigate_desktops(5)
        case ["Key.alt_l", "Key.ctrl_l", "<54>"]:
            move_window_navigate_desktops(6)
        case ["Key.alt_l", "Key.ctrl_l", "<55>"]:
            move_window_navigate_desktops(7)
        case ["Key.alt_l", "Key.ctrl_l", "<56>"]:
            move_window_navigate_desktops(8)
        case ["Key.alt_l", "Key.ctrl_l", "<57>"]:
            move_window_navigate_desktops(9)
        case ["Key.alt_l", "Key.ctrl_l", "<48>"]:
            move_window_navigate_desktops(10)


def on_release(key) -> None | Literal[False]:
    global last_key, pressed_keys
    # Stop listener if "Key.alt_l", "Key.ctrl_l", "<81>"] is pressed, which is Left Alt + Left Ctrl + q
    if get_pressed_keys() == ["Key.alt_l", "Key.ctrl_l", "<81>"]:
        return False
    # Removes keys from pressed key list
    if str(key) in get_pressed_keys():
        pressed_keys.remove(str(key))
    if str(key) == last_key:
        last_key = pressed_keys[-1] if len(pressed_keys) > 0 else None


# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
