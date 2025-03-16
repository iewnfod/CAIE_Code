$ErrorActionPreference = 'Stop' # stop on all errors

$packageName = 'CAIE_Code'

Write-Output "Selecting Source ..."
$response = Invoke-WebRequest -Uri "https://cdn.createchstudio.com/cdn-cgi/trace" -UseBasicParsing
$location = ($response.Content -split "`n" | Where-Object { $_ -match "^loc=" }) -replace "loc=",""

if ($location -eq "CN") {
    $url = "http://github.createchstudio.com/https://github.com/iewnfod/CAIE_Code/archive/refs/heads/stable.zip"
} else {
    $url = "https://github.com/iewnfod/CAIE_Code/archive/refs/heads/stable.zip"
}

$toolsdir = "$env:LOCALAPPDATA\CAIE_Code"

$packageargs = @{
    packagename   = $packagename
    unzipLocation = $toolsdir
    url           = $url
    checksumType  = 'sha256'
}

Install-ChocolateyZipPackage @packageargs

Install-ChocolateyPath "$toolsdir\CAIE_Code-stable\bin" -PathType 'User'

git config --global --add safe.directory "$toolsdir\CAIE_Code-stable"
