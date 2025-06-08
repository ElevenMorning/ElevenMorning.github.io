---
permalink: /
title: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I'm a second year Phd student from [School of SEIEE](https://www.seiee.sjtu.edu.cn/), [shanghai jiao tong University](https://www.sjtu.edu.cn/). My research interest includes computer vision, EDA, face anti-spoofing, and MLLM. I'm extremely fortunate to be supervised by Professor [Lei He](https://scholar.google.com/citations?hl=zh-CN&user=n_N-PJkAAAAJ&view_op=list_works&sortby=pubdate) from UCLA, and Associate Professor [Ting-Jung Lin](https://ieeexplore.ieee.org/author/37090062293) from EIT.


My research topics include applying AI methods to accelerate analog and mixed-signal (AMS) circuit design. Recently, I have developed a strong interest in the use of **multimodal large language models (MLLMs)** and **optimization techniques** in electronic design automation (EDA). I am also interested in **computer vision** and **biometric security**.


If you are interested in discussing related topics or potential collaborations, feel free to contact me via email at [shiyichen@sjtu.edu.cn](mailto:shiyichen@sjtu.edu.cn).

FEATS
=====
To foster academic exchange among young researchers in the intersection of AI and EDA, I co-founded the **Future EDA and AI Techniques Seminar (FEATs)** — an online seminar jointly initiated by Ph.D. students from East Institute of Technology, Shanghai Jiao Tong University, and UCLA. FEATs aims to provide a collaborative platform for early-career researchers to engage in in-depth discussions, share insights, and explore interdisciplinary collaboration opportunities. It also serves as a valuable entry point for newcomers to keep up with cutting-edge developments in EDA, machine learning, and AI. You can find at [here](https://space.bilibili.com/3546780138474143).
![DDCL 方法示意图](/images/2.3.png)

News
======

- 📄 [AMSbench: A Comprehensive Benchmark for Evaluating MLLM Capabilities in AMS Circuits](https://arxiv.org/abs/2505.24138) is now **available on arXiv**. (2025)
- 📄 [FaceShield: Explainable Face Anti-Spoofing with Multimodal Large Language Models](https://arxiv.org/abs/2505.09415) is now **available on arXiv**. (2025)
- 🎉 [Automated SAR ADC Sizing Using Analytical Equations](https://arxiv.org/abs/2505.09172) has been **accepted to ISEDA 2025**! (2025)
- 🎉 [AMSnet 2.0: A Large AMS Database with AI Segmentation for Net Detection](https://arxiv.org/abs/2505.09155) has been **accepted to LAD 2025**! (2025)
- 🎉 [AMSNet-KG: A Netlist Dataset for LLM-based AMS Circuit Auto-Design Using Knowledge Graph RAG](https://arxiv.org/abs/2411.13560) has been **accepted to ACM TODAES**！ (2024)
- 🎉 [SHIELD: An Evaluation Benchmark for Face Spoofing and Forgery Detection with Multimodal Large Language Models](https://arxiv.org/abs/2402.04178) has been **accepted to Visual Intelligence**！ (2024)
- 🎉 [AMSNet: Netlist Dataset for AMS Circuits](https://arxiv.org/abs/2405.09045) has been **accepted to LAD 2024** and received the **Best Paper Award**! (2024)

<!-- Getting started
======
1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
1. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section

Site-wide configuration
------
The main configuration file for the site is in the base directory in [_config.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_config.yml), which defines the content in the sidebars and other site-wide features. You will need to replace the default variables with ones about yourself and your site's github repository. The configuration file for the top menu is in [_data/navigation.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_data/navigation.yml). For example, if you don't have a portfolio or blog posts, you can remove those items from that navigation.yml file to remove them from the header. 

Create content & metadata
------
For site content, there is one markdown file for each type of content, which are stored in directories like _publications, _talks, _posts, _teaching, or _pages. For example, each talk is a markdown file in the [_talks directory](https://github.com/academicpages/academicpages.github.io/tree/master/_talks). At the top of each markdown file is structured data in YAML about the talk, which the theme will parse to do lots of cool stuff. The same structured data about a talk is used to generate the list of talks on the [Talks page](https://academicpages.github.io/talks), each [individual page](https://academicpages.github.io/talks/2012-03-01-talk-1) for specific talks, the talks section for the [CV page](https://academicpages.github.io/cv), and the [map of places you've given a talk](https://academicpages.github.io/talkmap.html) (if you run this [python file](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.py) or [Jupyter notebook](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb), which creates the HTML for the map based on the contents of the _talks directory).

**Markdown generator**

I have also created [a set of Jupyter notebooks](https://github.com/academicpages/academicpages.github.io/tree/master/markdown_generator
) that converts a CSV containing structured data about talks or presentations into individual markdown files that will be properly formatted for the Academic Pages template. The sample CSVs in that directory are the ones I used to create my own personal website at stuartgeiger.com. My usual workflow is that I keep a spreadsheet of my publications and talks, then run the code in these notebooks to generate the markdown files, then commit and push them to the GitHub repository.

How to edit your site's GitHub repository
------
Many people use a git client to create files on their local computer and then push them to GitHub's servers. If you are not familiar with git, you can directly edit these configuration and markdown files directly in the github.com interface. Navigate to a file (like [this one](https://github.com/academicpages/academicpages.github.io/blob/master/_talks/2012-03-01-talk-1.md) and click the pencil icon in the top right of the content preview (to the right of the "Raw | Blame | History" buttons). You can delete a file by clicking the trashcan icon to the right of the pencil icon. You can also create new files or upload files by navigating to a directory and clicking the "Create new file" or "Upload files" buttons. 

Example: editing a markdown file for a talk
![Editing a markdown file for a talk](/images/editing-talk.png)

For more info
------
More info about configuring Academic Pages can be found in [the guide](https://academicpages.github.io/markdown/). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful. -->
