---
title: "FMA-Net: Flexible Modality Adaptation for Robust Multimodal Face Presentation Attack Detection"
collection: publications
permalink: /publication/2026-11-10-fma-net-flexible-modality-adaptation
excerpt: "FMA-Net uses instruction-guided latent-space translation, modality-invariant semantic anchors, and facial feature adaptation for robust multimodal face presentation attack detection under missing-modality conditions."
date: 2026-11-10
venue: "IEEE Transactions on Biometrics, Behavior, and Identity Science (TBIOM)"
shortvenue: "IEEE TBIOM (Accepted)"
status: accepted
category: FAS
label: "Co-first author"
citation: "Gao, Y., Shi, Y., Yu, Z., Wang, H., Li, H., Zhang, R., Ding, S., &amp; Feng, J. (2026). FMA-Net: Flexible Modality Adaptation for Robust Multimodal Face Presentation Attack Detection. <i>IEEE Transactions on Biometrics, Behavior, and Identity Science</i>, accepted."
---

**Authors:** Yuhao Gao<sup>*</sup>, **Yichen Shi<sup>*</sup>**, Zitong Yu, Hongyang Wang, Hongrui Li, Ruixin Zhang, Shouhong Ding, Jun Feng.

<sup>*</sup> Equal contribution (co-first authors).

The preprint is also available on **arXiv**.

## Abstract

Multimodal face presentation attack detection (fPAD) improves robustness using complementary RGB, depth, and infrared (IR) cues, but deployment remains challenging when modalities are unavailable or incomplete. Existing flexible-modality methods mainly use zero-filling or modality omission, potentially discarding cross-modal information and introducing modality-dependent bias. We propose the Flexible Modality Adaptation Network (FMA-Net), a unified framework that compensates for missing modalities through instruction-guided latent-space translation. The Face Modality Instruct Translator (FMIT) estimates target modality observations from RGB inputs, while context-aware category enhancement uses learnable text prompts as modality-invariant semantic anchors. A Facial Feature Adapter (F2A) integrates global facial structure and local spoof-relevant cues to enhance discriminative representations. Synthetic-to-Real Face Domain Alignment (SR-FDA) reduces feature discrepancies between translated and real modalities, with benefits depending on the missing-modality pattern and data domain. Experiments on WMCA and PADISI-Face validate the framework. On WMCA with a 70% modality missing ratio, FMA-Net achieves a mean ACER of 3.22% across four intra-domain missing-modality protocols, compared with 4.24% for the strongest baseline by the same criterion. When both depth and IR are entirely unavailable, it achieves 5.23% ACER, compared with 5.99% for the best competing result. Cross-domain experiments also reveal limitations of synthetic-to-real alignment under dataset shifts. These results support FMA-Net as a practical approach to fPAD with flexible and incomplete modalities.
