# SmarTorium

![Status](https://img.shields.io/badge/status-beta-yellow)
![Python](https://img.shields.io/badge/python-3.x-blue)
![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)
![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)
[![GitHub stars](https://img.shields.io/github/stars/hidden2see/SmartTorium?style=social)](https://github.com/hidden2see/SmartTorium/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/hidden2see/SmartTorium)](https://github.com/hidden2see/SmartTorium/commits/master)

I got tired of hand-editing `torrc` every time I wanted to switch exit countries in Tor Browser, so I built SmarTorium — a small script that does it for you, with more coming.

> ⚠️ **Heads up: this is beta software.** The exit-country switch works well. Most of the rest is still being built (see the table below). Try it in a throwaway/test setup first, not your daily driver. Details in the [Disclaimer](#disclaimer--legal-notice).

---

## Why this exists

Tor Browser can already do most of this — but only if you're comfortable opening config files by hand, restarting the browser, and remembering the exact syntax each time. I wasn't, most of the time, so I wrapped the parts I use most into one command.

Right now that's:
- Switching exit country without touching `torrc`

And on the way:
- Saving and switching between browser profiles
- Making your preferred settings stick across sessions

To be clear — this doesn't touch or replace Tor Browser's actual security model. It just sits on top of it and saves you some typing. No telemetry, nothing phoned home.

## See it in action

![SmarTorium demo](https://i.ibb.co/twDBcD7Y/DEMO.png)

## Getting it running

```bash
git clone https://github.com/hidden2see/SmartTorium.git
cd SmartTorium
python main.py
```

You'll need Python 3.x and a Tor Browser install already on your machine.

## Using it

*(A couple of real examples belong here, e.g.)*

```bash
python main.py --exit-country de
```

## Where things stand

| Feature | Status |
|---|---|
| Modify exit country | ✅ works today |
| Profiles | 🚧 building it |
| Profile data persistence | 🚧 building it |
| Encrypted local profile data | 🚧 planned — see note below |
| Auto-run | 🚧 building it |

## On local data and encryption

**Right now, SmarTorium does not create or store any persistent local data.** The only working feature (exit-country switching) just writes a value Tor itself reads — there's nothing saved to disk that belongs to you as a user yet.

Once profiles are implemented, some of that will change — profile preferences and any cookies you opt to retain will need to live somewhere. When that happens:
- This section will be updated to describe exactly what's stored, where, and how it's protected.
- Sensitive data (like retained cookies) will be encrypted; non-sensitive preferences (like "reopen this profile on load") likely won't need to be, and I'll be explicit about which is which rather than blanket-labeling everything "encrypted."
- I'll document the specific method used (library, key derivation, and what happens if you lose your passphrase) before this feature ships — not after.

Until that's written and true, please don't rely on this tool for protecting sensitive local data.

## On trust

I know asking people to hand a tool access to their Tor config is a big ask, especially from a project this new. So, plainly:

- Nothing leaves your device — no analytics, no phone-home.
- The code's all here to read — `main.py` and `scripts/`, nothing hidden.
- I haven't had this independently reviewed yet. Treat it accordingly until it has been.

## What's next

- [ ] Ship basic profiles (exit-country + reopen-on-load, no sensitive data)
- [ ] Add per-site preference metadata (retain cookies, extension exceptions) as settings only
- [ ] Implement real encryption for the profile tier that actually needs it (cookies)
- [ ] Test across platforms properly
- [ ] Call it stable

## Questions people ask

**Got an idea for a feature?**
Open an issue and tell me about it — I do read them.

**Want to help build it?**
Fork it, follow [Conventional Commits](https://www.conventionalcommits.org/) for commit messages, and send a PR. Take a look at open issues and the roadmap above first so we're not duplicating work.

## A note on compatibility

I haven't been able to properly verify this across different setups yet — that'll come with the first stable release. Until then, please don't run this outside a test environment; the risk is local data loss or corruption, not a hypothetical one.

## Disclaimer & Legal Notice

- **Beta Software Notice:** This software is currently in beta. **Use at your own risk.**
- **Open-Source Terms:** This project is open source (AGPLv3) and open to public contribution.
- **Limitation of Liability & Warranty:** This software is provided "AS IS", without warranty of any kind, express or implied, including but not limited to warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the developers or contributors be liable for any claim, damages, privacy leaks, system anomalies, data loss, or other liability arising from, out of, or in connection with the use of this software or Tor Browser.
- **Data Encryption & Loss:** SmarTorium does not currently store persistent local data, so there is nothing to encrypt yet. Once local data storage (e.g. profiles) is implemented, this section will be updated with accurate details — including what happens if an encryption key or passphrase is lost. Until then, this clause is a placeholder for future functionality, not a description of anything currently shipped.

## License

AGPLv3 — see [LICENSE.md](./LICENSE.md) for the full text. In short: you're free to use, modify, and redistribute this, but if you distribute a modified version — including running it as a hosted/network service — you must release your source under the same license. This is meant to keep SmarTorium (and anything built from it) open, including if someone tries to offer it as a paid hosted service.