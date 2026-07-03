from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.platypus import ListFlowable, ListItem, Paragraph, SimpleDocTemplate, Spacer


PAGE_WIDTH, PAGE_HEIGHT = A4


def build_story(data, chinese=False):
    styles = getSampleStyleSheet()
    base_font = "STSong-Light" if chinese else "Helvetica"
    bold_font = "STSong-Light" if chinese else "Helvetica-Bold"

    title = ParagraphStyle(
        "ResumeTitle",
        parent=styles["Title"],
        fontName=bold_font,
        fontSize=18,
        leading=22,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#1f2937"),
        spaceAfter=6,
    )
    contact = ParagraphStyle(
        "Contact",
        parent=styles["Normal"],
        fontName=base_font,
        fontSize=9.5,
        leading=12,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#4b5563"),
        spaceAfter=8,
    )
    section = ParagraphStyle(
        "Section",
        parent=styles["Heading2"],
        fontName=bold_font,
        fontSize=11.5,
        leading=14,
        textColor=colors.HexColor("#0f766e"),
        spaceBefore=7,
        spaceAfter=5,
        borderWidth=0,
    )
    body = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontName=base_font,
        fontSize=9.5,
        leading=12.5,
        textColor=colors.HexColor("#111827"),
        spaceAfter=3,
        alignment=TA_LEFT,
    )
    item_title = ParagraphStyle(
        "ItemTitle",
        parent=body,
        fontName=bold_font,
        fontSize=9.8,
        leading=12.5,
        spaceAfter=1,
    )
    bullet = ParagraphStyle(
        "Bullet",
        parent=body,
        leftIndent=10,
        firstLineIndent=0,
        bulletIndent=0,
        spaceAfter=2,
    )

    story = [
        Paragraph(data["name"], title),
        Paragraph(data["contact"], contact),
        Spacer(1, 2),
    ]

    for sec in data["sections"]:
        story.append(Paragraph(sec["title"], section))

        if sec["type"] == "paragraph":
            story.append(Paragraph(sec["content"], body))
        elif sec["type"] == "bullets":
            bullets = [
                ListItem(Paragraph(item, bullet), leftIndent=0) for item in sec["items"]
            ]
            story.append(
                ListFlowable(
                    bullets,
                    bulletType="bullet",
                    bulletFontName=base_font,
                    bulletFontSize=8,
                    bulletOffsetY=2,
                    leftIndent=8,
                )
            )
        elif sec["type"] == "entries":
            for entry in sec["items"]:
                story.append(Paragraph(entry["title"], item_title))
                if entry.get("subtitle"):
                    story.append(Paragraph(entry["subtitle"], body))
                if entry.get("bullets"):
                    bullets = [
                        ListItem(Paragraph(item, bullet), leftIndent=0)
                        for item in entry["bullets"]
                    ]
                    story.append(
                        ListFlowable(
                            bullets,
                            bulletType="bullet",
                            bulletFontName=base_font,
                            bulletFontSize=8,
                            bulletOffsetY=2,
                            leftIndent=8,
                        )
                    )
        story.append(Spacer(1, 3))

    return story


def build_pdf(path, data, chinese=False):
    doc = SimpleDocTemplate(
        path,
        pagesize=A4,
        rightMargin=16 * mm,
        leftMargin=16 * mm,
        topMargin=14 * mm,
        bottomMargin=14 * mm,
        title=data["name"],
        author="Yichen Shi",
    )
    doc.build(build_story(data, chinese=chinese))


def main():
    registerFont(UnicodeCIDFont("STSong-Light"))

    en = {
        "name": "Yichen Shi",
        "contact": "Shanghai, China | shiyichen@sjtu.edu.cn | https://elevenmorning.github.io/ | Google Scholar",
        "sections": [
            {
                "title": "SUMMARY",
                "type": "paragraph",
                "content": (
                    "PhD student in Electronic Information and Electrical Engineering at Shanghai Jiao Tong University, "
                    "specializing in AI (LLM) for EDA, multimodal reasoning, and biometric security. Experienced in "
                    "building datasets, benchmarks, and applied machine learning systems through research and industry internships. "
                    "Seeking research or engineering roles in AI, multimodal systems, EDA intelligence, or applied machine learning."
                ),
            },
            {
                "title": "EDUCATION",
                "type": "bullets",
                "items": [
                    "<b>Shanghai Jiao Tong University</b> — Ph.D. in Electronic Information and Electrical Engineering, expected 2027",
                    "<b>Shijiazhuang Tiedao University</b> — M.S. in Computer Science, 2023",
                    "<b>Shijiazhuang Tiedao University</b> — B.S. in Computer Science, 2020",
                ],
            },
            {
                "title": "EXPERIENCE",
                "type": "entries",
                "items": [
                    {
                        "title": "Algorithm Intern — Shukun Technology | Sep 2023 – Jun 2024",
                        "bullets": [
                            "Worked on Segment Anything Model (SAM) and multimodal large language models for applied vision tasks.",
                            "Explored multimodal perception pipelines for practical AI applications.",
                        ],
                    },
                    {
                        "title": "Algorithm Intern — Ping An Technology | Jun 2023 – Sep 2023",
                        "bullets": [
                            "Conducted research on multimodal learning and model development.",
                            "Supported experimentation and evaluation for applied AI workflows.",
                        ],
                    },
                    {
                        "title": "Algorithm Intern — Hikvision | Feb 2022 – Jun 2023",
                        "bullets": [
                            "Worked on face anti-spoofing and face detection algorithms for biometric security scenarios.",
                            "Contributed to practical computer vision modeling and evaluation tasks.",
                        ],
                    },
                ],
            },
            {
                "title": "SELECTED PUBLICATIONS",
                "type": "bullets",
                "items": [
                    "<b>FaceShield</b>. AAAI 2026.",
                    "<b>SHIELD</b>. Visual Intelligence, 2025.",
                    "<b>AMSnet-KG</b>. ACM TODAES, 2025.",
                    "<b>AMSbench</b>. arXiv, 2025.",
                    "<b>AMSnet 2.0</b>. arXiv, 2025.",
                    "<b>AMSNet</b>. LAD 2024 Best Paper Award.",
                    "<b>Symbol and Footprint Database for Electronic Components by Agentic Recognition and Generation</b>. PRCV 2025.",
                ],
            },
            {
                "title": "PROJECT HIGHLIGHTS",
                "type": "bullets",
                "items": [
                    "Built <b>AMSNet</b>, <b>AMSnet 2.0</b>, and <b>AMSnet-KG</b>, a line of datasets and infrastructure for AMS circuit understanding, netlist generation, and LLM-based auto-design.",
                    "Developed <b>AMSbench</b>, a benchmark for evaluating multimodal large language models on AMS circuit perception, analysis, and design tasks.",
                    "Contributed to <b>FaceShield</b> and <b>SHIELD</b>, covering explainable face anti-spoofing, face forgery detection, multimodal evaluation, and model reasoning.",
                    "Co-founded <b>FEATs</b> (Future EDA and AI Techniques Seminar) to support academic exchange among early-career researchers in AI and EDA.",
                ],
            },
            {
                "title": "TECHNICAL SKILLS",
                "type": "bullets",
                "items": [
                    "<b>Programming:</b> Python, C++",
                    "<b>Domains:</b> machine learning, multimodal learning, large language models, computer vision, EDA, AMS circuits",
                    "<b>Research Workflow:</b> dataset construction, benchmarking, model evaluation, experiment design, academic writing",
                ],
            },
            {
                "title": "AWARDS",
                "type": "bullets",
                "items": [
                    "<b>LAD 2024 Best Paper Award</b> — for AMSNet: Netlist Dataset for AMS Circuits",
                    "Lanqiao Cup, Hebei Province — First Prize (Ranked 1st), 2020",
                    "HBCPC — Gold Medal (Top 10), 2020 and 2019",
                    "ACM-ICPC Xi'an Regional — Bronze Medal, 2019",
                    "CCF-CCSP North China Regional — Bronze Medal, 2019",
                    "ACM-ICPC Ningxia Regional — Bronze Medal, 2018",
                ],
            },
        ],
    }

    cn = {
        "name": "史屹琛",
        "contact": "上海 | shiyichen@sjtu.edu.cn | https://elevenmorning.github.io/ | Google Scholar",
        "sections": [
            {
                "title": "个人简介",
                "type": "paragraph",
                "content": (
                    "上海交通大学电子信息与电气工程学院博士生，研究方向聚焦于 AI（LLM）for EDA、多模态推理与生物特征安全。"
                    "具备数据集与 benchmark 构建、模型研发、多模态系统设计以及产业实习经验，正在寻找人工智能、多模态系统、EDA 智能化、"
                    "应用机器学习等方向的研究或算法岗位。"
                ),
            },
            {
                "title": "教育背景",
                "type": "bullets",
                "items": [
                    "<b>上海交通大学</b> — 电子信息与电气工程 博士，预计 2027 毕业",
                    "<b>石家庄铁道大学</b> — 计算机科学与技术 硕士，2023",
                    "<b>石家庄铁道大学</b> — 计算机科学与技术 学士，2020",
                ],
            },
            {
                "title": "实习经历",
                "type": "entries",
                "items": [
                    {
                        "title": "算法实习生 — 数坤科技 | 2023.09 – 2024.06",
                        "bullets": [
                            "参与 Segment Anything Model（SAM）与多模态大语言模型相关研究与应用探索。",
                            "面向实际视觉场景进行多模态感知流程研发。",
                        ],
                    },
                    {
                        "title": "算法实习生 — 平安科技 | 2023.06 – 2023.09",
                        "bullets": [
                            "参与多模态学习相关研究与模型开发工作。",
                            "支持应用型 AI 任务的实验与评估流程。",
                        ],
                    },
                    {
                        "title": "算法实习生 — 海康威视 | 2022.02 – 2023.06",
                        "bullets": [
                            "参与人脸反欺诈与人脸检测算法研发。",
                            "面向生物特征安全场景开展计算机视觉建模与评测工作。",
                        ],
                    },
                ],
            },
            {
                "title": "研究方向",
                "type": "bullets",
                "items": [
                    "<b>AI（LLM）for EDA：</b>模拟与混合信号电路理解、网表生成、多模态推理、知识增强自动设计",
                    "<b>计算机视觉与安全：</b>人脸反欺诈、人脸伪造检测、可解释多模态模型",
                ],
            },
            {
                "title": "代表论文",
                "type": "bullets",
                "items": [
                    "<b>FaceShield</b>，AAAI 2026",
                    "<b>SHIELD</b>，Visual Intelligence，2025",
                    "<b>AMSnet-KG</b>，ACM TODAES，2025",
                    "<b>AMSbench</b>，arXiv，2025",
                    "<b>AMSnet 2.0</b>，arXiv，2025",
                    "<b>AMSNet</b>，LAD 2024 Best Paper Award",
                    "<b>Symbol and Footprint Database for Electronic Components by Agentic Recognition and Generation</b>，PRCV 2025",
                ],
            },
            {
                "title": "项目与研究亮点",
                "type": "bullets",
                "items": [
                    "构建 <b>AMSNet</b>、<b>AMSnet 2.0</b> 与 <b>AMSnet-KG</b> 系列数据集与基础设施，支持 AMS 电路理解、网表生成与基于 LLM 的自动设计。",
                    "设计并开发 <b>AMSbench</b>，用于评测多模态大语言模型在 AMS 电路感知、分析与设计任务上的能力。",
                    "参与 <b>FaceShield</b> 与 <b>SHIELD</b> 研究，覆盖可解释人脸反欺诈、人脸伪造检测、多模态评测与模型推理。",
                    "联合发起 <b>FEATs</b>（Future EDA and AI Techniques Seminar），推动 AI 与 EDA 交叉方向青年研究者学术交流。",
                ],
            },
            {
                "title": "技术能力",
                "type": "bullets",
                "items": [
                    "<b>编程语言：</b>Python，C++",
                    "<b>技术领域：</b>机器学习，多模态学习，大语言模型，计算机视觉，EDA，AMS 电路",
                    "<b>研究能力：</b>数据集构建，benchmark 设计，模型评估，实验设计，学术写作",
                ],
            },
            {
                "title": "获奖情况",
                "type": "bullets",
                "items": [
                    "<b>LAD 2024 Best Paper Award</b> — AMSNet: Netlist Dataset for AMS Circuits",
                    "蓝桥杯河北省一等奖（第 1 名），2020",
                    "河北省大学生程序设计竞赛金奖（前 10 名），2020、2019",
                    "ACM-ICPC 西安区域赛铜奖，2019",
                    "CCF-CCSP 华北区域赛铜奖，2019",
                    "ACM-ICPC 宁夏区域赛铜奖，2018",
                ],
            },
        ],
    }

    build_pdf("files/Yichen_Shi_Resume_EN.pdf", en, chinese=False)
    build_pdf("files/史屹琛_简历_CN.pdf", cn, chinese=True)


if __name__ == "__main__":
    main()
