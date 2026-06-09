# data.py
# All roadmap content for the Purple Team & Agentic AI Roadmap.
# Structured as a list of phase dictionaries.
# Author: KyberPhantasma

PHASES = [
    {
        "id": "p0",
        "number": "00",
        "title": "Environment Setup",
        "duration": "Week 1",
        "summary": (
            "Before anything else, you need a proper working environment. "
            "This phase is non-negotiable. Everything else depends on it."
        ),
        "sections": [
            {
                "title": "Operating System",
                "type": "text",
                "content": (
                    "Install Kali Linux as your primary OS or dual-boot alongside "
                    "your existing system. If neither is possible, install it on "
                    "VirtualBox (free) or use WSL2 with Kali on Windows. "
                    "Choose whichever option gives you a full Linux terminal."
                ),
            },
            {
                "title": "Essential Software to Install",
                "type": "list",
                "items": [
                    "Terminator — terminal emulator with screen splitting",
                    "git — version control (pre-installed on Kali)",
                    "Python 3 — pre-installed on Kali",
                    "pip — Python package manager",
                    "Vim or nano — terminal text editor",
                    "Docker — optional but useful later",
                    "Ollama — local LLM runner",
                    "Goose — agentic terminal AI",
                    "Void IDE or VS Code with Continue.dev extension",
                ],
            },
            {
                "title": "Create Your Workspace",
                "type": "code",
                "content": (
                    "mkdir -p ~/projects/{scripts,notes,labs,portfolio}\n"
                    "cd ~/projects\n"
                    "git init"
                ),
            },
            {
                "title": "GitHub Setup",
                "type": "list",
                "items": [
                    "Create a GitHub account at github.com",
                    "Create a repository named: cybersecurity-portfolio",
                    "Push an initial README describing your goals",
                ],
            },
            {
                "title": "Medium Setup",
                "type": "list",
                "items": [
                    "Create a free Medium account",
                    "Write a Day 0 post: your setup, your goals, your roadmap",
                ],
            },
        ],
        "weekly_breakdown": [],
        "deliverables": [
            "Kali Linux installed and running",
            "All essential tools installed and tested",
            "GitHub repo: cybersecurity-portfolio created with README",
            "Day 0 Medium post published",
        ],
        "resources": [],
        "background_threads": [],
    },
    {
        "id": "p1",
        "number": "01",
        "title": "The Foundations",
        "duration": "Months 1 – 3",
        "summary": (
            "Goal: Move confidently in a Linux environment, understand networking "
            "at the packet level, and exploit every common web vulnerability."
        ),
        "sections": [
            {
                "title": "Month 1 Overview — Linux & Networking",
                "type": "text",
                "content": (
                    "This month builds your Linux and networking fundamentals — "
                    "the bedrock of everything that follows. You will complete "
                    "OverTheWire Bandit, study two essential books, and begin "
                    "packet-level network analysis."
                ),
            },
            {
                "title": "Month 2 Overview — Web Vulnerabilities & Recon",
                "type": "text",
                "content": (
                    "Begin PortSwigger Web Security Academy with HTTP fundamentals, "
                    "SQL Injection, XSS, CSRF, Broken Access Control, and Path "
                    "Traversal. In parallel, set up your recon tool stack and "
                    "make your first contact with AI-assisted workflows."
                ),
            },
            {
                "title": "Month 3 Overview — Deep Bug Class & OSINT",
                "type": "text",
                "content": (
                    "Choose one vulnerability class and master it completely at "
                    "Practitioner level. Begin OSINT study. Write and publish "
                    "your first automated recon pipeline script."
                ),
            },
        ],
        "weekly_breakdown": [
            {"period": "Week 1",  "focus": "Linux Mastery",
             "action": "Complete OverTheWire Bandit levels 0-15. Write a Markdown solution file for each level and push to GitHub."},
            {"period": "Week 2",  "focus": "Linux Deep Dive",
             "action": "Read Linux Basics for Hackers. Do every exercise. Continue Bandit 16-34. Write 2-3 Medium walkthroughs."},
            {"period": "Week 3",  "focus": "Networking Fundamentals",
             "action": "Complete TryHackMe free 'Intro to Networking' and 'Nmap' rooms. Install Wireshark and analyse your own traffic."},
            {"period": "Week 4",  "focus": "Network Hacking Basics",
             "action": "Read Network Basics for Hackers. Practice with tcpdump, nmap, netcat. Write blog: How I Learned to Love the Packet."},
            {"period": "Week 5-6", "focus": "HTTP & SQL Injection",
             "action": "Start PortSwigger Web Security Academy. Complete all Apprentice labs for HTTP Fundamentals and SQL Injection."},
            {"period": "Week 7",  "focus": "XSS & CSRF",
             "action": "Complete Apprentice labs for XSS and CSRF. Write a Medium post on reflected vs stored vs DOM-based XSS."},
            {"period": "Week 8",  "focus": "Access Control & Path Traversal",
             "action": "Complete Apprentice labs for Broken Access Control and Path Traversal on PortSwigger."},
            {"period": "Week 9-10", "focus": "Deep Bug Class Mastery",
             "action": "Choose XSS, IDOR, or SQLi. Complete ALL Practitioner labs for that class. Read matching chapters in Real-World Bug Hunting."},
            {"period": "Week 11", "focus": "OSINT & Target Selection",
             "action": "Read OSINT Techniques (Bazzell) Chapters 1-7. Learn Google dorking, certificate transparency, Shodan basics."},
            {"period": "Week 12", "focus": "Recon Pipeline Automation",
             "action": "Write a Bash/Python script chaining subfinder, httpx, and nuclei. Push to GitHub. Write Medium article on your pipeline."},
        ],
        "deliverables": [
            "GitHub repo with Bandit write-ups (all levels)",
            "Medium blog with 2+ detailed Bandit walkthroughs",
            "Python port scanner script pushed to GitHub",
            "Port scanner improved with banner grabbing and threading",
            "Custom Nuclei template for a simple misconfiguration",
            "Medium article: My First SQL Injection in the Lab",
            "Automated recon pipeline script (subfinder + httpx + nuclei)",
            "Medium article on your automated recon pipeline",
            "Second custom Nuclei template",
        ],
        "resources": [
            "OverTheWire Bandit — overthewire.org/wargames/bandit",
            "Linux Basics for Hackers — OccupyTheWeb",
            "Network Basics for Hackers — OccupyTheWeb",
            "TryHackMe — tryhackme.com (free tier)",
            "PortSwigger Web Security Academy — portswigger.net/web-security",
            "Wiz Bug Bounty Masterclass — YouTube (free)",
            "OSINT Techniques — Michael Bazzell",
            "Python Crash Course 3rd Ed.",
            "Eloquent JavaScript — eloquentjavascript.net (free)",
            "CS50x — cs50.harvard.edu (free)",
            "The Web Application Hacker's Handbook",
        ],
        "background_threads": [
            "Python: Read Python Crash Course daily (30 min/day). Push all scripts to GitHub.",
            "JavaScript: Read Eloquent JavaScript Chapters 1-6. Understand DOM basics and async.",
            "CS50x: Watch one lecture per week. Do not rush.",
            "Book of Proof (Chapters 1-3): 30 min, 2-3 times a week.",
        ],
    },
    {
        "id": "p2",
        "number": "02",
        "title": "Web2 Hunter & AI Assistant",
        "duration": "Months 4 – 6",
        "summary": (
            "Goal: Hunt on real bug bounty programs, submit reports, "
            "and use AI to accelerate every part of your workflow."
        ),
        "sections": [
            {
                "title": "Month 4 Overview — AI-Driven Bug Hunting",
                "type": "text",
                "content": (
                    "Set up your full AI-assisted security workflow with Goose, "
                    "Void IDE, and Ollama. Apply your first vulnerability to real "
                    "programs on HackerOne and Bugcrowd. Use AI for payload "
                    "generation, recon, and report drafting."
                ),
            },
            {
                "title": "Month 5-6 Overview — Expansion & Reporting",
                "type": "text",
                "content": (
                    "Deepen your second bug class to Practitioner level. Submit "
                    "reports and study every rejection. Apply advanced OSINT to "
                    "find hidden assets. Target your first valid, accepted report. "
                    "Begin Cryptography I and Mastering Ethereum in the background."
                ),
            },
        ],
        "weekly_breakdown": [
            {"period": "Week 13", "focus": "AI Workflow Setup",
             "action": "Install Goose and Void IDE. Connect to local Ollama models. Set up deepseek-coder-v2:16b for coding tasks."},
            {"period": "Week 14", "focus": "AI for Recon & Analysis",
             "action": "Use AI to generate wordlists, deobfuscate JavaScript, brainstorm attack vectors. Practice on PortSwigger labs first."},
            {"period": "Week 15-16", "focus": "First Real Programs",
             "action": "Create accounts on HackerOne and Bugcrowd. Pick 2-3 low-competition programs. Apply your mastered vulnerability."},
            {"period": "Week 17-18", "focus": "Deepen Second Bug Class",
             "action": "Finish all Practitioner labs for your second vulnerability class on PortSwigger."},
            {"period": "Week 19-20", "focus": "Reporting & Iteration",
             "action": "Submit reports, study all feedback, iterate. For every rejection, understand exactly why."},
            {"period": "Week 21-24", "focus": "Advanced OSINT & More Hunting",
             "action": "Apply OSINT to find hidden assets. Continue hunting. Aim for your first valid accepted report."},
        ],
        "deliverables": [
            "GitHub repo: my-bug-bounty-automation with AI-assisted scripts",
            "Medium article: How I Use AI in My Bug Bounty Workflow",
            "At least 2 bug reports submitted (even if duplicates)",
            "First valid, accepted bug bounty report",
            "Python script automating a specific recon or analysis task",
            "Completed Cryptography I course (Dan Boneh)",
        ],
        "resources": [
            "HackerOne — hackerone.com",
            "Bugcrowd — bugcrowd.com",
            "Ollama — ollama.ai (local LLM runner)",
            "Goose — agentic terminal AI",
            "Void IDE / VS Code + Continue.dev extension",
            "PortSwigger Web Security Academy — portswigger.net",
            "Real-World Bug Hunting — Peter Yaworski",
            "Book of Proof — free PDF online",
            "Cryptography I — Dan Boneh (Coursera, free audit)",
            "Mastering Ethereum — free PDF on GitHub",
        ],
        "background_threads": [
            "Math & Logic: Finish Book of Proof Chapters 4-6.",
            "Cryptography: Start Dan Boneh Cryptography I on Coursera (free audit). Do Python assignments.",
            "Ethereum Reading: Begin Mastering Ethereum Chapters 1-6.",
        ],
    },
    {
        "id": "p3",
        "number": "03",
        "title": "Web3 & Smart Contract Security",
        "duration": "Months 7 – 10",
        "summary": (
            "Goal: Become a competent smart contract auditor "
            "and start competing on live audit platforms."
        ),
        "sections": [
            {
                "title": "Month 7 — Solidity & EVM Foundations",
                "type": "text",
                "content": (
                    "Complete all CryptoZombies lessons. Read Mastering Ethereum "
                    "Chapters 7-9 on smart contracts. Write a simple ERC-20 token "
                    "using Foundry. Study Solidity docs and Solidity by Example in parallel."
                ),
            },
            {
                "title": "Month 8 — Gamified Hacking",
                "type": "text",
                "content": (
                    "Complete all Ethernaut levels and write detailed Medium walkthroughs "
                    "for each. Then complete all Capture the Ether challenges. "
                    "These platforms teach real exploit patterns through hands-on puzzles."
                ),
            },
            {
                "title": "Month 9 — DeFi Attack Patterns",
                "type": "text",
                "content": (
                    "Solve every Damn Vulnerable DeFi challenge. Understand flash loans, "
                    "oracle manipulation, governance attacks, and reentrancy. Study the "
                    "Secureum Epoch 0 mind map and SWC Registry. Read one Rekt.news "
                    "article daily to study real-world DeFi exploits."
                ),
            },
            {
                "title": "Month 10 — Professional Auditing",
                "type": "text",
                "content": (
                    "Complete the full Cyfrin Updraft Smart Contract Security course. "
                    "Do all mock audits. Learn Slither (static analysis), Echidna "
                    "(fuzzing), and Foundry fuzzing. Earn your Cyfrin certification."
                ),
            },
        ],
        "weekly_breakdown": [
            {"period": "Month 7", "focus": "Solidity & EVM",
             "action": "Complete ALL CryptoZombies. Read Mastering Ethereum Ch 7-9. Write an ERC-20 token in Foundry."},
            {"period": "Month 8 W1-2", "focus": "Ethernaut",
             "action": "Complete all Ethernaut levels. Write a detailed Medium walkthrough for each level."},
            {"period": "Month 8 W3-4", "focus": "Capture the Ether",
             "action": "Complete all Capture the Ether challenges. Document solutions on GitHub."},
            {"period": "Month 9", "focus": "Damn Vulnerable DeFi",
             "action": "Solve every challenge. Understand flash loans, oracles, governance, and reentrancy in depth."},
            {"period": "Month 10", "focus": "Cyfrin Updraft",
             "action": "Complete the full Smart Contract Security course. Do all mock audits. Learn Slither, Echidna, Foundry fuzzing."},
        ],
        "deliverables": [
            "GitHub repo with CryptoZombies code and custom ERC-20 token",
            "Medium series: Ethernaut Walkthroughs (one post per level)",
            "GitHub repo with all Ethernaut solutions",
            "All Damn Vulnerable DeFi solutions on GitHub",
            "Cyfrin Updraft certification earned",
            "Medium post: What I Learned in Cyfrin Updraft",
        ],
        "resources": [
            "CryptoZombies — cryptozombies.io (free)",
            "Mastering Ethereum — free PDF on GitHub",
            "Foundry — book.getfoundry.sh (free)",
            "Solidity by Example — solidity-by-example.org (free)",
            "Ethernaut — ethernaut.openzeppelin.com (free)",
            "Capture the Ether — capturetheether.com (free)",
            "Damn Vulnerable DeFi — damnvulnerabledefi.xyz (free)",
            "Secureum Epoch 0 mind map",
            "SWC Registry — swcregistry.io",
            "Rekt.news — daily DeFi exploit reading",
            "Cyfrin Updraft — updraft.cyfrin.io (free)",
            "Cyfrin Discord community",
        ],
        "background_threads": [
            "Read Solidity documentation in parallel with CryptoZombies.",
            "Read one Rekt.news article daily throughout this phase.",
            "Study Secureum Epoch 0 mind map as a reference throughout.",
        ],
    },
    {
        "id": "p4",
        "number": "04",
        "title": "Purple Team & Agentic AI",
        "duration": "Month 11+",
        "summary": (
            "Goal: Build AI agents for security research, compete in audit "
            "contests, and position yourself for remote work in the field."
        ),
        "sections": [
            {
                "title": "Month 11-12 — AI Agent Development",
                "type": "list",
                "items": [
                    "Learn LangChain and CrewAI using free tutorials. Build a simple agent that runs Slither analysis and summarises the results.",
                    "Integrate tools: connect your agents to Ollama and ProjectDiscovery tools (subfinder, httpx, nuclei).",
                    "Build a report-writing agent that takes raw security notes and outputs a formatted, professional audit report.",
                ],
            },
            {
                "title": "Month 13+ — Competitive Auditing",
                "type": "list",
                "items": [
                    "Code4rena / Cantina / Sherlock: Join contests regularly. Start with lower-stakes contests to build your on-chain reputation.",
                    "Immunefi: Begin hunting on live Web3 bug bounty programs.",
                    "Apply for remote roles: Junior Security Researcher, Pentester, Smart Contract Auditor. Use your public GitHub work as proof.",
                ],
            },
            {
                "title": "Ongoing Practices",
                "type": "list",
                "items": [
                    "Keep building AI agents that automate parts of your offensive workflow.",
                    "Continue learning: Trail of Bits blog, Noxx EVM deep dives.",
                    "Mentor others and contribute to open source security projects.",
                ],
            },
        ],
        "weekly_breakdown": [
            {"period": "Month 11-12", "focus": "AI Agent Development",
             "action": "Learn LangChain and CrewAI. Build a Slither analysis agent. Build a report-writing agent."},
            {"period": "Month 13+", "focus": "Competitive Auditing",
             "action": "Join Code4rena, Sherlock, or Cantina contests. Begin Immunefi hunting. Update LinkedIn and apply for remote roles."},
            {"period": "Ongoing", "focus": "Growth & Community",
             "action": "Build more AI agents, read Trail of Bits blog and Noxx EVM, mentor others, contribute to open source."},
        ],
        "deliverables": [
            "AI agent that runs Slither and summarises findings",
            "Report-writing agent (raw notes to formatted report)",
            "First Code4rena / Sherlock / Cantina contest submission",
            "First Immunefi live bounty report",
            "Updated LinkedIn with full portfolio and work samples",
            "First remote security job application submitted",
        ],
        "resources": [
            "LangChain documentation — python.langchain.com (free)",
            "CrewAI documentation — crewai.com (free)",
            "Code4rena — code4rena.com",
            "Sherlock — sherlock.xyz",
            "Cantina — cantina.xyz",
            "Immunefi — immunefi.com",
            "Tra
