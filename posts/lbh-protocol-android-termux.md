# Building the LBH Protocol from Android/Termux: A Sovereign Edge Architecture

**By Cristhiam Leonardo Hernández Quiñonez (CLHQ)**  
*Founder – HormigasAIS | Sovereign edge computing ecosystem – San Miguel, El Salvador*  
*github.com/Thrumanshow/HormigasAIS*

![HormigasAIS LBH Protocol Cover](../assets/cover-lbh-termux.png)

---

## 1. The Problem: Depending on the Cloud to Validate What's Real

Most content-verification and edge-computing stacks today assume a baseline dependency: a cloud provider, a centralized API, or a third-party service sitting between your data and the claim that it's authentic. That dependency is convenient, but it's also a single point of failure and a single point of control.

The question I kept returning to while building HormigasAIS was simple: **can a verification system be sovereign?** Not "self-hosted on someone else's cloud," but genuinely independent — running on infrastructure you own, from a device as unconventional as a phone.

## 2. The Solution: A Node Architecture Built on Sealing, Not Trust

HormigasAIS approaches this with a node-based architecture rather than a service-based one. Three pieces anchor it:

- **LBH cryptographic sealing** — content is sealed using SHA-256 + HMAC-SHA256, with signed verification that doesn't require calling out to a third party to confirm integrity.
- **`barrera.js`** — an ethical/logical filter layer (informally, "decromatiza") that sits between raw input and the system's accepted state.
- **`humano.js`** — a small symbolic module declaring the human-language layer of the project: `HormigasAIS = {{lenguaje-humano}}`. It's less a functional API and more a positioning statement embedded directly in code — a reminder that the system is meant to stay legible to a human reader, not just to a machine.

None of this requires a data center. The full development loop — writing, testing, sealing, deploying — happens from an Android device running Termux.

## 3. The Implementation: From a 404 to a Working Node

The most concrete proof point is small on purpose. The repository [`Thrumanshow/HormigasAIS`](https://github.com/Thrumanshow/HormigasAIS) started as a set of governance and symbolic files with no public-facing page — visiting its GitHub Pages URL returned a plain 404.

Getting it live took: enabling GitHub Pages from the `main` branch root, writing a minimal `index.html` (styled, ~19 lines of real content), and documenting the repo properly — `README.md`, `LICENSE` (MIT), `GOVERNANCE.md`, `STATUS.md`, and `MANIFIESTO.md`. The structure deliberately mirrors an earlier, simpler project of mine, [`Chris-BarberShop`](https://github.com/Thrumanshow/Chris-BarberShop), which proved the same pattern — a single clean `index.html` as a public entry point — works for something as unrelated as a local barbershop's digital presence. If the pattern holds at that scale, it holds for infrastructure documentation too.

The entire sequence — clone, edit, verify with `curl`, commit, push, confirm `200` — ran from Termux on a Samsung A16, no laptop involved.

## 4. The Ecosystem: What's Actually Public

To be precise about what's verifiable versus conceptual:

**Live and checkable:**
- [hormigasais.com](https://hormigasais.com) — main site
- [lbh.hormigasais.com](https://lbh.hormigasais.com) — LBH protocol site
- [api.hormigasais.com](https://api.hormigasais.com) — Worker API
- [docs.hormigasais.com](https://docs.hormigasais.com) — documentation
- [blog.hormigasais.com](https://blog.hormigasais.com) — blog
- The formal LBH specification is deposited on Zenodo: **DOI [10.5281/zenodo.17767205](https://doi.org/10.5281/zenodo.17767205)**

**Governance:**
The project operates under an explicit [GOVERNANCE.md](https://github.com/Thrumanshow/HormigasAIS/blob/main/GOVERNANCE.md), which is worth flagging precisely because it's unusual for a solo project: it draws a hard line between forking/using the code (permitted under license) and any claim of official representation or node status (which requires explicit, written recognition from the maintainer of record). Forks are welcome. Authority isn't inherited by default.

**Still experimental:**
The broader multi-agent decision system and node-validation layer are active work — not yet at the same level of external verifiability as the sealing protocol or the published spec, and I want to be upfront about that distinction rather than blur it.

---

*If you're building anything edge-first, protocol-level, or just skeptical of cloud dependency by default — I'd welcome the conversation.*
