# 📚 App de Aprendizaje de Inglés con Método Campayo

## 🧠 Descripción del Proyecto

Esta aplicación tiene como objetivo enseñar inglés utilizando el método **Campayo**, basado en:

- **Visualización mnemotécnica**
- **Clasificación por tipo de palabra y dificultad**
- **Pronunciación activa**
- **Fases de repetición y repaso**

El contenido se presenta en **tablas temáticas** clasificadas por tipo de palabra (verbos, sustantivos, adjetivos, adverbios, etc.) y por **nivel de dificultad** (1000 palabras más comunes en adelante).

---

## 📋 Estructura de las Tablas

Cada tabla corresponde a un grupo temático o gramatical (ej. “Adverbios de frecuencia”, “Pronombres personales”). Cada fila contiene:

1. **Palabra en inglés**
2. **Pronunciación fonética**
3. **Traducción al español**
4. **Campo visualización** (imagen o frase mnemotécnica asociada)

---

## 🌀 Fases del Aprendizaje

1. **Aprendizaje / Visualización**
   - Se muestra palabra, pronunciación, traducción e imagen.
   - Avance controlado línea por línea.

2. **Comprensión sonora**
   - Se escucha el audio y se asocia con la traducción o imagen.

3. **Sombra (shadowing)**
   - Se escucha y repite la palabra de forma activa.

4. **Repaso**
   - Test activo de recuerdo sin mostrar todos los campos.

Cada fase altera lo que se muestra/interactúa en pantalla.

---

## 🔊 Audio y Visualización

- El botón de pronunciación reproduce audio (usando TTS o audios precargados).
- La visualización muestra **una imagen generada por IA** que ilustra la palabra con una técnica mnemotécnica.
  
---

## 💡 Características clave

- Navegación por tema, tipo de palabra y nivel.
- Tablas interactivas que se desbloquean progresivamente.
- Almacenamiento de progreso.
- Posibilidad de expansión con frases, oraciones compuestas, reglas gramaticales, etc.

---

## 🧱 Estado actual

- ✔ 1000 palabras clasificadas por tipo y tema en `.csv` y `.xlsx`.
- ✔ Plan pedagógico definido.
- 🚧 Desarrollo de prototipo en fase inicial.

---

## 💰 Viabilidad y Monetización

- ✅ Alta viabilidad técnica (React Native, Flutter, Web App).
- 💵 Monetizable mediante:
  - Versión freemium (algunas tablas gratuitas).
  - Suscripción mensual/pago único.
  - Venta por módulos temáticos.
- 📦 Tamaño aproximado (con audios e imágenes locales): 150–200 MB.

---

## 🔧 Próximos pasos

1. **Conversión de datos CSV a tablas Excel** por tipo de palabra.
2. **Prototipo de App/Web App** con tabla navegable y reproducción de audio.
3. **Generación de imágenes IA y audios** (TTS o precargados).
4. **Definición de fases de aprendizaje interactivas.**
5. **Prueba con usuarios reales.**
6. **Publicación y monetización.**

---

## 🔨 Tecnologías planeada

- **Frontend**: React, React Native o Flutter
- **Backend**: Firebase / Supabase / Django (para usuarios y progreso)
- **Audio**: TTS (gTTS, Amazon Polly, etc.) o archivos precargados
- **Imagen IA**: DALL·E, MidJourney, Stable Diffusion
- **Exportación**: Python (`pandas` + `openpyxl` para convertir `.csv` a `.xlsx`)

---


# 📚 English Learning App Based on Thematic Tables

## 🧠 Project Description

This application aims to teach English through a method based on:

- **Mnemonic visualization**
- **Classification by word type and difficulty**
- **Active pronunciation**
- **Repetition and review phases**

The content is presented in **thematic tables** organized by word type (verbs, nouns, adjectives, adverbs, etc.) and **difficulty level** (starting with the 1000 most common words).

---

## 📋 Table Structure

Each table corresponds to a thematic or grammatical group (e.g., “Frequency adverbs”, “Personal pronouns”). Each row contains:

1. **English word**
2. **Phonetic pronunciation**
3. **Spanish translation**
4. **Visualization field** (mnemonic phrase or generated image)

---

## 🌀 Learning Phases

1. **Learning / Visualization**
   - Shows word, pronunciation, translation, and image.
   - Progress is controlled line by line.

2. **Listening comprehension**
   - User hears the audio and links it to translation or image.

3. **Shadowing**
   - The word is heard and actively repeated.

4. **Review**
   - Active recall test without displaying all the fields.

Each phase modifies the way content is shown and interacted with.

---

## 🔊 Audio & Visualization

- Pronunciation button plays the audio (using TTS or preloaded files).
- Visualization displays an **AI-generated image** illustrating the mnemonic concept.

---

## 💡 Key Features

- Navigation by theme, word type, and difficulty.
- Interactive tables unlocked progressively.
- Progress tracking and user history.
- Expandable to include phrases, compound sentences, grammar rules, etc.

---

## 🧱 Current Status

- ✔ 1000 categorized words in `.csv` and `.xlsx`.
- ✔ Learning method fully defined.
- 🚧 Prototype development in early stages.

---

## 💰 Viability & Monetization

- ✅ High technical viability (React Native, Flutter, or Web App).
- 💵 Monetization options:
  - Freemium model (some free tables).
  - Monthly subscription or one-time purchase.
  - Sale of thematic content packs.
- 📦 Estimated size (with local audios and images): 150–200 MB.

---

## 🔧 Next Steps

1. **Convert CSV to categorized Excel files**.
2. **Build an App/Web prototype** with interactive table and audio playback.
3. **Generate AI images and audios** (via TTS or preloaded files).
4. **Define interactive learning phases**.
5. **Conduct user testing**.
6. **Launch and monetize**.

---

## 🔨 Planned Tech Stack

- **Frontend**: React, React Native, or Flutter  
- **Backend**: Firebase / Supabase / Django (for user and progress tracking)  
- **Audio**: TTS (gTTS, Amazon Polly, etc.) or local audio files  
- **AI Image**: DALL·E, MidJourney, Stable Diffusion  
- **Data Processing**: Python (`pandas` + `openpyxl` to convert `.csv` to `.xlsx`)  
