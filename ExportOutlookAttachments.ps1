# This script exports pdf attachments from Outlook from selected folder
$o = New-Object -comobject outlook.application
$n = $o.GetNamespace("MAPI")
$f = $n.PickFolder()
$filepath = "c:\temp\pdfs"
$counter = 400
$f.Items| foreach {
    $_.attachments|foreach {
		$counter--
		$a = $_.filename
		If ($a.EndsWith(".pdf")) {
            $fileName = "\" + $a.Split('.')[0] + "\"  # Take file name without extension
            
            $destinationDirName = $filepath +  $fileName
            if(!(Test-Path -Path $destinationDirName )){
                Write-Host "Creating folder file:"  $destinationDirName
                New-Item -ItemType directory -Path $destinationDirName
            }

            $destinationFileName = $destinationDirName + $counter + "_" + $a

            Write-Host "Saving file:"  $destinationFileName
			$_.saveasfile($destinationFileName)
		}
	}
}
