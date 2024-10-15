; TriggerScreenshot.jss - A JAWS Script to trigger browser extension events

Include "hjconst.jsh"
Include "hjglobal.jsh"

Script TriggerScreenshot ()
    SayString("Screenshot trigger activated.")
    
    ; Inject a hidden trigger element into the DOM for the browser extension
    If (GetCurrentAppName() == "chrome" || GetCurrentAppName() == "firefox") Then
        Let oElement = GetDocumentElement() ; Get the DOM element
        Let oNewDiv = CreateElement("div")
        SetAttribute(oNewDiv, "id", "triggerLogoImageOne")
        SetAttribute(oNewDiv, "style", "display:none;")
        AppendChild(oElement, oNewDiv)
    Else
        SayString("Browser not supported.")
    EndIf
EndScript

KeyPressedEvent("Ctrl+Shift+S", TriggerScreenshot)
