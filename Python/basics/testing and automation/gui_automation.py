import pyautogui
import keyboard

screen_width, screen_height = pyautogui.size()
print(screen_height, screen_width)

pyautogui.moveTo(100, 100, duration=1)
pyautogui.click(200, 200)
pyautogui.dragTo(300, 300, duration=2)
pyautogui.write("hello world", intercal=0.1)
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "c")

screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")

x, y = pyautogui.position()
print("pos: ",x, y)

# keyboard
keyboard.press_and_release("shift+a, space")
keyboard.write("hello")

def custom_action():
    print("custom")

keyboard.add_hotkey("ctrl+a+h", custom_action)
print("press crl-alt-h")
keyboard.wait("esc")

