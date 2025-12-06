# ================================
# Skill vocabulary for text matching
# Derived from analysis of public job datasets
# ================================


soft_skills = ["communication","analytical","leadership","initiative","presentation","flexible","collaboration",
               "organizational","work independently","interpersonal","teamwork","time management","critical thinking",
               "problem solving","detail oriented","adaptability","customer focused","multitasking","self motivated"]

technical_skills = ["sql","excel","python","statistics","tableau","power bi","r","machine learning","java","etl","sas","aws",
                     "azure","gcp","snowflake","databricks","redshift","bigquery","spark","hadoop","docker","kubernetes",
                     "mysql","postgres","git","linux","unix",".net","react","node","javascript","api","rest","graphql",
                     "tensorflow","pytorch","scikit","scikit-learn","numpy","pandas","matlab","c++","c#"]

# ================================
# Entry-level terms for text matching:
# - Title column (include + exclude terms)
# - Description column
# ================================

title_pattern = r"(?:entry|entry level|junior|jr|associate|level i|level 1|trainee|apprentice)"
desc_pattern  = r"(?:0-1|0-2|1-2|recent graduate|new grad|entry level|graduate program|early career)"
exclude_pattern = r"(?:senior|sr|lead|principal|manager|director|architect|5\+|7\+|10\+|3\+)"
