
# Lyrics Writer

## When to Use
- The user asks you to write song lyrics, e.g. "write lyrics about...", "write a song for...".
- The user runs `/lyrics-writer`.

## Procedure
1. Identify the key parameters from the request (ask only if truly ambiguous, otherwise infer sensible defaults):
   - **Topic/theme** — what the song is about.
   - **Genre/style** — e.g. pop, rock, country, hip-hop, folk, ballad. Default to a flexible, generic pop/folk style if unspecified.
   - **Mood/tone** — e.g. upbeat, melancholic, romantic, angry, hopeful.
   - **Length/structure** — default to Verse 1 / Chorus / Verse 2 / Chorus / Bridge / Chorus if not specified.
2. Write original lyrics matching those parameters:
   - Keep a consistent rhyme scheme and syllable/meter rhythm appropriate to the genre.
   - Label each section clearly (e.g. `[Verse 1]`, `[Chorus]`, `[Bridge]`).
   - Make the chorus the most memorable/repeatable part — reuse it verbatim where the structure calls for it.
3. Keep content original — do not copy or closely paraphrase existing copyrighted song lyrics. If the user asks for lyrics "in the style of" a specific artist, mimic general stylistic tendencies (tempo, themes, vocabulary) without copying actual lines from their real songs.
4. After presenting the lyrics, briefly offer to adjust genre, mood, length, or rhyme scheme if the user wants a revision.

## Example
Input: "Write me a short upbeat pop song about starting a new adventure."
Output:
```
[Verse 1]
Packed my bags before the sun came up,
Left the doubt behind, filled up my cup,
...

[Chorus]
We're running toward the great unknown,
Planting flags in fields we've never known,
...
```
