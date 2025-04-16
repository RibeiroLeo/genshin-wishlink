# Genshin Wish Link Fetcher (Offline Friendly)

# O Script Principal é feito todo pelo MadeBaruna, este é apenas um reply preguiçoso.

Este script PowerShell tenta extrair o link do histórico de desejos do Genshin Impact de forma automática.

## 🧠 Como funciona:

1. Primeiro ele tenta ler o link de um arquivo `.wishlink`.
2. Se não achar, tenta extrair dos logs do jogo usando o script do MadeBaruna.

## 🚀 Como usar:

```bash
powershell -ExecutionPolicy Bypass -File .\getWishLink.ps1

