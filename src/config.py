# ================================
# Skill vocabulary for text matching
# Derived from analysis of public job datasets
# ================================


soft_skills = ["communication","analytical","leadership","initiative","presentation","flexible","collaboration",
               "organizational","work independently","interpersonal","teamwork","time management","critical thinking",
               "problem solving","detail oriented","adaptability","customer focused","multitasking","self motivated"]

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
    "excel": ["excel", "spreadsheet"],
    "powerpoint": ["powerpoint", "powerpoints"],
    "word": ["word"],
    "outlook": ["outlook"],
    "sharepoint": ["sharepoint"],
    "jira": ["jira"],
    "atlassian": ["atlassian"],
    "visio": ["visio"],

}


# ================================
# Entry-level terms for text matching:
# - Title column (include + exclude terms)
# - Description column
# ================================

title_pattern = r"(?:entry|entry level|junior|jr|associate|level i|level 1|trainee|apprentice)"
desc_pattern  = r"(?:0-1|0-2|1-2|recent graduate|new grad|entry level|graduate program|early career)"
exclude_pattern = r"(?:senior|sr|lead|principal|manager|director|architect|5\+|7\+|10\+|3\+)"
