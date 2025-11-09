import speech_recognition as sr
import pyttsx3
import pyautogui
import webbrowser
import os
import subprocess
import time
import psutil

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speaking rate

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            print("Speech recognition service is down.")
            return ""
        except AttributeError as e:
            print(f"AttributeError: {e}")
            return ""

# Kill running process (if necessary) before reopening
def kill_process(process_name):
    for proc in psutil.process_iter():
        if process_name.lower() in proc.name().lower():
            proc.kill()
            time.sleep(1)

def open_application(app_name):
    try:
        if app_name == "whatsapp":
            kill_process("whatsapp.exe")
            subprocess.Popen("shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App")
        elif app_name == "asphalt":
            kill_process("asphalt9.exe")
            subprocess.Popen("shell:AppsFolder\\A278AB0D.Asphalt9_h6adky7gbf63m!App")
        elif app_name == "chrome":
            kill_process("chrome.exe")
            os.system("start chrome")
        elif app_name == "notepad":
            kill_process("notepad.exe")
            os.system("start notepad")
        elif app_name == "vscode":
            kill_process("code.exe")
            os.system("start code")
        else:
            speak(f"Application {app_name} not recognized.")
    except Exception as e:
        speak(f"Failed to open {app_name}. Error: {e}")

def open_website(url):
    speak(f"Opening {url}")
    webbrowser.open(url)

def shutdown():
    speak("Shutting down the computer")
    os.system("shutdown /s /f /t 0")

def restart():
    speak("Restarting the computer")
    os.system("shutdown /r /f /t 0")

def calculate(expression):
    try:
        result = eval(expression)
        speak(f"The result is {result}")
        print(f"Result: {result}")
    except Exception as e:
        speak(f"Error: {e}")
        print(f"Error: {e}")

def main():
    speak("Hello Barry, I'm ready!")
    while True:
        command = listen()

        if "open notepad" in command:
            open_application("notepad")
        elif "open chrome" in command:
            open_application("chrome")
        elif "open whatsapp" in command:
            open_application("whatsapp")
        elif "open asphalt" in command:
            open_application("asphalt")
        elif "open vscode" in command:
            open_application("vscode")
        elif "open youtube" in command:
            open_website("https://www.youtube.com")
        elif "shutdown" in command:
            shutdown()
        elif "restart" in command:
            restart()
        elif "calculate" in command:
            expression = command.replace("calculate", "").strip()
            calculate(expression)
        elif "stop" in command or "exit" in command:
            speak("Goodbye Barry!")
            break
        else:
            speak("Command not recognized.")

if __name__ == "__main__":
    main()
