# Kompliment App

Lille PWA der viser tilfældige komplimenter. Kører helt i browseren — ingen backend.

## Live URL

Når GitHub Pages er aktiveret:

**https://nis-knowit.github.io/Kompliment-App/Kompliment.html**

## Aktivér GitHub Pages (engangsopsætning)

1. Gå til repo → Settings → Pages
2. Source: **Deploy from a branch**
3. Branch: **main** / **/** (root)
4. Save

Efter et par minutter er siden live på URL'en ovenfor.

## Installér på Android

1. Åbn URL'en i Chrome
2. Menu (⋮) → **Tilføj til startskærm** / **Installér app**
3. App'en virker offline efter første åbning (service worker cacher alt)

## Installér på iPhone

1. Åbn URL'en i Safari
2. Del-knap → **Føj til hjemmeskærm**

## Filer

- `Kompliment.html` — selve app'en (HTML + CSS + JS i én fil)
- `manifest.webmanifest` — gør det installerbart som PWA
- `sw.js` — service worker for offline-support
- `icon.svg` — app-ikon

## Tilføj flere komplimenter

Rediger `KOMPLIMENTER`-arrayet i `Kompliment.html`. Commit og push — service workeren henter den nye version automatisk næste gang app'en åbnes online.
