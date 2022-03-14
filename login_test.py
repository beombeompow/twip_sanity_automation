import pyautogui as pag
import time
import keyboard
import threading as th

keep_going = True
def key_capture_thread():
    global keep_going
    a = keyboard.read_key()

    if a== "q":
        keep_going = False


def main():
    th.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()

    while keep_going:
        center = pag.locateCenterOnScreen('streamer_login.png')
        
        if center is not None:
            pag.click(center)
            time.sleep(1)

            pag.click(center)
            time.sleep(5)

            center = pag.locateCenterOnScreen('already_id_pw.png')
            
            center = pag.locateCenterOnScreen('already_id_pw.png')
            
            if center is None:
                center = pag.locateCenterOnScreen('if_double_clicked_at_login.png')

            if center is not None:
                pag.click(center)
                time.sleep(0.3)

                center = pag.locateCenterOnScreen('login.png')
                
                if center is not None:
                    pag.click(center)
                    time.sleep(0.3)


                    center = pag.locateCenterOnScreen('gmail.png')
                    
                    if center is not None:
                        pag.click(center)
                        time.sleep(60)
                        
                        center = pag.locateCenterOnScreen('login_mail.png')
                        
                        if center is not None:
                            pag.click(center)
                            time.sleep(0.3)
                            pag.press('down')
                            pag.press('down')
                            pag.press('down')
                            pag.press('down')
                            pag.press('down')
                            center = pag.locateCenterOnScreen('find_code.png')
                            
                            if center is not None:
                                x, y = center
                                y = y + 55

                                center = (x,y)
                                pag.doubleClick(center)
                                pag.keyDown('ctrl')
                                pag.press('c')
                                pag.keyUp('ctrl')

        time.sleep(0.1)

if __name__ == "__main__":
    main()
