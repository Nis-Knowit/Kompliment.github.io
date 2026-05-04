# Kompliment App

Lille PWA der viser tilfældige komplimenter. Kører helt i browseren — ingen backend.

## Live URL

Når GitHub Pages er aktiveret:

**https://nis-knowit.github.io/Kompliment.github.io/Kompliment.html**

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
- `balder/` — billeder af Balder (placeholder ligger der allerede)

## Features

- **Komplimenter**: tryk på knappen — få en tilfældig kompliment med svævende hjerter
- **Balder-tilstand**: tryk på paw-ikonet i hjørnet — filtrerer til kun Balder-komplimenter og viser hans billede
- **Kupon-chance**: ~8% chance per tryk for at få en kupon i stedet for en kompliment (kan indløses i virkeligheden)

## Tilføj flere komplimenter eller kuponer

Rediger `KOMPLIMENTER`- eller `KUPONER`-arrayet i `Kompliment.html`. Commit og push — service workeren henter den nye version automatisk næste gang app'en åbnes online.

Bump også `CACHE`-konstanten i `sw.js` (fx `komplimenter-v3`) når du laver ændringer, så de gamle filer ikke serveres fra cache.

## Tilføj rigtige billeder af Balder

1. Læg JPG/PNG-billeder i `balder/`-mappen, fx `balder/01.jpg`, `balder/02.jpg`, ...
2. Tilføj filnavnene til `BALDER_BILLEDER`-arrayet i `Kompliment.html`:
   ```js
   const BALDER_BILLEDER = [
     'balder/01.jpg',
     'balder/02.jpg',
     'balder/03.jpg'
   ];
   ```
3. Tilføj de samme stier til `ASSETS`-arrayet i `sw.js` så de cacher offline.
4. Bump `CACHE`-versionen og push.

Et tilfældigt billede vælges hver gang Balder-tilstanden tændes.
