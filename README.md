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

Hver gang knappen trykkes, ruller app'en en terning:

- **76% normal kompliment** med svævende hjerter
- **10% Balder-overraskelse** &mdash; bronzefarvet baggrund, billede af Balder, og sm&aring; pote-aftryk der svaever op
- **10% Lykke-overraskelse** &mdash; rosa baggrund, billede af jer to, og ekstra hjerter
- **4% kupon** &mdash; styled som et kupon-kort. Tryk **"Indl&oslash;s"** for at sende kuponen direkte via Messenger (eller hvilken som helst messaging-app via Web Share API). Indl&oslash;ste kuponer kommer ikke igen f&oslash;r alle er brugt.

Sandsynlighederne kan justeres &oslash;verst i `<script>`-blokken: `KUPON_CHANCE`, `BALDER_CHANCE`, `LYKKE_CHANCE`.

## Tilføj flere komplimenter eller kuponer

Rediger `KOMPLIMENTER`- eller `KUPONER`-arrayet i `Kompliment.html`. Commit og push — service workeren henter den nye version automatisk næste gang app'en åbnes online.

Bump også `CACHE`-konstanten i `sw.js` (fx `komplimenter-v3`) når du laver ændringer, så de gamle filer ikke serveres fra cache.

## Tilføj eller udskift billeder

1. Smid nye billeder (HEIC, JPG, PNG) i `balder/` eller `lykke/`
2. Kør konverteringsscriptet:
   ```
   py scripts/convert_photos.py
   ```
   Det laver web-optimerede `-web.jpg`-versioner ved siden af originalerne (resized til max 1200px, ~80% kvalitet).
3. Tilføj de nye `-web.jpg`-stier til `BALDER_BILLEDER` eller `LYKKE_BILLEDER` i `Kompliment.html`.
4. Bump `CACHE`-konstanten i `sw.js` (fx `komplimenter-v4`) og push.

Originalerne er ekskluderet via `.gitignore` — kun de optimerede `-web.jpg`-versioner pushes til repoet.
