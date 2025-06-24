import speech_recognition as sr

# Simulated device status
devices = {
    "light": "off",
    "fan": "off"
}

def process_command(command):
    command = command.lower()
    if "light on" in command:
        devices["light"] = "on"
        print("[ACTION] Light is ON ✅")
    elif "light off" in command:
        devices["light"] = "off"
        print("[ACTION] Light is OFF ❌")
    elif "fan on" in command:
        devices["fan"] = "on"
        print("[ACTION] Fan is ON ✅")
    elif "fan off" in command:
        devices["fan"] = "off"
        print("[ACTION] Fan is OFF ❌")
    else:
        print(f"[INFO] Command not recognized: {command}")

def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Listening for voice commands... Say 'Light on', 'Light off', 'Fan on' or 'Fan off'.")

    while True:
        try:
            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio)
            print(f"[HEARD] {command}")

            process_command(command)

        except sr.UnknownValueError:
            print("[ERROR] Could not understand the audio.")
        except sr.RequestError:
            print("[ERROR] Could not request results from the service.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if _name_ == "_main_":
    main()
