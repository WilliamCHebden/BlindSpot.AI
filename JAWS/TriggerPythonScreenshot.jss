; JAWS Script to trigger Python script on Print Screen key press

Include "hjconst.jsh"
Include "hjglobal.jsh"

Script TriggerPythonScreenshot ()
    SayString("Triggering screenshot analysis.")
    
    ; Call the Python script using the "Run" function
    If FileExists("C:\\path\\to\\your\\script\\screenshot_script.py") Then
        Run("python C:\\path\\to\\your\\script\\screenshot_script.py")
    Else
        SayString("Python script not found.")
    EndIf
EndScript

; Bind the JAWS script to the "Print Screen" key
KeyPressedEvent("print screen", TriggerPythonScreenshot)
