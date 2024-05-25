import cv2
import numpy as np
import time

from fontprint import font_data

def draw_char(image, char, x, y, scale=1, color=(0, 255, 0)):
    if char in font_data:
        font = font_data[char]
        for i, row in enumerate(font):
            for j, pixel in enumerate(row):
                if pixel == "#":
                    cv2.rectangle(image, 
                                  (x + j*scale, y + i*scale), 
                                  (x + (j+1)*scale - 1, y + (i+1)*scale - 1), 
                                  color, 
                                  -1)

def display_text_charactor_manner(image, text, x, y, scale=1, color=(0, 255, 0), delay=0.1):
    start_x = x
    for char in text:
        if char == "\n":
            y += 7 * scale
            x = start_x
        else:
            draw_char(image, char, x, y, scale, color)
            x += 6 * scale
            cv2.imshow("VFD_Simulator", image)
            cv2.waitKey(int(delay * 1000))

def display_text(image, text, x, y, scale=1, color=(0, 255, 0)):
    start_x = x
    for char in text:
        if char == "\n":
            y += 7 * scale
            x = start_x
        else:
            draw_char(image, char, x, y, scale, color)
            x += 6 * scale


def main():
    # 获取显示器信息并创建窗口
    display_width = 1280
    display_height = 400
    screen_x_offset = 0  # Assuming each monitor is 1920 pixels wide
    screen_y_offset = -1000

    # 创建黑色背景的全屏窗口
    cv2.namedWindow("VFD_Simulator", cv2.WND_PROP_FULLSCREEN)
    cv2.moveWindow("VFD_Simulator", screen_x_offset, screen_y_offset)
    cv2.setWindowProperty("VFD_Simulator", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    while True:
        text = "......................................................\n......................................................\n......................................................\n......................................................\n......................................................\n......................................................\n......................................................\n......................................................\n......................................................\n......................................................\n......................................................\n......................................................\n......................................................\n......................................................\n"
        image = np.zeros((display_height, display_width, 3), dtype=np.uint8)
        display_text_charactor_manner(image, text, 10, 10, scale=4, delay=0.001)
        if cv2.waitKey(500) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            exit(0)


        text = "INIT... FF PASSED\n"
        image = np.zeros((display_height, display_width, 3), dtype=np.uint8)
        display_text_charactor_manner(image, text, 10, 10, scale=4, delay=0.1)
        if cv2.waitKey(500) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            exit(0)

        cv2.imshow("VFD_Simulator", image)
        if cv2.waitKey(500) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            exit(0)

        text = "INNOVATION IN CANADA\nTHIS WILL BE AN OPEN SOURCE PROJECT\nUNDER CC LICENSE @ REALTENSOR"
        image = np.zeros((display_height, display_width, 3), dtype=np.uint8)
        display_text(image, text, 10, 100, scale=4)
        cv2.imshow("VFD_Simulator", image)
        if cv2.waitKey(1000) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            exit(0)

        # 闪烁效果
        for _ in range(5):
            image = np.zeros((display_height, display_width, 3), dtype=np.uint8)
            cv2.imshow("VFD_Simulator", image)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                exit(0)
            display_text(image, text, 10, 100, scale=4)
            cv2.imshow("VFD_Simulator", image)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                exit(0)

        text = "WE SHALL BE AS A CITY UPON A HILL\n--THE EYES OF ALL PEOPLE ARE UPON US."
        image = np.zeros((display_height, display_width, 3), dtype=np.uint8)
        display_text_charactor_manner(image, text, 10, 100, scale=4)
        cv2.imshow("VFD_Simulator", image)
        if cv2.waitKey(2000) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            exit(0)


        text = "EINIGKEIT UND RECHT UND FREIHEIT.\nUNITY AND JUSTICE AND FREEDOM."
        image = np.zeros((display_height, display_width, 3), dtype=np.uint8)
        display_text_charactor_manner(image, text, 10, 100, scale=4)
        cv2.imshow("VFD_Simulator", image)
        if cv2.waitKey(2000) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            exit(0)

        
        text = "A QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
        for i in range(8):
            image = np.zeros((display_height, display_width, 3), dtype=np.uint8)
            display_text(image, text, 10, 10 + i * 50, scale=4)
            cv2.imshow("VFD_Simulator", image)
            if cv2.waitKey(1000) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                exit(0)

        # 退出条件
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            exit(0)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
