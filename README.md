\# Mantra Smriti



Mantra Smriti is a lightweight browser-based app for memorising Sanskrit texts through recall, sequence practice, cues, meanings, and selected sandhi notes.



The current collection includes:



\- \*\*Ram Raksha Stotra\*\*

\- \*\*Nirvana Shatakam\*\*



\## Features



\- Verse-by-verse memory map

\- Recall and sequence practice

\- First-word cues

\- Progressive sequence hints

\- Pāda-by-pāda build mode

\- Meanings and word notes

\- Selective sandhi explanations for difficult forms

\- Full-text recitation view

\- Per-browser progress tracking using `localStorage`



\## Access



The published app is encrypted.



The repository contains:



\- `index.html` — the unlock page

\- `app.enc` — the encrypted application payload



The access code is \*\*not stored in this repository\*\*.



When a valid access code is entered, the browser derives a key using PBKDF2 and decrypts the application locally using AES-256-GCM.



The unencrypted application source is intentionally not included in the public repository.



\## Privacy and progress



No account is required.



Learning progress is stored locally in the browser using `localStorage`. It is not uploaded to a server.



As a result:



\- progress remains available on the same browser/device

\- different browsers or devices maintain separate progress

\- clearing browser/site data removes saved progress



\## Repository structure



```text

mantra-smrit/

├── index.html

├── app.enc

├── encrypt\_app.py

├── README.md

└── .gitignore

```



`source-app.html` is intentionally excluded via `.gitignore`.



\## Updating the application



The application source is maintained separately from the public encrypted build.



After updating the source, `encrypt\_app.py` is used to generate a new `app.enc`. The same access code may be reused across updates.



Only the encrypted payload is committed to the public repository.



\## Security model



This project uses client-side encryption rather than server-side authentication.



The application contents are not available in plaintext from the public repository, but anyone who knows the shared access code can decrypt and redistribute them.



This access mechanism is intended for lightweight controlled sharing, not high-security authentication.



\## Hosting



The site is designed to be hosted as a static site using GitHub Pages.

