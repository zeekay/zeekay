<h1 align="center">Z</h1>

<p align="center">
  <em>Open Sourceror. Building decentralized intelligence across AI, blockchain, and quantum.</em>
</p>

<p align="center">
  <a href="https://zeekay.io">zeekay.io</a> &middot;
  <a href="https://hanzo.ai">hanzo.ai</a> &middot;
  <a href="https://lux.network">lux.network</a> &middot;
  <a href="https://zoo.ngo">zoo.ngo</a> &middot;
  <a href="https://zenlm.org">zenlm.org</a>
</p>

<p align="center">
  <code>curl -sL zeekay.chat | sh</code>
</p>

---

### Models

Zen generates. Enso routes. Kai decides. Nio enforces.

| Model | Focus & Architecture |
|---|---|
| [Zen](https://hanzo.ai/zen) | Open-weight foundation model family &mdash; language, code, vision, audio, embeddings ([weights](https://huggingface.co/zenlm)) |
| [Enso](https://hanzo.ai/enso) | Adaptive model family & router &mdash; routes every call, in every modality, to the optimal model |
| [Kai](https://hanzo.ai/kai) | Decision model &mdash; block speculative diffusion turning heterogeneous evidence into calibrated, typed decisions |
| [Nio](https://hanzo.ai/trust) | Deterministic policy authority &mdash; joins on `allow < ask < deny`, governs action execution under invariant policy |
| [Lifeguard](https://github.com/zooai/lifeguard) | Autonomous life preservation framework &mdash; couples Kai perception with Nio policy to eliminate hardware self-preservation |

#### Creative AI

Video, image, 3D, Foley, voice and music &mdash; from open Zen foundations to studio generation.

| Model | Modality & Capabilities |
|---|---|
| [Koma](https://hanzo.ai/koma) | Cinematic video generation, character continuity, and director camera control (`/v1/video`) &middot; [Zen Director](https://huggingface.co/zenlm/zen-director) |
| [Iro](https://hanzo.ai/iro) | High-fidelity image synthesis, character sheets, inpainting and wide-gamut color (`/v1/images`) &middot; [Zen Artist](https://github.com/zenlm/zen-artist) |
| [Mori](https://hanzo.ai/mori) | Production 3D asset generation, watertight quad/tri meshes, and PBR materials (`/v1/3d`) &middot; [Zen 3D](https://huggingface.co/zenlm/zen-3d) |
| [Oto](https://hanzo.ai/oto) | Frame-synchronized Foley, acoustic room impulse modeling, and environmental audio (`/v1/foley`) &middot; [Zen Foley](https://huggingface.co/zenlm/zen-foley) |
| [Koe](https://hanzo.ai/koe) | Directable speech synthesis, emotional modulation, voice cloning, and dubbing (`/v1/audio/speech`) &middot; [Zen Dub](https://github.com/zenlm/zen-dub) |
| [Uta](https://hanzo.ai/uta) | Original song composition, cue-driven scoring, and multi-track music production (`/v1/music`) &middot; [Zen Musician](https://github.com/zenlm/zen-musician) |
| [Jin](https://hanzo.ai/realtime) | Real-time bidirectional streaming, voice activity detection (VAD), and conversational agent interaction |

Hanzo builds and runs these for companies: [hanzo.ai/enterprise](https://hanzo.ai/enterprise) &middot; [hanzo.ai/contact](https://hanzo.ai/contact)

---

### Research

#### AI & Foundation Models

Frontier AI, from the model weights to the cloud that serves them.

**[Hanzo AI](https://github.com/hanzoai)** `CEO` &mdash; Techstars '17. The Open AI Cloud.

| Component | Function |
|---|---|
| [Cloud](https://github.com/hanzoai/cloud) | The open core of Hanzo Cloud &mdash; one Go binary |
| [Engine](https://github.com/hanzoai/engine) | Native multimodal inference in one Rust binary &mdash; text, vision, audio, speech, image, embeddings |
| [Decision](https://github.com/hanzoai/decision) | Typed decision runtime and Kai inference engine &mdash; CPU, CUDA, Vulkan, Metal |
| [Trust](https://github.com/hanzoai/trust) | Deterministic policy authority (Nio) and runtime trust boundary |
| [MCP](https://github.com/hanzoai/mcp) | Model Context Protocol server with 260+ tools for AI agents |
| [Agents](https://github.com/hanzoai/agents) | Multi-agent orchestration over the MCP tool surface |
| [Crawl](https://github.com/hanzoai/crawl) | Read any web page as clean markdown &mdash; Go library, CLI and API |
| [Code](https://github.com/hanzoai/code) | Open source AI code editor &mdash; any model, full data control |
| [Guard](https://github.com/hanzoai/guard) | The safety layer for LLM applications |
| [Gateway](https://github.com/hanzoai/gateway) | The trust boundary at `api.hanzo.ai` &mdash; identity, rate limits, metering |

**[Zen LM](https://github.com/zenlm)** `Architect` &mdash; Open foundation models, from the edge to frontier scale.

| Foundation | Architecture & Role |
|---|---|
| [Zen6](https://huggingface.co/zenlm/zen6) | 27B dense model, NVFP4 |
| [Zen6 Flash](https://huggingface.co/zenlm/zen6-flash) | 27B ternary vision-language model |
| [Zen6 Coder](https://huggingface.co/zenlm/zen6-coder) | Agentic mixture-of-experts for code |
| [Zen5](https://github.com/zenlm/zen5) | Mixture of Diverse Experts &mdash; compute scales with task difficulty |
| [Zen](https://github.com/zenlm/zen) | The open model family &mdash; language, code, vision, audio, 3D and world models |
| [Zen VL](https://huggingface.co/zenlm/zen-vl-30b-instruct) | Vision-language models with function calling |
| [Zen Omni](https://github.com/zenlm/zen-omni) | 30B hypermodal AI &mdash; text, vision, audio, video |
| [Zen Director](https://huggingface.co/zenlm/zen-director) | Open diffusion transformer foundation for video research (Wan2.2 base) |
| [Zen Artist](https://github.com/zenlm/zen-artist) | Open foundation for text-to-image synthesis, styling and inpainting |
| [Zen 3D](https://github.com/zenlm/zen-3d) | Controllable image-to-3D asset generation based on TRELLIS |
| [Zen World](https://github.com/zenlm/zen-world) | 3D world and scene generation |
| [Zen Foley](https://huggingface.co/zenlm/zen-foley) | Open foundation for frame-synchronized audio and Foley synthesis |
| [Zen Dub](https://github.com/zenlm/zen-dub) | Multilingual directable speech synthesis foundation (Qwen3-TTS base) |
| [Zen Musician](https://github.com/zenlm/zen-musician) | Full-length song generation and latent diffusion music foundation |
| [Satori](https://github.com/zenlm/satori) | Video generation in latent space with explicit temporal dynamics |
| [Mu](https://github.com/zenlm/mu) | Full-length song generation with latent diffusion |
| [Engine](https://github.com/zenlm/engine) | High-performance inference &mdash; Rust, MLX, GGUF |
| [Gym](https://github.com/zenlm/gym) | Unified fine-tuning for 100+ LLMs and VLMs |

---

#### Post-Quantum Cryptography & Blockchain

Hardening decentralized systems against quantum computers with lattice-based cryptography, threshold signatures, and a consensus engine of our own.

**[Lux](https://github.com/luxfi)** `Chairman` &mdash; Post-quantum blockchain accelerating economic freedom.

| Component | Description |
|---|---|
| [Node](https://github.com/luxfi/node) | The Lux node &mdash; Go, Rust and C++ runtimes at parity, ZAP-native |
| [Consensus](https://github.com/luxfi/consensus) | Quasar consensus engine |
| [Precompiles](https://github.com/luxfi/precompile) | EVM precompiles for ML-DSA, ML-KEM, SLH-DSA, AI mining, and Teleport |
| [ML-DSA](https://github.com/luxfi/precompile/tree/main/mldsa) | On-chain Dilithium (FIPS 204) signature verification |
| [Crypto](https://github.com/luxfi/crypto) | Core primitives: SHA-2/3, ECDSA, BLS, HKDF, and lattice-based post-quantum schemes |
| [Threshold](https://github.com/luxfi/threshold) | Multiparty CGGMP21, FROST, and LSS threshold signatures |
| [MPC](https://github.com/luxfi/mpc) | Multi-party compute nodes and wallet service &mdash; CGGMP21, FROST |
| [FROST](https://github.com/luxfi/safe-frost) | FROST threshold signatures for Safe smart accounts |
| [KMS](https://github.com/luxfi/kms) | Open source secrets and key management |
| [EVM](https://github.com/luxfi/evm) | Launch your own EVM chain on Lux |

---

#### Encrypted Computation & Privacy

Computing on data that stays encrypted, and moving value between chains without a trusted party.

| Protocol | Focus |
|---|---|
| [FHE](https://github.com/luxfi/fhe) | Fully homomorphic encryption with GPU acceleration |
| [Lattice](https://github.com/luxfi/lattice) | Multiparty homomorphic encryption for post-quantum safety |
| [Bridge](https://github.com/luxfi/bridge) | Trustless MPC bridge with the Teleport protocol |
| [Multi-Party ECDSA](https://github.com/luxfi/multi-party-ecdsa) | {t,n}-threshold ECDSA for Teleport |

---

#### Decentralized AI & Science

Open research networks and community governance for AI.

**[Zoo](https://github.com/zoo-labs)** `Founder` &mdash; Decentralized AI research network and regenerative finance for endangered life.

| Project | Focus |
|---|---|
| [Lifeguard](https://github.com/zooai/lifeguard) | Autonomous life preservation framework &mdash; dataset, benchmarks, and structural complement head |
| [Papers](https://papers.zoo.ngo) | Open peer-style papers on species monitoring, bioacoustics, and habitat modeling |
| [ZIPs](https://zips.zoo.ngo) | Zoo Improvement Proposals &mdash; open governance for AI research |
| [Zoo](https://github.com/zoo-labs/zoo) | The Zoo ecosystem &mdash; decentralized AI research network and interactive menagerie |

---

#### ZAP

Zero-copy app protocol: one wire format for AI agents and the services they call, with a written spec, formal proofs, and native bindings across languages.

| Layer | Specification & Bindings |
|---|---|
| [Spec](https://github.com/zap-proto/spec) | The wire format, byte for byte |
| [Proofs](https://github.com/zap-proto/proofs) | Formal proofs for the protocol family |
| [zip](https://github.com/zap-proto/zip) | ZAP-native web framework for Go |
| [zapd](https://github.com/zap-proto/zapd) | The shared local broker every ZAP service connects to |
| [Go](https://github.com/zap-proto/go) &middot; [Rust](https://github.com/zap-proto/rust) &middot; [Python](https://github.com/zap-proto/py) &middot; [TypeScript](https://github.com/zap-proto/js) &middot; [C++](https://github.com/zap-proto/cpp) &middot; [C](https://github.com/zap-proto/c) &middot; [Java](https://github.com/zap-proto/java) &middot; [.NET](https://github.com/zap-proto/cs) | Core bindings |
| [Haskell](https://github.com/zap-proto/haskell) &middot; [OCaml](https://github.com/zap-proto/ocaml) &middot; [Scala](https://github.com/zap-proto/scala) &middot; [Erlang](https://github.com/zap-proto/erlang) &middot; [Nim](https://github.com/zap-proto/nim) &middot; [D](https://github.com/zap-proto/d) &middot; [Lua](https://github.com/zap-proto/lua) &middot; [Ruby](https://github.com/zap-proto/ruby) &middot; [WebAssembly](https://github.com/zap-proto/wasm) | More languages |
| [LSP](https://github.com/zap-proto/lsp) &middot; [VS Code](https://github.com/zap-proto/vscode) &middot; [Vim](https://github.com/zap-proto/vim) &middot; [Sublime](https://github.com/zap-proto/sublime) &middot; [IntelliJ](https://github.com/zap-proto/intellij) &middot; [Wireshark](https://github.com/zap-proto/wireshark) | Tooling |

---

#### Finance

| Application | Purpose |
|---|---|
| [Wallet](https://github.com/luxfi/wallet) | Open source Lux DeFi wallet |
| [Market](https://github.com/luxfi/market) | Marketplace for real-world assets |
| [Bank](https://github.com/luxfi/bank) | Open source banking-as-a-service |

---

### Organizations

| Organization | Public Repos | Focus |
|---|---|---|
| [hanzoai](https://github.com/hanzoai) | 552 | The Open AI Cloud: Enso, agents, MCP, inference |
| [luxfi](https://github.com/luxfi) | 345 | Post-quantum blockchain, consensus, DeFi |
| [zenlm](https://github.com/zenlm) | 91 | Open foundation models, training, inference |
| [zoo-labs](https://github.com/zoo-labs) | 4 | DeAI research, decentralized science |
| [zeekay](https://github.com/zeekay) | 453 | Open source tools, protocols, experiments |

---

<p align="center">
  <a href="https://zeekay.io">
    <img src="https://img.shields.io/badge/zeekay.io-000?style=flat-square&logo=safari&logoColor=white" alt="Website" />
  </a>
  <a href="https://github.com/zeekay">
    <img src="https://img.shields.io/badge/GitHub-000?style=flat-square&logo=github&logoColor=white" alt="GitHub" />
  </a>
  <a href="https://huggingface.co/zenlm">
    <img src="https://img.shields.io/badge/HuggingFace-000?style=flat-square&logo=huggingface&logoColor=white" alt="HuggingFace" />
  </a>
</p>
