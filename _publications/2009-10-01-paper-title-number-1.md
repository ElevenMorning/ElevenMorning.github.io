---
title: "二次解耦与活体特征渐进式对齐的域自适应人脸反欺诈"
collection: publications
permalink: /publication/2009-10-01-paper-title-number-1
excerpt: '现有的人脸反欺诈（face anti-spoofing,FAS）方法虽然在域内测试表现良好，但在跨域场景下性能会大幅度下降.当前基于域对抗对齐的跨域人脸反欺诈方法，因其对齐网络和分类网络彼此独立，无法保证对齐任务直接服务于分类任务.提出了一种基于二次解耦与活体特征课程学习渐进式对抗对齐的域自适应人脸反欺诈（domain adaptation for face anti-spoofing based on dual disentanglement and liveness feature curriculum learning progressive adversarial alignment,DDCL）方法，首先将源域特征启发式解耦为域相关特征和域无关特征，之后使用分类器的梯度信息将域无关特征中的活体相关和无关特征进行第2次解耦.在训练过程中为减轻优化难度，通过课程学习的方式对目标域特征与活体相关、无关特征的组合进行渐进式对抗对齐，逐步提高活体相关特征的比重，增强目标域特征与活体检测任务的相关性，从因果角度给出活体对齐域自适应的解释.在CASIA-MFSD,Idiap Replay-Attack,MSU-MFSD与OULU-NPU公开数据集上的实验结果表明，与现有10种方法相比，所提出的方法获得了22.5%的最佳平均HTER值，并在4个测评协议上均达到了当前先进水平，尤其是I-M和O-M测评协议的HTER值分别达到了12.4%和12.8%，能显著降低模型在目标域上的错误率，具有更好的跨域泛化能力.'
date: 2023-06-16
venue: '计算机研究与发展'
paperurl: [PDF链接](https://github.com/ElevenMorning/ElevenMorning.github.io/tree/master/files/fas_da.pdf)
citation: '封筠,史屹琛,高宇豪,等.二次解耦与活体特征渐进式对齐的域自适应人脸反欺诈[J].计算机研究与发展,2023,60(08):1727-1739.'
---

The contents above will be part of a list of publications, if the user clicks the link for the publication than the contents of section will be rendered as a full page, allowing you to provide more information about the paper for the reader. When publications are displayed as a single page, the contents of the above "citation" field will automatically be included below this section in a smaller font.
