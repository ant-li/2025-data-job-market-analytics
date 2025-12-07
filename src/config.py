# ================================
# Skill vocabulary for text matching
# Derived from analysis of public job datasets
# ================================


# soft_skills = ["communication","analytical","leadership","initiative","presentation","flexible","collaboration",
#                "organizational","work independently","interpersonal","teamwork","time management","critical thinking",
#                "problem solving","detail oriented","adaptability","customer focused","multitasking","self motivated", "research",
               # ]

SOFT_SKILL_ALIASES = {
    # --- communication ---
    "communication skills": "communication",
    "strong communication skills": "communication",
    "excellent communication skills": "communication",
    "outstanding communication skills": "communication",
    "effective communication": "communication",
    "communicate effectively": "communication",
    "able to communicate effectively": "communication",
    "clear communication": "communication",
    "verbal and written communication": "communication",
    "written and verbal communication": "communication",
    "oral and written communication": "communication",
    "written communication": "communication",
    "verbal communication": "communication",
    "oral communication": "communication",
    "presentation and communication skills": "communication",

    # --- collaboration / teamwork ---
    "collaboration": "collaboration",
    "collaborative mindset": "collaboration",
    "collaborative environment": "collaboration",
    "cross-functional collaboration": "collaboration",
    "work collaboratively": "collaboration",
    "collaborate with": "collaboration",

    "team player": "teamwork",
    "strong team player": "teamwork",
    "team-oriented": "teamwork",
    "work well in a team": "teamwork",
    "work well within a team": "teamwork",
    "working in a team environment": "teamwork",
    "cross-functional teams": "teamwork",
    "cross functional team": "teamwork",

    # --- leadership / people management ---
    "leadership skills": "leadership",
    "strong leadership": "leadership",
    "demonstrated leadership": "leadership",
    "proven leadership": "leadership",
    "people leadership": "leadership",
    "team leadership": "leadership",
    "lead teams": "leadership",
    "lead a team": "leadership",
    "leading a team": "leadership",
    "servant leadership": "leadership",

    "manage a team": "leadership",
    "managing a team": "leadership",
    "people management": "leadership",
    "line management": "leadership",

    # --- problem solving / analytical / critical thinking ---
    "problem solving": "problem solving",
    "problem-solving": "problem solving",
    "solve complex problems": "problem solving",
    "solve problems": "problem solving",
    "ability to solve problems": "problem solving",
    "issue resolution": "problem solving",
    "root cause analysis": "problem solving",

    "analytical mindset": "analytical thinking",
    "analytical thinking": "analytical thinking",
    "strong analytical skills": "analytical thinking",
    "strong analytical ability": "analytical thinking",
    "data-driven decision making": "analytical thinking",

    "critical thinking": "critical thinking",
    "think critically": "critical thinking",

    # --- adaptability / ambiguity / flexibility ---
    "adaptability": "adaptability",
    "adaptable": "adaptability",
    "highly adaptable": "adaptability",
    "flexible and adaptable": "adaptability",

    "comfort with ambiguity": "adaptability",
    "handle ambiguity": "adaptability",
    "dealing with ambiguity": "adaptability",
    "work in a fast-paced environment": "adaptability",
    "fast paced environment": "adaptability",
    "dynamic environment": "adaptability",

    "flexible work style": "adaptability",
    "flexibility": "adaptability",

    # --- time & priority management ---
    "time management": "time management",
    "strong time management": "time management",
    "manage time effectively": "time management",
    "ability to prioritize": "time management",
    "prioritize tasks": "time management",
    "prioritize work": "time management",
    "manage multiple priorities": "time management",
    "manage competing priorities": "time management",
    "multitasking": "time management",
    "multi-tasking": "time management",

    # --- attention to detail ---
    "attention to detail": "attention to detail",
    "strong attention to detail": "attention to detail",
    "high attention to detail": "attention to detail",
    "detail oriented": "attention to detail",
    "detail-oriented": "attention to detail",
    "meticulous": "attention to detail",
    "thoroughness": "attention to detail",

    # --- project / program management ---
    "project management": "project management",
    "manage projects": "project management",
    "managing projects": "project management",
    "end-to-end project delivery": "project management",
    "delivery of projects": "project management",

    "program management": "program management",
    "manage programs": "program management",
    "managing programs": "program management",

    # --- stakeholder management / communication ---
    "stakeholder management": "stakeholder management",
    "manage stakeholders": "stakeholder management",
    "managing stakeholders": "stakeholder management",
    "senior stakeholder management": "stakeholder management",
    "executive stakeholder management": "stakeholder management",

    "stakeholder communication": "stakeholder communication",
    "communicate with stakeholders": "stakeholder communication",
    "senior stakeholder communication": "stakeholder communication",
    "executive communication": "stakeholder communication",

    # --- customer focus ---
    "customer focus": "customer focus",
    "customer-centric": "customer focus",
    "customer centric": "customer focus",
    "customer obsession": "customer focus",
    "client focus": "customer focus",
    "client-facing": "customer focus",
    "client facing": "customer focus",
    "work with clients": "customer focus",
    "manage client relationships": "customer focus",
    "client relationship management": "customer focus",

    # --- business acumen ---
    "business acumen": "business acumen",
    "strong business acumen": "business acumen",
    "commercial awareness": "business acumen",
    "commercial acumen": "business acumen",
    "understanding of the business": "business acumen",

    # --- decision making / ownership / initiative / self-motivation ---
    "decision making": "decision making",
    "sound decision making": "decision making",
    "make data-driven decisions": "decision making",
    "make informed decisions": "decision making",

    "ownership": "ownership",
    "sense of ownership": "ownership",
    "end-to-end ownership": "ownership",
    "take ownership": "ownership",
    "bias for action": "ownership",
    "accountability": "ownership",

    "self starter": "initiative",
    "self-starter": "initiative",
    "proactive": "initiative",
    "proactive mindset": "initiative",
    "take initiative": "initiative",
    "show initiative": "initiative",

    "self-motivated": "self-motivation",
    "highly motivated": "self-motivation",
    "strong drive": "self-motivation",

    # --- learning agility ---
    "learning agility": "learning agility",
    "eager to learn": "learning agility",
    "willingness to learn": "learning agility",
    "continuous learner": "learning agility",
    "continuous learning": "learning agility",
    "growth mindset": "learning agility",

    # --- emotional intelligence / conflict / negotiation ---
    "emotional intelligence": "emotional intelligence",
    "empathy": "emotional intelligence",
    "empathetic": "emotional intelligence",
    "build trust": "emotional intelligence",

    "conflict resolution": "conflict resolution",
    "resolve conflicts": "conflict resolution",
    "mediation": "conflict resolution",
    "diplomacy": "conflict resolution",
    "handle difficult conversations": "conflict resolution",

    "negotiation": "negotiation",
    "negotiation skills": "negotiation",
    "negotiate with stakeholders": "negotiation",

    # --- presentation / public speaking / storytelling ---
    "presentation skills": "presentation skills",
    "strong presentation skills": "presentation skills",
    "present to stakeholders": "presentation skills",
    "present to executives": "presentation skills",

    "public speaking": "public speaking",
    "speak in public": "public speaking",

    "storytelling": "storytelling",
    "data storytelling": "storytelling",
    "tell a compelling story": "storytelling",

    # --- mentoring / coaching / relationship / networking ---
    "mentoring": "mentoring",
    "mentor others": "mentoring",
    "mentor junior": "mentoring",

    "coaching": "coaching",
    "coach others": "coaching",

    "relationship building": "relationship building",
    "build relationships": "relationship building",
    "relationship management": "relationship building",
    "manage relationships": "relationship building",

    "networking": "networking",
    "build a network": "networking",

    # --- resilience / stress management / work ethic ---
    "resilience": "resilience",
    "resilient": "resilience",

    "stress management": "stress management",
    "work well under pressure": "stress management",
    "perform under pressure": "stress management",
    "handle pressure": "stress management",

    "strong work ethic": "work ethic",
    "work ethic": "work ethic",
    "highly accountable": "work ethic",

    # --- process / continuous improvement ---
    "process improvement": "process improvement",
    "improve processes": "process improvement",
    "process optimization": "process improvement",

    "continuous improvement": "continuous improvement",
    "drive continuous improvement": "continuous improvement",

    # --- strategic / systems thinking ---
    "strategic thinking": "strategic thinking",
    "think strategically": "strategic thinking",
    "strategic mindset": "strategic thinking",

    "systems thinking": "systems thinking",
    "holistic thinking": "systems thinking",
}

# technical_skills = [
# "sql","excel","python","statistics","tableau","power bi","r","machine learning","java","etl","sas",
# "aws","azure","gcp","snowflake","databricks","redshift","bigquery","spark","hadoop","docker","kubernetes",
# "mysql","postgres","mongodb","mssql","redis","nosql",
# "git","gitlab","bitbucket","linux","unix","bash","shell","powershell","terminal",
# ".net","asp.net","react","node","node.js","javascript","typescript","api","rest","graphql",
# "tensorflow","pytorch","keras","scikit","scikit-learn","numpy","pandas","matplotlib","nltk","seaborn","pyspark",
# "matlab","c++","c#","c/c++","cobol","fortran","go","groovy","julia","perl","php","ruby","rust","scala","swift","dart","assembly",
# "alteryx","cognos","crystal","dax","looker","microstrategy","qlik","rshiny","spss","spreadsheet","ssis","ssrs",
# "jira","atlassian","sharepoint","outlook","visio","word","powerpoint",
# "airflow","aurora","selenium","splunk","twilio",
# "gdpr"
# ]

TECHNICAL_SKILL_ALIASES = {

    # ======================
    # Core Languages
    # ======================
    "python": ["python"],
    "r": ["r", "r language", "r programming"],
    "java": ["java"],
    "scala": ["scala"],
    "javascript": ["javascript", "js"],
    "typescript": ["typescript"],
    "go": ["go", "golang"],
    "ruby": ["ruby"],
    "php": ["php"],
    "perl": ["perl"],
    "julia": ["julia"],
    "dart": ["dart"],
    "swift": ["swift"],
    "c++": ["c++", "c/c++"],
    "c#": ["c#"],
    "visual basic": ["visual basic", "vb.net", "vba"],
    "css": ["css"],

    # ======================
    # Data / SQL / Databases
    # ======================
    "sql": ["sql", "t-sql", "pl/sql"],
    "postgres": ["postgres", "postgresql"],
    "mysql": ["mysql"],
    "mongodb": ["mongodb", "mongo"],
    "mssql": ["mssql"],
    "nosql": ["nosql", "no-sql"],
    "redis": ["redis"],
    "snowflake": ["snowflake"],
    "redshift": ["redshift"],
    "bigquery": ["bigquery"],
    "databricks": ["databricks"],
    "sas": ["sas"],

    # ======================
    # Big Data / Processing
    # ======================
    "spark": ["spark"],
    "hadoop": ["hadoop"],
    "pyspark": ["pyspark"],

    # ======================
    # Python / ML Libraries
    # ======================
    "numpy": ["numpy"],
    "pandas": ["pandas"],
    "matplotlib": ["matplotlib"],
    "seaborn": ["seaborn"],
    "scikit-learn": ["scikit-learn", "sklearn"],
    "tensorflow": ["tensorflow"],
    "pytorch": ["pytorch"],
    "keras": ["keras"],

    # ======================
    # BI / Visualization
    # ======================
    "tableau": ["tableau"],
    "power bi": ["power bi", "powerbi", "power_bi"],
    "qlik": ["qlik"],
    "looker": ["looker"],
    "microstrategy": ["microstrategy"],
    "cognos": ["cognos"],
    "spss": ["spss"],
    "rshiny": ["rshiny"],
    "dax": ["dax"],
    "alteryx" : ["alteryx"],

    # ======================
    # Cloud Platforms
    # ======================
    "aws": ["aws"],
    "azure": ["azure"],
    "gcp": ["gcp"],
    "airflow": ["airflow"],
    "aurora": ["aurora"],
    "sagemaker": ["sagemaker"],

    # ======================
    # DevOps / OS / Tools
    # ======================
    "git": ["git"],
    "gitlab": ["gitlab"],
    "github": ["github"],
    "bitbucket": ["bitbucket"],
    "linux": ["linux"],
    "unix": ["unix", "linux/unix", "unix/linux"],
    "bash": ["bash"],
    "shell": ["shell"],
    "powershell": ["powershell"],
    "terminal": ["terminal"],
    "docker": ["docker"],
    "kubernetes": ["kubernetes"],
    "selenium": ["selenium"],
    "splunk": ["splunk"],

    # ======================
    # Enterprise / Office
    # ======================
    "excel": ["excel", "spreadsheet", "google sheets", "google sheet"],
    "powerpoint": ["powerpoint", "powerpoints"],
    "word": ["word"],
    "outlook": ["outlook"],
    "sharepoint": ["sharepoint"],
    "jira": ["jira"],
    "atlassian": ["atlassian"],
    "visio": ["visio"],
    "sap": ["sap"],

    "REST API": ["REST API"],
    "generative ai": [
    "gen ai",
    "genai",
    "generative ai",
    "generative artificial intelligence",
    "gpt",
    "llm",
    "large language model",
    "large language models"
],
    "data mining": ["data mining", "mining"],
    
}


# ================================
# Entry-level terms for text matching:
# - Title column (include + exclude terms)
# - Description column
# ================================

# title_pattern = r"(?:entry|entry level|junior|jr|associate|level i|level 1|trainee|apprentice)"
# desc_pattern  = r"(?:0-1|0-2|1-2|recent graduate|new grad|entry level|graduate program|early career)"
# exclude_pattern = r"(?:senior|sr|lead|principal|manager|director|architect|5\+|7\+|10\+|3\+)"
title_pattern = (
    r"\b("
    r"entry[- ]?level|"
    r"junior|jr\.?|"
    r"new grad(?:uate)?|recent graduate|early career|"
    r"graduate (analyst|engineer|scientist|developer|data scientist)|"
    r"(data|business|analytics|machine learning|software)\s+intern(?:ship)?|"
    r"intern\b|trainee\b|co[- ]?op|"
    r"level\s*[01]\b|"
    r"associate\b"
    r")\b"
)

desc_pattern = (
    r"\b("
    r"entry[- ]?level|"
    r"junior role|junior position|"
    r"new grad(?:uate)?|recent graduate|early career|"
    r"intern(?:ship)?|trainee\b|co[- ]?op|"
    r"0[-–]2 years|0[-–]1 years|1[-–]2 years|"
    r"less than 2 years|"
    r"no (prior )?experience (required|necessary)"
    r")\b"
)

# Patterns to exclude clearly senior roles
exclude_pattern = (
    r"\b("
    r"senior|sr\.|staff|principal|lead\b|"
    r"manager|management|director|head of|vp|vice president|"
    r"iii\b|iv\b|v\b"
    r")\b"
)
