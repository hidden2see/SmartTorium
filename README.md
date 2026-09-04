# SmarTorium

![Status](https://img.shields.io/badge/status-beta-yellow)
![Python](https://img.shields.io/badge/python-3.x-blue)
![License](https://img.shields.io/badge/license-unlicensed-lightgrey)
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

*(This is where a short terminal recording or screenshot should go — genuinely the thing that will convince people fastest. A 10-second [asciinema](https://asciinema.org/) clip of setting an exit country would do more than any paragraph here.)*

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
| Encrypted local add-on data | 🚧 building it |
| Profiles | 🚧 building it |
| Profile data persistence | 🚧 building it |
| Auto-run | 🚧 building it |

## On trust

I know asking people to hand a tool access to their Tor config is a big ask, especially from a project this new. So, plainly:

- Nothing leaves your device — no analytics, no phone-home.
- The code's all here to read — `main.py` and `scripts/`, nothing hidden.
- *(Worth adding once true: whether anyone besides me has reviewed this, and exactly how local data gets stored/encrypted. Being upfront about what hasn't been checked yet matters more than pretending it has.)*

## What's next

- [ ] Get encrypted local storage actually working
- [ ] Ship profiles
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
- **Open-Source Terms:** This project is open source and open to public contribution.
- **Limitation of Liability & Warranty:** This software is provided "AS IS", without warranty of any kind, express or implied, including but not limited to warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the developers or contributors be liable for any claim, damages, privacy leaks, system anomalies, data loss, or other liability arising from, out of, or in connection with the use of this software or Tor Browser.
- **Data Encryption & Loss:** Local data is encrypted using cryptographic methods. If encryption keys or passwords are lost, deleted, or forgotten, that data **cannot be decrypted or recovered** by the developers or maintenance team.

## License

*(Still needs one — an unlicensed repo makes people hesitate to use or contribute to it, especially for anything touching Tor. MIT or Apache-2.0 are the usual picks for something this size.)*
