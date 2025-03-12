$toolsdir = "$(Split-Path -parent $MyInvocation.MyCommand.Definition)"
Uninstall-ChocolateyPath "$toolsdir\CAIE_Code-stable\bin" -PathType 'User'