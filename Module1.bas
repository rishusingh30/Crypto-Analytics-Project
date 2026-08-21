Attribute VB_Name = "Module1"
Sub CheckWorkingHours()

    Dim currentTime As Date
    Dim cht As ChartObject

    Set cht = ActiveSheet.ChartObjects(1)

    currentTime = Time

    If currentTime >= TimeValue("09:00:00") And currentTime <= TimeValue("17:00:00") Then

        cht.Visible = True

    Else

        cht.Visible = False

        MsgBox "Please open in working hours (9 am to 5 pm).", _
               vbExclamation, "Crypto Dashboard"

    End If

End Sub

