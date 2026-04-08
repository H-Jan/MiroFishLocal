"""
Generate MiroFish-Offline Technical Thesis PDF
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    ListFlowable, ListItem, KeepTogether
)


def build_pdf():
    output_path = "/Users/hanijandali/Desktop/MiroFish_Offline_Technical_Thesis.pdf"

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72,
    )

    styles = getSampleStyleSheet()

    # Custom styles
    styles.add(ParagraphStyle(
        name='ThesisTitle',
        parent=styles['Title'],
        fontSize=26,
        leading=32,
        spaceAfter=6,
        alignment=TA_CENTER,
        textColor=HexColor('#1a1a2e'),
    ))
    styles.add(ParagraphStyle(
        name='Subtitle',
        parent=styles['Normal'],
        fontSize=14,
        leading=18,
        alignment=TA_CENTER,
        textColor=HexColor('#444444'),
        spaceAfter=30,
    ))
    styles.add(ParagraphStyle(
        name='ChapterTitle',
        parent=styles['Heading1'],
        fontSize=20,
        leading=26,
        spaceBefore=30,
        spaceAfter=14,
        textColor=HexColor('#1a1a2e'),
        borderWidth=1,
        borderColor=HexColor('#1a1a2e'),
        borderPadding=(0, 0, 4, 0),
    ))
    styles.add(ParagraphStyle(
        name='SectionTitle',
        parent=styles['Heading2'],
        fontSize=15,
        leading=20,
        spaceBefore=18,
        spaceAfter=8,
        textColor=HexColor('#2d3436'),
    ))
    styles.add(ParagraphStyle(
        name='SubSection',
        parent=styles['Heading3'],
        fontSize=12,
        leading=16,
        spaceBefore=12,
        spaceAfter=6,
        textColor=HexColor('#2d3436'),
    ))
    styles.add(ParagraphStyle(
        name='Body',
        parent=styles['Normal'],
        fontSize=11,
        leading=16,
        alignment=TA_JUSTIFY,
        spaceAfter=8,
    ))
    styles.add(ParagraphStyle(
        name='CodeBlock',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=9,
        leading=12,
        leftIndent=20,
        spaceAfter=8,
        backColor=HexColor('#f5f5f5'),
    ))
    styles.add(ParagraphStyle(
        name='TableHeader',
        parent=styles['Normal'],
        fontSize=10,
        leading=13,
        textColor=white,
        alignment=TA_CENTER,
    ))
    styles.add(ParagraphStyle(
        name='TableCell',
        parent=styles['Normal'],
        fontSize=9,
        leading=12,
    ))
    styles.add(ParagraphStyle(
        name='Caption',
        parent=styles['Normal'],
        fontSize=9,
        leading=12,
        alignment=TA_CENTER,
        textColor=HexColor('#666666'),
        spaceAfter=12,
        spaceBefore=4,
    ))
    styles.add(ParagraphStyle(
        name='Warning',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        leftIndent=20,
        rightIndent=20,
        spaceBefore=8,
        spaceAfter=8,
        backColor=HexColor('#fff3cd'),
        borderWidth=1,
        borderColor=HexColor('#ffc107'),
        borderPadding=8,
    ))
    styles.add(ParagraphStyle(
        name='TOCEntry',
        parent=styles['Normal'],
        fontSize=12,
        leading=22,
        leftIndent=0,
    ))
    styles.add(ParagraphStyle(
        name='TOCSubEntry',
        parent=styles['Normal'],
        fontSize=11,
        leading=18,
        leftIndent=20,
    ))

    story = []
    S = Spacer

    def make_table(headers, rows, col_widths=None):
        hdr = [Paragraph(h, styles['TableHeader']) for h in headers]
        data = [hdr]
        for row in rows:
            data.append([Paragraph(str(c), styles['TableCell']) for c in row])
        t = Table(data, colWidths=col_widths, repeatRows=1)
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), HexColor('#1a1a2e')),
            ('TEXTCOLOR', (0, 0), (-1, 0), white),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('TOPPADDING', (0, 0), (-1, 0), 8),
            ('BACKGROUND', (0, 1), (-1, -1), HexColor('#fafafa')),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [HexColor('#ffffff'), HexColor('#f5f5f5')]),
            ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#cccccc')),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
            ('TOPPADDING', (0, 1), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 5),
        ]))
        return t

    # ==================== TITLE PAGE ====================
    story.append(S(1, 120))
    story.append(Paragraph("MiroFish-Offline", styles['ThesisTitle']))
    story.append(S(1, 8))
    story.append(Paragraph("A Fully Local Multi-Agent Swarm Intelligence Engine<br/>for Social Simulation and Public Opinion Analysis", styles['Subtitle']))
    story.append(S(1, 40))
    story.append(Paragraph("Comprehensive Technical Reference", styles['Subtitle']))
    story.append(S(1, 20))
    story.append(Paragraph("System Architecture, Deployment, Operations, and Troubleshooting", styles['Subtitle']))
    story.append(S(1, 80))
    story.append(Paragraph("Prepared: April 2026", styles['Subtitle']))
    story.append(Paragraph("Platform: Apple Silicon (128GB Unified Memory)<br/>Stack: Python 3.11 | Neo4j | Ollama | Vue 3 | Flask", styles['Subtitle']))
    story.append(PageBreak())

    # ==================== TABLE OF CONTENTS ====================
    story.append(Paragraph("Table of Contents", styles['ChapterTitle']))
    story.append(S(1, 12))
    toc_chapters = [
        ("Chapter 1", "What is MiroFish-Offline?"),
        ("Chapter 2", "System Architecture Overview"),
        ("Chapter 3", "The Technology Stack"),
        ("Chapter 4", "Installation and Environment Setup"),
        ("Chapter 5", "Configuration Deep Dive"),
        ("Chapter 6", "The Five-Step Workflow"),
        ("Chapter 7", "Knowledge Graph Engine (Neo4j)"),
        ("Chapter 8", "LLM Integration (Ollama)"),
        ("Chapter 9", "The Simulation Engine (OASIS)"),
        ("Chapter 10", "The Report Agent"),
        ("Chapter 11", "Frontend Architecture"),
        ("Chapter 12", "API Reference"),
        ("Chapter 13", "Performance Optimization"),
        ("Chapter 14", "Operations Manual"),
        ("Chapter 15", "Troubleshooting Guide"),
        ("Chapter 16", "GPU and Memory Management"),
        ("Appendix A", "Command Reference"),
        ("Appendix B", "File Structure"),
        ("Appendix C", "Model Comparison"),
    ]
    for ch, title in toc_chapters:
        story.append(Paragraph(f"<b>{ch}:</b>  {title}", styles['TOCEntry']))
    story.append(PageBreak())

    # ==================== CHAPTER 1 ====================
    story.append(Paragraph("Chapter 1: What is MiroFish-Offline?", styles['ChapterTitle']))
    story.append(Paragraph(
        "MiroFish is a multi-agent simulation engine designed for social dynamics analysis. "
        "You upload a document, such as a press release, policy draft, financial report, or news article, "
        "and the system generates hundreds of AI agents with unique personalities. These agents then "
        "simulate public reaction on social media platforms, posting, arguing, shifting opinions, and "
        "forming consensus, hour by hour across a configurable timeline.", styles['Body']))
    story.append(Paragraph(
        "The original MiroFish was built for the Chinese market: Chinese UI, Zep Cloud for knowledge graphs, "
        "and DashScope/OpenAI APIs for LLM inference. MiroFish-Offline is a complete fork that makes the "
        "entire system local and English:", styles['Body']))
    story.append(make_table(
        ["Original MiroFish", "MiroFish-Offline"],
        [
            ["Chinese UI", "English UI (1,000+ translated strings)"],
            ["Zep Cloud (graph memory)", "Neo4j Community Edition (local)"],
            ["DashScope / OpenAI API", "Ollama (local LLM inference)"],
            ["Zep Cloud embeddings", "nomic-embed-text via Ollama"],
            ["Cloud API keys required", "Zero cloud dependencies"],
            ["Pay-per-call pricing", "Free after hardware setup"],
        ],
        col_widths=[220, 250]
    ))
    story.append(Paragraph("Table 1.1: MiroFish Original vs Offline Comparison", styles['Caption']))

    story.append(Paragraph("1.1 Why Go Offline?", styles['SectionTitle']))
    story.append(Paragraph(
        "The migration to a fully local setup was driven by practical limitations encountered during "
        "development and testing with cloud APIs:", styles['Body']))
    story.append(Paragraph(
        "<b>OpenAI API Rate Limits:</b> The Tier 1 limit of 200,000 tokens per minute was consistently hit "
        "during simulations. MiroFish makes approximately 72+ LLM calls per simulation cycle, and with "
        "hundreds of agents each requiring persona generation, the token budget was exhausted rapidly.", styles['Body']))
    story.append(Paragraph(
        "<b>Zep Cloud Throttling:</b> Episode and rate limits (HTTP 429 errors) made graph building unreliable. "
        "The knowledge graph construction phase requires sustained API access over hours, and intermittent "
        "throttling caused partial builds and data inconsistencies.", styles['Body']))
    story.append(Paragraph(
        "<b>Cost:</b> Running hundreds of agents across dozens of simulation rounds with cloud LLMs generates "
        "substantial API costs. Local inference eliminates this entirely after the initial hardware investment.", styles['Body']))
    story.append(Paragraph(
        "<b>Privacy:</b> Simulation documents may contain sensitive content (unreleased press releases, draft "
        "policies, proprietary financial data). Local processing ensures nothing leaves your machine.", styles['Body']))

    story.append(Paragraph("1.2 Use Cases", styles['SectionTitle']))
    story.append(Paragraph(
        "<b>PR Crisis Testing:</b> Upload a draft press release and simulate public reaction before publishing. "
        "Observe how different demographics respond, what controversies emerge, and how sentiment evolves.", styles['Body']))
    story.append(Paragraph(
        "<b>Trading Signal Generation:</b> Feed financial news articles and observe simulated market sentiment "
        "across agent populations with different risk profiles and investment philosophies.", styles['Body']))
    story.append(Paragraph(
        "<b>Policy Impact Analysis:</b> Test draft regulations against simulated public response. Identify "
        "unexpected objections, gauge support across demographics, and refine messaging.", styles['Body']))
    story.append(Paragraph(
        "<b>Academic Research:</b> Study opinion formation, echo chambers, information cascades, and influence "
        "dynamics in controlled simulated environments with reproducible parameters.", styles['Body']))
    story.append(PageBreak())

    # ==================== CHAPTER 2 ====================
    story.append(Paragraph("Chapter 2: System Architecture Overview", styles['ChapterTitle']))
    story.append(Paragraph(
        "MiroFish-Offline operates as a layered system with four primary services that communicate "
        "through well-defined interfaces:", styles['Body']))

    story.append(Paragraph("2.1 The Four Services", styles['SectionTitle']))
    story.append(make_table(
        ["Service", "Technology", "Port", "Role", "Runs As"],
        [
            ["Frontend", "Vue 3 + Vite", "3000", "User interface, visualization", "npm run dev"],
            ["Backend", "Flask (Python 3.11)", "5001", "API server, orchestration", "python run.py"],
            ["Graph DB", "Neo4j Community Ed.", "7474/7687", "Knowledge graph storage", "brew service"],
            ["LLM Engine", "Ollama + qwen2.5", "11434", "Language model inference", "Menu bar app"],
        ],
        col_widths=[70, 95, 60, 130, 100]
    ))
    story.append(Paragraph("Table 2.1: Service Overview", styles['Caption']))

    story.append(Paragraph("2.2 Data Flow Architecture", styles['SectionTitle']))
    story.append(Paragraph(
        "The system follows a strict layered architecture with dependency injection:", styles['Body']))
    story.append(Paragraph(
        "<b>Layer 1 - Flask API:</b> Three blueprints (graph.py, simulation.py, report.py) handle HTTP "
        "requests and coordinate the workflow. Each blueprint accesses shared services through "
        "Flask's app.extensions dictionary.", styles['Body']))
    story.append(Paragraph(
        "<b>Layer 2 - Service Layer:</b> Business logic lives in dedicated service classes: "
        "EntityReader, GraphToolsService, GraphMemoryUpdater, SimulationRunner, ReportAgent, "
        "OasisProfileGenerator, and SimulationConfigGenerator.", styles['Body']))
    story.append(Paragraph(
        "<b>Layer 3 - Storage Abstraction:</b> GraphStorage is an abstract interface. Neo4jStorage "
        "implements it, providing NER extraction, embedding, and graph operations. This design allows "
        "swapping Neo4j for any other graph database by implementing a single class.", styles['Body']))
    story.append(Paragraph(
        "<b>Layer 4 - External Services:</b> Neo4j CE for graph storage, Ollama for LLM inference "
        "and embeddings. These run independently and communicate via network protocols (Bolt for "
        "Neo4j, HTTP for Ollama).", styles['Body']))

    story.append(Paragraph("2.3 Key Design Decisions", styles['SectionTitle']))
    story.append(Paragraph(
        "<b>Dependency Injection:</b> No global singletons. The Neo4jStorage instance is created in "
        "the Flask app factory and stored in app.extensions['neo4j_storage']. All services receive "
        "their dependencies explicitly.", styles['Body']))
    story.append(Paragraph(
        "<b>Hybrid Search:</b> Information retrieval uses a weighted combination: 70% vector similarity "
        "(cosine distance on nomic-embed-text embeddings) + 30% BM25 keyword search. This balances "
        "semantic understanding with exact term matching.", styles['Body']))
    story.append(Paragraph(
        "<b>Synchronous NER:</b> Entity extraction runs synchronously via local LLM, replacing Zep's "
        "asynchronous episode processing. This simplifies the pipeline at the cost of longer processing "
        "time per chunk, but eliminates the need for polling and callback mechanisms.", styles['Body']))
    story.append(PageBreak())

    # ==================== CHAPTER 3 ====================
    story.append(Paragraph("Chapter 3: The Technology Stack", styles['ChapterTitle']))

    story.append(Paragraph("3.1 Backend Technologies", styles['SectionTitle']))
    story.append(make_table(
        ["Package", "Version", "Purpose"],
        [
            ["Flask", ">=3.0.0", "Web framework and API server"],
            ["flask-cors", ">=6.0.0", "Cross-origin request handling"],
            ["openai (SDK)", ">=1.0.0", "OpenAI-compatible client (talks to Ollama)"],
            ["neo4j (driver)", ">=5.15.0", "Neo4j graph database driver"],
            ["camel-oasis", "0.2.5", "OASIS social media simulation framework"],
            ["camel-ai", "0.2.78", "Multi-agent AI framework (underlies OASIS)"],
            ["PyMuPDF", ">=1.24.0", "PDF document parsing and text extraction"],
            ["pydantic", ">=2.0.0", "Data validation and settings management"],
            ["python-dotenv", ">=1.0.0", "Environment variable loading from .env"],
            ["charset-normalizer", ">=3.0.0", "Character encoding detection"],
        ],
        col_widths=[120, 80, 270]
    ))
    story.append(Paragraph("Table 3.1: Backend Dependencies", styles['Caption']))

    story.append(Paragraph("3.2 Frontend Technologies", styles['SectionTitle']))
    story.append(Paragraph(
        "The frontend is a Vue 3 single-page application using the Composition API. It communicates "
        "with the backend exclusively through REST API calls via Axios. Vite serves as the build tool "
        "and development server. D3.js powers the interactive knowledge graph visualization.", styles['Body']))

    story.append(Paragraph("3.3 Ollama and Model Selection", styles['SectionTitle']))
    story.append(Paragraph(
        "Ollama provides an OpenAI-compatible API endpoint for local LLM inference. MiroFish uses the "
        "OpenAI Python SDK pointed at Ollama's endpoint (localhost:11434/v1), making the code compatible "
        "with any OpenAI-format provider.", styles['Body']))
    story.append(make_table(
        ["Model", "Parameters", "Size", "Speed/Chunk", "JSON Reliability", "Best For"],
        [
            ["qwen2.5:72b", "72B", "47 GB", "~45 sec", "Excellent", "Maximum quality, final runs"],
            ["qwen2.5:32b", "32B", "20 GB", "~15 sec", "Excellent", "Best balance of speed/quality"],
            ["qwen2.5:14b", "14B", "9 GB", "~8 sec", "Very Good", "Fast iteration and testing"],
            ["qwen3:30b", "30B", "19 GB", "~20 sec", "Poor (reasoning tokens)", "NOT recommended for MiroFish"],
        ],
        col_widths=[80, 60, 50, 70, 80, 130]
    ))
    story.append(Paragraph("Table 3.2: Model Comparison for MiroFish Workloads", styles['Caption']))
    story.append(Paragraph(
        "<b>Critical Warning:</b> Reasoning models (qwen3, deepseek-r1) output chain-of-thought tokens "
        "before the actual response. This breaks MiroFish's JSON parsing because the NER extractor "
        "expects clean JSON output. Always use dense models from the qwen2.5 family.",
        styles['Warning']))

    story.append(Paragraph("3.4 Neo4j Community Edition", styles['SectionTitle']))
    story.append(Paragraph(
        "Neo4j serves as the knowledge graph database, storing entities (people, organizations, events) "
        "and their relationships extracted from uploaded documents. It also stores agent memories during "
        "simulation. The Bolt protocol (port 7687) handles driver connections, while the HTTP interface "
        "(port 7474) provides the Neo4j Browser for visual graph exploration.", styles['Body']))

    story.append(Paragraph("3.5 Embedding Model: nomic-embed-text", styles['SectionTitle']))
    story.append(Paragraph(
        "nomic-embed-text generates 768-dimensional vector embeddings for text passages. These vectors "
        "enable semantic similarity search within the knowledge graph. When a query comes in, the system "
        "embeds the query text and finds the closest matching graph nodes by cosine distance, combined "
        "with BM25 keyword matching (70/30 split).", styles['Body']))
    story.append(PageBreak())

    # ==================== CHAPTER 4 ====================
    story.append(Paragraph("Chapter 4: Installation and Environment Setup", styles['ChapterTitle']))

    story.append(Paragraph("4.1 Prerequisites", styles['SectionTitle']))
    story.append(make_table(
        ["Component", "Requirement", "Installation"],
        [
            ["macOS", "Apple Silicon (M1/M2/M3/M4)", "Built-in"],
            ["Homebrew", "Latest", "/bin/bash -c \"$(curl -fsSL ...)\""],
            ["Python", "3.11+", "brew install python@3.11"],
            ["Node.js", "18+", "brew install node"],
            ["Neo4j", "5.15+", "brew install neo4j"],
            ["Ollama", "0.20+", "Download from ollama.com"],
        ],
        col_widths=[80, 130, 260]
    ))
    story.append(Paragraph("Table 4.1: Prerequisites", styles['Caption']))

    story.append(Paragraph("4.2 Step-by-Step Installation", styles['SectionTitle']))
    story.append(Paragraph("<b>Step 1: Clone the Repository</b>", styles['SubSection']))
    story.append(Paragraph("git clone https://github.com/H-Jan/MiroFishLocal.git<br/>"
                           "cd MiroFish-Offline", styles['CodeBlock']))

    story.append(Paragraph("<b>Step 2: Create Python Virtual Environment</b>", styles['SubSection']))
    story.append(Paragraph("python3.11 -m venv venv<br/>"
                           "source venv/bin/activate", styles['CodeBlock']))

    story.append(Paragraph("<b>Step 3: Install Backend Dependencies</b>", styles['SubSection']))
    story.append(Paragraph("pip install -r backend/requirements.txt", styles['CodeBlock']))

    story.append(Paragraph("<b>Step 4: Install Frontend Dependencies</b>", styles['SubSection']))
    story.append(Paragraph("cd frontend<br/>npm install<br/>cd ..", styles['CodeBlock']))

    story.append(Paragraph("<b>Step 5: Configure Environment</b>", styles['SubSection']))
    story.append(Paragraph("cp .env.example .env<br/>"
                           "# Edit .env to set your preferred model", styles['CodeBlock']))

    story.append(Paragraph("<b>Step 6: Pull Ollama Models</b>", styles['SubSection']))
    story.append(Paragraph("ollama pull qwen2.5:32b<br/>"
                           "ollama pull nomic-embed-text", styles['CodeBlock']))

    story.append(Paragraph("<b>Step 7: Start Neo4j</b>", styles['SubSection']))
    story.append(Paragraph("brew services start neo4j", styles['CodeBlock']))
    story.append(Paragraph(
        "On first run, change the default password. The default credentials are neo4j/neo4j. "
        "Change the password to 'mirofish' to match the .env configuration.", styles['Body']))

    story.append(Paragraph("4.3 The .env Configuration File", styles['SectionTitle']))
    story.append(Paragraph(
        "The .env file controls all service connections. For a fully local setup, all URLs point "
        "to localhost:", styles['Body']))
    story.append(Paragraph(
        "LLM_API_KEY=ollama<br/>"
        "LLM_BASE_URL=http://localhost:11434/v1<br/>"
        "LLM_MODEL_NAME=qwen2.5:32b<br/><br/>"
        "NEO4J_URI=bolt://localhost:7687<br/>"
        "NEO4J_USER=neo4j<br/>"
        "NEO4J_PASSWORD=mirofish<br/><br/>"
        "EMBEDDING_MODEL=nomic-embed-text<br/>"
        "EMBEDDING_BASE_URL=http://localhost:11434<br/><br/>"
        "OPENAI_API_KEY=ollama<br/>"
        "OPENAI_API_BASE_URL=http://localhost:11434/v1",
        styles['CodeBlock']))
    story.append(Paragraph(
        "To change the LLM model, edit the LLM_MODEL_NAME line and restart the backend. "
        "No other changes are needed.", styles['Body']))
    story.append(PageBreak())

    # ==================== CHAPTER 5 ====================
    story.append(Paragraph("Chapter 5: Configuration Deep Dive", styles['ChapterTitle']))

    story.append(Paragraph("5.1 Text Processing Parameters", styles['SectionTitle']))
    story.append(make_table(
        ["Parameter", "Default", "Location", "Effect"],
        [
            ["DEFAULT_CHUNK_SIZE", "3000", "config.py", "Characters per text chunk for NER extraction"],
            ["DEFAULT_CHUNK_OVERLAP", "50", "config.py", "Overlap between adjacent chunks"],
            ["batch_size", "10", "graph_builder.py", "Chunks processed per batch iteration"],
            ["max_workers", "8", "graph_builder.py", "Parallel threads for chunk processing"],
            ["OLLAMA_NUM_CTX", "8192", "llm_client.py", "LLM context window size (tokens)"],
        ],
        col_widths=[120, 60, 110, 180]
    ))
    story.append(Paragraph("Table 5.1: Text Processing Configuration", styles['Caption']))
    story.append(Paragraph(
        "Chunk size directly determines the number of LLM calls needed for graph building. "
        "A 1,000,000 character document at chunk_size=3000 produces ~333 chunks, each requiring "
        "one NER extraction call and one embedding call. Increasing chunk size reduces total calls "
        "but may cause the LLM to miss entities in dense passages.", styles['Body']))
    story.append(Paragraph(
        "<b>Important:</b> Increasing OLLAMA_NUM_CTX from 8192 to 16384 was tested and caused a 10x "
        "slowdown in inference speed (4 seconds to 42 seconds per call). The larger KV cache consumes "
        "significantly more GPU memory on Apple Silicon. Keep it at 8192.",
        styles['Warning']))

    story.append(Paragraph("5.2 Simulation Parameters", styles['SectionTitle']))
    story.append(make_table(
        ["Parameter", "Default", "Effect"],
        [
            ["total_simulation_hours", "72 (3 days)", "Simulated time span"],
            ["minutes_per_round", "60", "Each round = 1 simulated hour"],
            ["agents_per_hour_min", "5-20", "Minimum active agents per round"],
            ["agents_per_hour_max", "20-80", "Maximum active agents per round"],
            ["peak_hours", "[19,20,21,22]", "Evening peak activity hours"],
            ["off_peak_hours", "[0,1,2,3,4,5]", "Near-zero activity hours"],
            ["echo_chamber_effect", "0.5", "Strength of opinion reinforcement"],
            ["viral_threshold", "10", "Interactions needed for viral spread"],
        ],
        col_widths=[130, 100, 240]
    ))
    story.append(Paragraph("Table 5.2: Simulation Configuration", styles['Caption']))

    story.append(Paragraph("5.3 Timeout Configuration", styles['SectionTitle']))
    story.append(Paragraph(
        "Both the backend LLM client and frontend API client have timeout settings. These were "
        "increased from the defaults to handle large documents with local LLMs:", styles['Body']))
    story.append(make_table(
        ["Component", "File", "Default", "Modified", "Purpose"],
        [
            ["LLM Client", "llm_client.py", "300s (5 min)", "3600s (1 hr)", "Backend LLM call timeout"],
            ["Frontend API", "api/index.js", "300,000ms", "3,600,000ms", "Frontend request timeout"],
        ],
        col_widths=[80, 90, 80, 80, 140]
    ))
    story.append(Paragraph("Table 5.3: Timeout Configuration", styles['Caption']))

    story.append(Paragraph("5.4 Ollama Environment Variables", styles['SectionTitle']))
    story.append(make_table(
        ["Variable", "Value", "Effect"],
        [
            ["OLLAMA_NUM_PARALLEL", "2", "Concurrent inference requests (set via launchctl)"],
            ["OLLAMA_FLASH_ATTENTION", "1", "Enable Flash Attention for faster inference"],
            ["OLLAMA_KEEP_ALIVE", "5m", "Auto-unload model after 5 min idle"],
        ],
        col_widths=[150, 60, 260]
    ))
    story.append(Paragraph("Table 5.4: Ollama Environment Variables", styles['Caption']))
    story.append(Paragraph(
        "Set these via: launchctl setenv OLLAMA_NUM_PARALLEL 2<br/>"
        "Then quit and reopen the Ollama app for changes to take effect.",
        styles['CodeBlock']))
    story.append(PageBreak())

    # ==================== CHAPTER 6 ====================
    story.append(Paragraph("Chapter 6: The Five-Step Workflow", styles['ChapterTitle']))

    story.append(Paragraph("6.1 Step 1: Graph Build", styles['SectionTitle']))
    story.append(Paragraph(
        "The graph build phase transforms your uploaded document into a structured knowledge graph. "
        "This is the most time-intensive step and involves:", styles['Body']))
    story.append(Paragraph(
        "<b>Document Upload:</b> Accepts PDF, Markdown, or plain text files up to 50MB. PyMuPDF handles "
        "PDF extraction, preserving text structure and layout.", styles['Body']))
    story.append(Paragraph(
        "<b>Ontology Generation:</b> The LLM analyzes a sample of the document to identify relevant "
        "entity types (Person, Organization, Event, etc.) and relationship types (allied_with, "
        "opposes, sanctions, etc.). This ontology guides all subsequent extraction.", styles['Body']))
    story.append(Paragraph(
        "<b>Text Chunking:</b> The document is split into chunks of ~3000 characters with 50-character "
        "overlap. Splitting occurs at sentence boundaries when possible.", styles['Body']))
    story.append(Paragraph(
        "<b>NER Extraction:</b> Each chunk is sent to the LLM with the ontology as context. The LLM "
        "returns structured JSON with extracted entities and relationships. This is the most LLM-intensive "
        "step: for a 1M character document with 3000-char chunks, this means ~333 LLM calls.", styles['Body']))
    story.append(Paragraph(
        "<b>Embedding:</b> Each entity name and relationship description is embedded via nomic-embed-text "
        "to enable semantic search later.", styles['Body']))
    story.append(Paragraph(
        "<b>Graph Construction:</b> Entities become Neo4j nodes, relationships become edges. Duplicate "
        "entities are merged by normalized name (case-insensitive matching).", styles['Body']))

    story.append(Paragraph("6.2 Step 2: Environment Setup", styles['SectionTitle']))
    story.append(Paragraph(
        "This step generates the simulation environment: agent profiles and simulation configuration.", styles['Body']))
    story.append(Paragraph(
        "<b>Entity Filtering:</b> The system identifies which graph entities should become agents. "
        "Individual entities (people, officials, journalists) get personal personas. Group entities "
        "(organizations, companies, media outlets) get representative personas.", styles['Body']))
    story.append(Paragraph(
        "<b>Profile Generation:</b> For each entity, the LLM generates a detailed social media persona "
        "including: bio, personality description, age, gender, MBTI type, country, profession, "
        "interested topics, posting behavior, sentiment bias, and influence weight. This requires "
        "one LLM call per agent.", styles['Body']))
    story.append(Paragraph(
        "<b>Configuration Generation:</b> The LLM analyzes the document context and agent population "
        "to generate timing parameters, event triggers, platform settings, and per-agent activity "
        "configurations. Agents are processed in batches of 15.", styles['Body']))
    story.append(Paragraph(
        "<b>Custom Rounds:</b> You can set a custom round count (e.g., 25) using the checkbox and "
        "slider in the UI. This overrides the auto-generated round count.", styles['Body']))

    story.append(Paragraph("6.3 Step 3: Simulation", styles['SectionTitle']))
    story.append(Paragraph(
        "The simulation runs agents on parallel Twitter and Reddit platforms. Each round represents "
        "one simulated hour. During each round, a subset of agents become active based on the time "
        "configuration and their individual activity schedules.", styles['Body']))
    story.append(Paragraph(
        "Active agents can: create posts, like posts, repost, follow other agents, quote posts, "
        "create comments, or do nothing. Their actions are determined by their persona, the current "
        "discourse, their sentiment bias, and their memory of past interactions.", styles['Body']))
    story.append(Paragraph(
        "With graph memory update enabled, agent activities are written back to the Neo4j knowledge "
        "graph, allowing agents to reference past events in subsequent rounds.", styles['Body']))

    story.append(Paragraph("6.4 Step 4: Report Generation", styles['SectionTitle']))
    story.append(Paragraph(
        "The ReportAgent analyzes the simulation using a ReACT (Reasoning + Acting) pattern. It:", styles['Body']))
    story.append(Paragraph(
        "1. Plans a report outline with multiple sections<br/>"
        "2. For each section, performs research using graph tools (Search, InsightForge, Panorama)<br/>"
        "3. Interviews simulated agents about their behavior<br/>"
        "4. Reflects on findings and generates structured analysis<br/>"
        "5. Produces a comprehensive markdown report", styles['Body']))

    story.append(Paragraph("6.5 Step 5: Interaction", styles['SectionTitle']))
    story.append(Paragraph(
        "After the simulation, you can chat with any agent. They respond in character, drawing on "
        "their persona, their simulation history, and their knowledge graph memories. This enables "
        "deep qualitative analysis of why agents behaved the way they did.", styles['Body']))
    story.append(PageBreak())

    # ==================== CHAPTER 7 ====================
    story.append(Paragraph("Chapter 7: Knowledge Graph Engine (Neo4j)", styles['ChapterTitle']))

    story.append(Paragraph("7.1 Graph Structure", styles['SectionTitle']))
    story.append(Paragraph(
        "Each project creates a graph identified by a UUID (graph_id). All nodes and edges within "
        "that graph share this identifier, enabling multiple projects to coexist in the same Neo4j "
        "instance.", styles['Body']))
    story.append(Paragraph(
        "<b>Node Properties:</b> graph_id, name, name_lower (for deduplication), entity_type, "
        "attributes (JSON), embedding (768-dim vector), created_at, updated_at.", styles['Body']))
    story.append(Paragraph(
        "<b>Edge Properties:</b> graph_id, relation_type, fact (description), source_text, "
        "embedding (768-dim vector), created_at.", styles['Body']))

    story.append(Paragraph("7.2 Deduplication Strategy", styles['SectionTitle']))
    story.append(Paragraph(
        "Entity deduplication uses MERGE on (graph_id + name_lower). This means 'Barack Obama', "
        "'BARACK OBAMA', and 'barack obama' all resolve to the same node. Attributes are merged "
        "rather than overwritten, accumulating information across chunks.", styles['Body']))

    story.append(Paragraph("7.3 Hybrid Search", styles['SectionTitle']))
    story.append(Paragraph(
        "When the system needs to find relevant information (e.g., for report generation or agent "
        "memory retrieval), it uses hybrid search:", styles['Body']))
    story.append(Paragraph(
        "<b>Vector Component (70%):</b> Embeds the query, finds nearest neighbors by cosine similarity "
        "across all node and edge embeddings.", styles['Body']))
    story.append(Paragraph(
        "<b>Keyword Component (30%):</b> BM25 text search across node names, edge facts, and entity "
        "attributes. Handles exact matches and terminology that embedding similarity might miss.", styles['Body']))

    story.append(Paragraph("7.4 Accessing Neo4j Browser", styles['SectionTitle']))
    story.append(Paragraph(
        "Open http://localhost:7474 in your browser. Login with neo4j/mirofish. You can run Cypher "
        "queries to explore the graph directly. Useful queries:", styles['Body']))
    story.append(Paragraph(
        "// Count all nodes in a graph<br/>"
        "MATCH (n) WHERE n.graph_id = 'your-graph-id' RETURN count(n)<br/><br/>"
        "// Find all entity types<br/>"
        "MATCH (n) WHERE n.graph_id = 'your-graph-id' RETURN DISTINCT n.entity_type, count(n)<br/><br/>"
        "// Find relationships for a specific entity<br/>"
        "MATCH (n)-[r]-(m) WHERE n.name =~ '(?i).*iran.*' RETURN n, r, m LIMIT 50",
        styles['CodeBlock']))
    story.append(PageBreak())

    # ==================== CHAPTER 8 ====================
    story.append(Paragraph("Chapter 8: LLM Integration (Ollama)", styles['ChapterTitle']))

    story.append(Paragraph("8.1 How Ollama Connects to MiroFish", styles['SectionTitle']))
    story.append(Paragraph(
        "MiroFish uses the OpenAI Python SDK configured to point at Ollama's OpenAI-compatible "
        "endpoint. This is set up in llm_client.py:", styles['Body']))
    story.append(Paragraph(
        "self.client = OpenAI(<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;api_key='ollama',<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;base_url='http://localhost:11434/v1',<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;timeout=3600.0,<br/>"
        ")", styles['CodeBlock']))
    story.append(Paragraph(
        "The api_key value is arbitrary (Ollama ignores it). The base_url points to Ollama's "
        "OpenAI-compatible endpoint. All standard OpenAI SDK methods work: chat completions, "
        "JSON mode, function calling.", styles['Body']))

    story.append(Paragraph("8.2 Context Window Management", styles['SectionTitle']))
    story.append(Paragraph(
        "Ollama defaults to a 2048-token context window, which is too small for NER extraction "
        "on 3000-character chunks. MiroFish overrides this to 8192 via the num_ctx parameter:", styles['Body']))
    story.append(Paragraph(
        "extra_body = {'options': {'num_ctx': 8192}}", styles['CodeBlock']))
    story.append(Paragraph(
        "This is automatically applied to all Ollama requests when the LLM client detects port "
        "11434 in the base URL.", styles['Body']))

    story.append(Paragraph("8.3 GPU Memory Allocation", styles['SectionTitle']))
    story.append(Paragraph(
        "On Apple Silicon, CPU and GPU share unified memory. When Ollama loads a model, it allocates "
        "memory for both model weights and KV cache (for context processing):", styles['Body']))
    story.append(make_table(
        ["Component", "qwen2.5:32b", "qwen2.5:72b"],
        [
            ["Model Weights", "~20 GB", "~47 GB"],
            ["KV Cache (per parallel slot)", "~10 GB", "~10 GB"],
            ["Total (2 parallel)", "~40 GB", "~67 GB"],
            ["Total (8 parallel)", "~100 GB", "~127 GB"],
        ],
        col_widths=[160, 150, 150]
    ))
    story.append(Paragraph("Table 8.1: GPU Memory Allocation by Model", styles['Caption']))
    story.append(Paragraph(
        "macOS reports GPU-allocated memory as 'wired memory' in Activity Monitor. The model "
        "auto-unloads after 5 minutes of inactivity, returning memory to the system.",
        styles['Body']))

    story.append(Paragraph("8.4 Parallel Inference", styles['SectionTitle']))
    story.append(Paragraph(
        "OLLAMA_NUM_PARALLEL controls how many simultaneous inference requests Ollama can handle. "
        "Each parallel slot requires its own KV cache allocation. Testing showed that increasing "
        "parallel slots beyond 2 does not improve total throughput because the GPU processes "
        "requests sequentially. More slots simply divide GPU time across more waiting requests, "
        "with each individual request taking proportionally longer.", styles['Body']))
    story.append(Paragraph(
        "Recommended: OLLAMA_NUM_PARALLEL=2 for qwen2.5:32b on 128GB Apple Silicon.",
        styles['Warning']))
    story.append(PageBreak())

    # ==================== CHAPTER 9 ====================
    story.append(Paragraph("Chapter 9: The Simulation Engine (OASIS)", styles['ChapterTitle']))
    story.append(Paragraph(
        "OASIS (camel-oasis) is the multi-agent simulation framework that powers MiroFish's social "
        "media simulation. It was developed by the CAMEL-AI team and provides the infrastructure "
        "for agent-based interaction on simulated platforms.", styles['Body']))

    story.append(Paragraph("9.1 Agent Anatomy", styles['SectionTitle']))
    story.append(Paragraph(
        "Each simulated agent has:", styles['Body']))
    story.append(Paragraph(
        "<b>Profile:</b> Name, bio, age, gender, MBTI, profession, country, interests.<br/>"
        "<b>Activity Config:</b> Activity level (0-1), posts per hour, active hours, response delay, "
        "sentiment bias (-1 to +1), stance (supportive/opposing/neutral/observer), influence weight.<br/>"
        "<b>Platform Accounts:</b> Twitter profile (followers, friends, statuses) and Reddit profile "
        "(karma, subscribed communities).<br/>"
        "<b>Memory:</b> Graph-based memory of past interactions and knowledge from the source document.",
        styles['Body']))

    story.append(Paragraph("9.2 Simulation Rounds", styles['SectionTitle']))
    story.append(Paragraph(
        "Each round represents one simulated hour. The simulation engine:", styles['Body']))
    story.append(Paragraph(
        "1. Selects active agents based on time-of-day multipliers and individual schedules<br/>"
        "2. Each active agent observes the current social media feed<br/>"
        "3. The LLM generates an action for each agent based on their persona and observations<br/>"
        "4. Actions are executed (posts created, likes registered, follows established)<br/>"
        "5. The platform's recommendation algorithm updates feeds<br/>"
        "6. Graph memory is updated (if enabled)", styles['Body']))

    story.append(Paragraph("9.3 Platform Mechanics", styles['SectionTitle']))
    story.append(Paragraph(
        "The recommendation algorithm weights content by: recency (40%), popularity (30%), and "
        "relevance (30%). An echo chamber effect (strength 0.5) biases agents toward content "
        "matching their existing sentiment. Content goes viral after reaching 10 interactions.", styles['Body']))

    story.append(Paragraph("9.4 Round Limits", styles['SectionTitle']))
    story.append(Paragraph(
        "The auto-generated config often specifies 1440 rounds (72 hours at 60 min/round). This "
        "is typically truncated to a manageable number. Set custom rounds in Step 2's UI to control "
        "simulation duration. Each round takes approximately 1-2 minutes with the 32b model.", styles['Body']))
    story.append(PageBreak())

    # ==================== CHAPTER 10 ====================
    story.append(Paragraph("Chapter 10: The Report Agent", styles['ChapterTitle']))
    story.append(Paragraph(
        "The ReportAgent is an autonomous AI system that analyzes simulation results using the "
        "ReACT pattern: Reasoning, Acting (tool use), and Reflection.", styles['Body']))

    story.append(Paragraph("10.1 ReACT Pattern", styles['SectionTitle']))
    story.append(Paragraph(
        "For each report section, the agent cycles through:", styles['Body']))
    story.append(Paragraph(
        "<b>Thought:</b> Analyzes what information is needed for this section.<br/>"
        "<b>Action:</b> Calls a tool to gather evidence (search the graph, interview an agent, etc.).<br/>"
        "<b>Observation:</b> Processes the tool result.<br/>"
        "<b>Reflection:</b> Evaluates whether sufficient evidence has been gathered.<br/>"
        "<b>Generation:</b> Writes the section content based on gathered evidence.", styles['Body']))

    story.append(Paragraph("10.2 Available Tools", styles['SectionTitle']))
    story.append(make_table(
        ["Tool", "Purpose", "How It Works"],
        [
            ["Search", "Find relevant facts", "Hybrid vector/keyword search in Neo4j"],
            ["InsightForge", "Extract key insights", "Summarize entity information and patterns"],
            ["Panorama", "Overview relationships", "Map entity connections and influence"],
            ["Interview", "Query agents", "Ask simulated agents about their actions"],
        ],
        col_widths=[80, 120, 270]
    ))
    story.append(Paragraph("Table 10.1: Report Agent Tools", styles['Caption']))

    story.append(Paragraph("10.3 Configuration", styles['SectionTitle']))
    story.append(Paragraph(
        "REPORT_AGENT_MAX_TOOL_CALLS (default 5) limits tool invocations per section. "
        "REPORT_AGENT_MAX_REFLECTION_ROUNDS (default 2) limits ReACT cycles. "
        "REPORT_AGENT_TEMPERATURE (default 0.5) controls creativity vs determinism.", styles['Body']))
    story.append(PageBreak())

    # ==================== CHAPTER 11 ====================
    story.append(Paragraph("Chapter 11: Frontend Architecture", styles['ChapterTitle']))
    story.append(Paragraph(
        "The frontend is a Vue 3 single-page application with seven primary view components:", styles['Body']))
    story.append(make_table(
        ["View", "URL", "Purpose"],
        [
            ["Home.vue", "/", "Landing page, project dashboard, simulation history"],
            ["Process.vue", "/process", "Graph build phase with real-time visualization"],
            ["MainView.vue", "/main", "Main workflow container (all 5 steps)"],
            ["SimulationView.vue", "/simulation", "Simulation configuration and monitoring"],
            ["SimulationRunView.vue", "/simulation-run", "Live simulation progress"],
            ["ReportView.vue", "/report", "Report generation and display"],
            ["InteractionView.vue", "/interaction", "Chat with simulated agents"],
        ],
        col_widths=[120, 90, 260]
    ))
    story.append(Paragraph("Table 11.1: Frontend Views", styles['Caption']))

    story.append(Paragraph("11.1 Graph Visualization", styles['SectionTitle']))
    story.append(Paragraph(
        "The knowledge graph is rendered using D3.js force-directed layout. Nodes are colored by "
        "entity type, sized by connection count, and labeled with entity names. The graph supports "
        "drag-to-pan, scroll-to-zoom, and click-to-select interactions. It refreshes every 10 seconds "
        "during graph building to show progress in real time.", styles['Body']))

    story.append(Paragraph("11.2 API Communication", styles['SectionTitle']))
    story.append(Paragraph(
        "All frontend-backend communication uses Axios HTTP client configured in api/index.js. "
        "The base URL defaults to http://localhost:5001. The timeout is set to 3,600,000ms (1 hour) "
        "to accommodate long-running LLM operations.", styles['Body']))
    story.append(PageBreak())

    # ==================== CHAPTER 12 ====================
    story.append(Paragraph("Chapter 12: API Reference", styles['ChapterTitle']))

    story.append(Paragraph("12.1 Graph API (/api/graph)", styles['SectionTitle']))
    story.append(make_table(
        ["Method", "Endpoint", "Purpose"],
        [
            ["GET", "/project/list", "List all projects"],
            ["GET", "/project/{id}", "Get project details"],
            ["DELETE", "/project/{id}", "Delete a project"],
            ["POST", "/project/{id}/reset", "Reset project state"],
            ["POST", "/ontology/generate", "Generate ontology from document"],
            ["POST", "/build", "Start graph building"],
            ["GET", "/task/{id}", "Poll task progress"],
            ["GET", "/tasks", "List all tasks"],
            ["GET", "/data/{graph_id}", "Get complete graph data"],
            ["DELETE", "/delete/{graph_id}", "Delete a graph"],
        ],
        col_widths=[60, 150, 260]
    ))
    story.append(Paragraph("Table 12.1: Graph API Endpoints (10 total)", styles['Caption']))

    story.append(Paragraph("12.2 Simulation API (/api/simulation)", styles['SectionTitle']))
    story.append(make_table(
        ["Method", "Endpoint", "Purpose"],
        [
            ["POST", "/create", "Create new simulation"],
            ["POST", "/prepare", "Prepare simulation environment"],
            ["POST", "/start", "Start simulation run"],
            ["POST", "/stop", "Stop running simulation"],
            ["GET", "/{id}/run-status", "Get simulation progress"],
            ["GET", "/{id}/posts", "Get simulated posts"],
            ["GET", "/{id}/actions", "Get agent actions log"],
            ["GET", "/{id}/timeline", "Get simulation timeline"],
            ["POST", "/interview", "Interview an agent"],
            ["GET", "/list", "List all simulations"],
            ["GET", "/history", "Get simulation history"],
        ],
        col_widths=[60, 150, 260]
    ))
    story.append(Paragraph("Table 12.2: Simulation API Endpoints (31 total, key ones shown)", styles['Caption']))

    story.append(Paragraph("12.3 Report API (/api/report)", styles['SectionTitle']))
    story.append(make_table(
        ["Method", "Endpoint", "Purpose"],
        [
            ["POST", "/generate", "Start report generation"],
            ["GET", "/{id}", "Get report content"],
            ["GET", "/{id}/progress", "Get generation progress"],
            ["GET", "/{id}/sections", "Get report sections"],
            ["GET", "/{id}/agent-log", "Get ReACT agent log"],
            ["GET", "/{id}/console-log", "Get console output"],
            ["POST", "/chat", "Chat with report context"],
            ["GET", "/list", "List all reports"],
            ["DELETE", "/{id}", "Delete a report"],
        ],
        col_widths=[60, 150, 260]
    ))
    story.append(Paragraph("Table 12.3: Report API Endpoints (18 total, key ones shown)", styles['Caption']))

    story.append(Paragraph("12.4 Health Check", styles['SectionTitle']))
    story.append(Paragraph(
        "GET /health - Returns {'status': 'ok', 'service': 'MiroFish-Offline Backend'}", styles['CodeBlock']))
    story.append(PageBreak())

    # ==================== CHAPTER 13 ====================
    story.append(Paragraph("Chapter 13: Performance Optimization", styles['ChapterTitle']))

    story.append(Paragraph("13.1 Optimizations Applied", styles['SectionTitle']))
    story.append(make_table(
        ["Optimization", "Before", "After", "Impact"],
        [
            ["Chunk size", "500 chars", "3000 chars", "6x fewer LLM calls"],
            ["Batch size", "3", "10", "Better progress tracking"],
            ["Parallel workers", "1 (sequential)", "8 (ThreadPool)", "Overlapping I/O operations"],
            ["LLM timeout", "300s", "3600s", "No timeout on large docs"],
            ["Frontend timeout", "5 min", "1 hour", "No timeout on large docs"],
            ["Auto-reloader", "Enabled", "Disabled", "No more killed simulations"],
            ["OLLAMA_NUM_PARALLEL", "1", "2", "Slight throughput improvement"],
            ["OLLAMA_FLASH_ATTENTION", "0", "1", "Faster attention computation"],
        ],
        col_widths=[110, 80, 100, 180]
    ))
    story.append(Paragraph("Table 13.1: Performance Optimizations", styles['Caption']))

    story.append(Paragraph("13.2 What Did NOT Help", styles['SectionTitle']))
    story.append(Paragraph(
        "<b>Increasing OLLAMA_NUM_PARALLEL beyond 2:</b> With 8 parallel slots, the 32b model used "
        "~100GB for KV caches, leaving little bandwidth for actual inference. Individual chunk times "
        "increased from ~15s to ~350s. Total throughput was actually worse than sequential.", styles['Body']))
    story.append(Paragraph(
        "<b>Increasing OLLAMA_NUM_CTX to 16384:</b> Doubled the KV cache size per slot, causing a "
        "10x slowdown (4s to 42s per inference call). The 8192 default is optimal for this hardware.", styles['Body']))

    story.append(Paragraph("13.3 Estimated Processing Times", styles['SectionTitle']))
    story.append(make_table(
        ["Phase", "1M Char Document", "Variables"],
        [
            ["Ontology Generation", "2-5 minutes", "Document complexity"],
            ["Graph Build (qwen2.5:32b)", "1.5-3 hours", "Chunk size, model speed"],
            ["Graph Build (qwen2.5:14b)", "30-45 minutes", "Chunk size, model speed"],
            ["Profile Generation (1151 agents)", "1-2 hours", "Agent count, model speed"],
            ["Simulation (25 rounds)", "35-50 minutes", "Round count, agent count"],
            ["Report Generation", "15-30 minutes", "Section count, tool calls"],
        ],
        col_widths=[160, 130, 180]
    ))
    story.append(Paragraph("Table 13.2: Estimated Processing Times", styles['Caption']))
    story.append(PageBreak())

    # ==================== CHAPTER 14 ====================
    story.append(Paragraph("Chapter 14: Operations Manual", styles['ChapterTitle']))

    story.append(Paragraph("14.1 Starting MiroFish", styles['SectionTitle']))
    story.append(Paragraph(
        "Ensure Ollama is running (menu bar icon visible) and Neo4j is running:", styles['Body']))
    story.append(Paragraph("brew services start neo4j", styles['CodeBlock']))
    story.append(Paragraph("Open two terminals in VSCode:", styles['Body']))
    story.append(Paragraph(
        "<b>Terminal 1 (Backend):</b><br/>"
        "cd /Users/hanijandali/Desktop/Code/MiroFish-Offline<br/>"
        "source venv/bin/activate<br/>"
        "cd backend<br/>"
        "python run.py", styles['CodeBlock']))
    story.append(Paragraph(
        "<b>Terminal 2 (Frontend):</b><br/>"
        "cd /Users/hanijandali/Desktop/Code/MiroFish-Offline/frontend<br/>"
        "npm run dev", styles['CodeBlock']))
    story.append(Paragraph("Open http://localhost:3000 in your browser.", styles['Body']))

    story.append(Paragraph("14.2 Stopping MiroFish", styles['SectionTitle']))
    story.append(Paragraph(
        "Ctrl+C in Terminal 1 (backend)<br/>"
        "Ctrl+C in Terminal 2 (frontend)<br/><br/>"
        "Ollama and Neo4j stay running in background (idle, no resource usage).", styles['CodeBlock']))

    story.append(Paragraph("14.3 Changing the LLM Model", styles['SectionTitle']))
    story.append(Paragraph(
        "1. Pull the model: ollama pull qwen2.5:14b<br/>"
        "2. Edit .env: LLM_MODEL_NAME=qwen2.5:14b<br/>"
        "3. Restart the backend (Ctrl+C then python run.py)", styles['CodeBlock']))

    story.append(Paragraph("14.4 Running Multiple Simulations", styles['SectionTitle']))
    story.append(Paragraph(
        "The graph and agent profiles are permanent. Each simulation run creates independent results. "
        "You can run 25 rounds today, 100 rounds tomorrow, and 200 rounds next week, all against "
        "the same project. Previous results are preserved.", styles['Body']))

    story.append(Paragraph("14.5 Checking GPU Usage", styles['SectionTitle']))
    story.append(Paragraph(
        "curl -s http://localhost:11434/api/ps | python3 -c \"<br/>"
        "import sys, json<br/>"
        "data = json.load(sys.stdin)<br/>"
        "for m in data.get('models', []):<br/>"
        "&nbsp;&nbsp;vram = m.get('size_vram', 0) / 1e9<br/>"
        "&nbsp;&nbsp;total = m.get('size', 0) / 1e9<br/>"
        "&nbsp;&nbsp;print(f'{m[chr(34)+chr(110)+chr(97)+chr(109)+chr(101)+chr(34)]}: {vram:.1f}/{total:.1f} GB on GPU')<br/>"
        "\"", styles['CodeBlock']))
    story.append(Paragraph(
        "If size_vram matches size, the model is 100% on GPU. If size_vram is 0, GPU acceleration "
        "is not working (check Ollama version and MLX library).", styles['Body']))

    story.append(Paragraph("14.6 Canceling a Running Simulation", styles['SectionTitle']))
    story.append(Paragraph(
        "<b>From UI:</b> Click the Stop button on the simulation page.<br/>"
        "<b>From API:</b> curl -X POST http://localhost:5001/api/simulation/stop "
        "-H 'Content-Type: application/json' -d '{\"simulation_id\":\"sim_xxx\"}'<br/>"
        "<b>Emergency:</b> Ctrl+C the backend (kills everything).<br/>"
        "<b>Kill stuck Ollama inference:</b> ollama stop qwen2.5:32b", styles['CodeBlock']))
    story.append(PageBreak())

    # ==================== CHAPTER 15 ====================
    story.append(Paragraph("Chapter 15: Troubleshooting Guide", styles['ChapterTitle']))

    story.append(make_table(
        ["Problem", "Cause", "Solution"],
        [
            ["500 error on ontology generation",
             "Model not pulled in Ollama",
             "Run: ollama pull [model-name]"],
            ["Timeout on graph build",
             "LLM/frontend timeout too short",
             "Increase timeout in llm_client.py and api/index.js"],
            ["'model not found' for embeddings",
             "nomic-embed-text not pulled",
             "Run: ollama pull nomic-embed-text"],
            ["CPU at 1000%+, GPU at 0%",
             "Broken MLX library in old Ollama",
             "Update Ollama to latest version from ollama.com"],
            ["Simulation killed unexpectedly",
             "Flask auto-reloader triggered by file edit",
             "Ensure use_reloader=False in run.py"],
            ["'status=paused' won't start",
             "Previous run left simulation in paused state",
             "Re-prepare the simulation via Step 2 UI"],
            ["Port 5001 already in use",
             "Previous backend instance still running",
             "Kill it: lsof -ti:5001 | xargs kill"],
            ["Neo4j auth failure",
             "Password mismatch between .env and Neo4j",
             "Change Neo4j password via browser at localhost:7474"],
            ["JSON parse errors during NER",
             "Using a reasoning model (qwen3, deepseek-r1)",
             "Switch to dense model: qwen2.5 family"],
            ["Graph memory updater error",
             "Storage not passed to start_simulation",
             "Fixed in simulation.py (passes neo4j_storage)"],
        ],
        col_widths=[130, 130, 210]
    ))
    story.append(Paragraph("Table 15.1: Common Issues and Solutions", styles['Caption']))
    story.append(PageBreak())

    # ==================== CHAPTER 16 ====================
    story.append(Paragraph("Chapter 16: GPU and Memory Management", styles['ChapterTitle']))

    story.append(Paragraph("16.1 Apple Silicon Unified Memory", styles['SectionTitle']))
    story.append(Paragraph(
        "Apple Silicon uses unified memory architecture. CPU and GPU share the same physical memory "
        "pool (128GB on your machine). There is no separate 'GPU memory' or 'VRAM'. When Ollama "
        "loads a model 'onto the GPU', it pins memory pages so they cannot be swapped, which macOS "
        "reports as 'wired memory' in Activity Monitor.", styles['Body']))

    story.append(Paragraph("16.2 Memory States in Activity Monitor", styles['SectionTitle']))
    story.append(make_table(
        ["Category", "What It Means", "MiroFish Context"],
        [
            ["Wired", "Pinned, cannot be swapped", "LLM model weights + KV caches on GPU"],
            ["App Memory", "Application heap allocations", "Ollama process overhead, Python, Node"],
            ["Compressed", "Inactive pages compressed in RAM", "Background apps, system caches"],
            ["Cached Files", "File system cache", "Recently read files, can be reclaimed"],
        ],
        col_widths=[90, 160, 220]
    ))
    story.append(Paragraph("Table 16.1: macOS Memory Categories", styles['Caption']))

    story.append(Paragraph("16.3 Model Auto-Unloading", styles['SectionTitle']))
    story.append(Paragraph(
        "Ollama automatically unloads models after 5 minutes of inactivity (OLLAMA_KEEP_ALIVE=5m). "
        "When unloaded, memory returns to the system. The model reloads automatically on the next "
        "request, taking 10-30 seconds for initial load. During active simulation, the model stays "
        "loaded continuously.", styles['Body']))

    story.append(Paragraph("16.4 Setting Ollama Environment Variables", styles['SectionTitle']))
    story.append(Paragraph(
        "Because Ollama runs as a macOS app (not command-line), environment variables must be set "
        "via launchctl so the app inherits them:", styles['Body']))
    story.append(Paragraph(
        "launchctl setenv OLLAMA_NUM_PARALLEL 2<br/>"
        "launchctl setenv OLLAMA_FLASH_ATTENTION 1<br/><br/>"
        "# Then quit and reopen Ollama app<br/>"
        "# Verify with:<br/>"
        "launchctl getenv OLLAMA_NUM_PARALLEL", styles['CodeBlock']))
    story.append(Paragraph(
        "Running 'OLLAMA_NUM_PARALLEL=8 ollama serve' from terminal does NOT use GPU acceleration "
        "because the command-line binary lacks the MLX integration that the macOS app provides. "
        "Always use the macOS app.",
        styles['Warning']))
    story.append(PageBreak())

    # ==================== APPENDIX A ====================
    story.append(Paragraph("Appendix A: Command Reference", styles['ChapterTitle']))
    story.append(make_table(
        ["Action", "Command"],
        [
            ["Start Neo4j", "brew services start neo4j"],
            ["Stop Neo4j", "brew services stop neo4j"],
            ["Check Neo4j status", "brew services list"],
            ["Start backend", "source venv/bin/activate && cd backend && python run.py"],
            ["Start frontend", "cd frontend && npm run dev"],
            ["Pull a model", "ollama pull qwen2.5:32b"],
            ["List models", "ollama list"],
            ["Check running models", "curl -s http://localhost:11434/api/ps"],
            ["Stop a model", "ollama stop qwen2.5:32b"],
            ["Check backend health", "curl http://localhost:5001/health"],
            ["Kill port 5001", "lsof -ti:5001 | xargs kill"],
            ["Kill port 3000", "lsof -ti:3000 | xargs kill"],
            ["Set Ollama parallel", "launchctl setenv OLLAMA_NUM_PARALLEL 2"],
            ["Set Flash Attention", "launchctl setenv OLLAMA_FLASH_ATTENTION 1"],
            ["Check GPU usage", "curl -s http://localhost:11434/api/ps | python3 -m json.tool"],
            ["Stop simulation (API)", "curl -X POST http://localhost:5001/api/simulation/stop -H 'Content-Type: application/json' -d '{...}'"],
        ],
        col_widths=[130, 340]
    ))
    story.append(Paragraph("Table A.1: Complete Command Reference", styles['Caption']))
    story.append(PageBreak())

    # ==================== APPENDIX B ====================
    story.append(Paragraph("Appendix B: File Structure", styles['ChapterTitle']))
    story.append(Paragraph(
        "MiroFish-Offline/<br/>"
        "|-- .env&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Configuration (model, Neo4j, etc.)<br/>"
        "|-- docker-compose.yml&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Docker config (optional, Neo4j only)<br/>"
        "|-- venv/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Python virtual environment<br/>"
        "|-- backend/<br/>"
        "|&nbsp;&nbsp;&nbsp;|-- run.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Entry point (python run.py)<br/>"
        "|&nbsp;&nbsp;&nbsp;|-- requirements.txt&nbsp;&nbsp;&nbsp;# Python dependencies<br/>"
        "|&nbsp;&nbsp;&nbsp;|-- uploads/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Uploaded docs + simulation data<br/>"
        "|&nbsp;&nbsp;&nbsp;|-- scripts/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Simulation runner scripts<br/>"
        "|&nbsp;&nbsp;&nbsp;|-- app/<br/>"
        "|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- __init__.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Flask app factory<br/>"
        "|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- config.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Configuration class<br/>"
        "|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- api/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# API blueprints (graph, simulation, report)<br/>"
        "|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- models/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Data models (Project, Task, Simulation)<br/>"
        "|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- services/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Business logic services<br/>"
        "|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- storage/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Neo4j, NER, Embedding implementations<br/>"
        "|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- utils/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# LLM client, file parser, logger<br/>"
        "|-- frontend/<br/>"
        "|&nbsp;&nbsp;&nbsp;|-- package.json<br/>"
        "|&nbsp;&nbsp;&nbsp;|-- src/<br/>"
        "|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- api/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Axios API client<br/>"
        "|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- views/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Vue page components<br/>"
        "|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- components/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Step components (Step1-Step5)<br/>",
        styles['CodeBlock']))
    story.append(PageBreak())

    # ==================== APPENDIX C ====================
    story.append(Paragraph("Appendix C: Model Comparison and Selection Guide", styles['ChapterTitle']))
    story.append(Paragraph(
        "Choosing the right model for MiroFish depends on your priorities: speed vs quality, "
        "testing vs production, small documents vs large corpora.", styles['Body']))

    story.append(Paragraph("C.1 Recommended Models", styles['SectionTitle']))
    story.append(make_table(
        ["Model", "Use Case", "Chunk Speed", "JSON Reliability", "Entity Quality"],
        [
            ["qwen2.5:72b", "Final production runs", "~45s", "Excellent", "Best available"],
            ["qwen2.5:32b", "Default recommendation", "~15s", "Excellent", "Very good"],
            ["qwen2.5:14b", "Fast testing/iteration", "~8s", "Very good", "Good"],
            ["qwen2.5:7b", "Quick prototyping", "~3s", "Good", "Acceptable"],
        ],
        col_widths=[90, 120, 70, 90, 100]
    ))
    story.append(Paragraph("Table C.1: Recommended Models", styles['Caption']))

    story.append(Paragraph("C.2 Models to AVOID", styles['SectionTitle']))
    story.append(make_table(
        ["Model Family", "Why to Avoid"],
        [
            ["qwen3 (all sizes)", "Reasoning model - outputs thinking tokens that break JSON parsing"],
            ["deepseek-r1 (all sizes)", "Reasoning model - same JSON parsing issue"],
            ["Any 'reasoning' or 'thinking' model", "Chain-of-thought tokens corrupt structured output"],
        ],
        col_widths=[150, 320]
    ))
    story.append(Paragraph("Table C.2: Models to Avoid", styles['Caption']))

    story.append(Paragraph("C.3 Parallel Slots by Model", styles['SectionTitle']))
    story.append(make_table(
        ["Model", "Weights", "Rec. Parallel Slots", "Total Memory", "Headroom (128GB)"],
        [
            ["qwen2.5:72b", "47 GB", "2", "~67 GB", "~61 GB free"],
            ["qwen2.5:32b", "20 GB", "2", "~40 GB", "~88 GB free"],
            ["qwen2.5:14b", "9 GB", "4", "~49 GB", "~79 GB free"],
            ["qwen2.5:7b", "5 GB", "4", "~25 GB", "~103 GB free"],
        ],
        col_widths=[90, 70, 100, 90, 120]
    ))
    story.append(Paragraph("Table C.3: Memory Planning Guide", styles['Caption']))

    story.append(S(1, 40))
    story.append(Paragraph("--- End of Document ---", styles['Subtitle']))

    # Build PDF
    doc.build(story)
    print(f"PDF generated: {output_path}")


if __name__ == "__main__":
    build_pdf()
