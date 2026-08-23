# Simple HTTP server for local testing
$port = 8000
$root = "D:\rex_archive\docs"

function Get-ContentType($path) {
    $ext = [System.IO.Path]::GetExtension($path)
    switch ($ext) {
        ".html" { return "text/html; charset=utf-8" }
        ".json" { return "application/json" }
        ".md" { return "text/plain; charset=utf-8" }
        ".css" { return "text/css" }
        ".js" { return "application/javascript" }
        ".jpg" { return "image/jpeg" }
        ".gif" { return "image/gif" }
        ".png" { return "image/png" }
        ".pdf" { return "application/pdf" }
        ".mp3" { return "audio/mpeg" }
        ".mp4" { return "video/mp4" }
        default { return "application/octet-stream" }
    }
}

Write-Host "Starting server on http://localhost:$port"
Write-Host "Press Ctrl+C to stop"
Write-Host ""

$listener = [System.Net.HttpListener]::new()
$listener.Prefixes.Add("http://localhost:$port/")
$listener.Start()

while ($listener.IsListening) {
    $context = $listener.GetContext()
    $request = $context.Request
    $response = $context.Response

    $path = $request.Url.LocalPath
    if ($path -eq "/") { $path = "/index.html" }

    # URL-decode the path
    $path = [System.Uri]::UnescapeDataString($path)
    $filePath = Join-Path $root $path.TrimStart("/")

    if (Test-Path -LiteralPath $filePath -PathType Leaf) {
        $bytes = [System.IO.File]::ReadAllBytes($filePath)
        $response.ContentType = Get-ContentType $path
        $response.ContentLength64 = $bytes.Length
        $response.OutputStream.Write($bytes, 0, $bytes.Length)
    } else {
        $response.StatusCode = 404
        $responseText = "Not found: $path"
        $bytes = [System.Text.Encoding]::UTF8.GetBytes($responseText)
        $response.OutputStream.Write($bytes, 0, $bytes.Length)
    }

    $response.Close()
    Write-Host "[$(Get-Date -Format 'HH:mm:ss')] $path"
}
