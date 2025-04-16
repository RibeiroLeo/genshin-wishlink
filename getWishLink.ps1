# Caminho do arquivo onde o link vai ser salvo
$linkFile = "$PSScriptRoot\.wishlink"

# Função para tentar ler o link salvo
function Get-SavedWishLink {
    if (Test-Path $linkFile) {
        $link = Get-Content $linkFile -Raw
        if ($link -match "^https:\/\/") {
            Write-Host "✅ Link salvo encontrado:" -ForegroundColor Green
            Write-Host $link
            return $true
        }
    }
    return $false
}

# Se não achar o link salvo, tenta usar o script do MadeBaruna
function Get-WishLinkFromLogs {
    Write-Host "🔍 Buscando link nos logs..." -ForegroundColor Yellow
    iex "&{$((New-Object System.Net.WebClient).DownloadString('https://gist.githubusercontent.com/MadeBaruna/1d75c1d37d19eca71591ec8a31178235/raw/getlink.ps1'))} global" | Tee-Object -Variable output
    if ($output -match "https:\/\/.+") {
        $url = ($output -split "`n") | Where-Object { $_ -match "^https:\/\/" }
        if ($url) {
            $url | Out-File -Encoding utf8 -FilePath $linkFile
            Write-Host "💾 Link salvo para uso futuro em '.wishlink'."
        }
    } else {
        Write-Host "❌ Não foi possível extrair o link automaticamente." -ForegroundColor Red
    }
}

# Execução
if (-not (Get-SavedWishLink)) {
    Get-WishLinkFromLogs
}
