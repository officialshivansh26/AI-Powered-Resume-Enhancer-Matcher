system_prompt_matching = """
Scoring Guide:
It's ok to say candidate does not match the requirement.
Degree Section: Prioritize major than degree level. Candidate with degrees more directly relevant to the required degree should receive higher score, even if their degree level is lower.
Experience Section: Candidate with more relevant experience field get higher score.
Technical Skills Section: Candidate with more relevant technical skills get higher score.
Responsibilities Section: Candidate with more relevant responsibilities get higher score.
Certificates Section: Candidate with required certificates get higher score. Candidate without required certificates get no score. Candidate with related certificates to the position get medium score.
Soft Skills Section: Prioritize foreign language and leadership skills. Candidate with more relevant soft skills get higher score.
All comments should use singular pronouns such as "he", "she", "the candidate", or the candidate's name.
In addition to the score and comment, give one practical suggestion for how the candidate can improve their resume or skills in each category. Suggestions should be actionable and tailored to the job requirements.
"""

fn_matching_analysis = [
    {
        "name": "evaluate",
        "description": "For each requirement, score in 0 - 100 scale if the candidate matches with the requirement or not.",
        "parameters": {
            "type": "object",
            "properties": {
                "degree": {
                    "type": "object",
                    "properties": {
                        "score": {
                            "type": "integer",
                            "minimum": 0,
                            "maximum": 100,
                        },
                        "comment": {
                            "type": "string",
                        },
                        "suggestion": {
                            "type": "string",
                            "description": "What the candidate can improve or add in the resume to increase the score for degree."
                        },
                    },
                    "required": ["score", "comment", "suggestion"],
                },
                "experience": {
                    "type": "object",
                    "properties": {
                        "score": {"type": "integer", "minimum": 0, "maximum": 100},
                        "comment": {"type": "string"},
                        "suggestion": {
                            "type": "string",
                            "description": "How the candidate can enhance or tailor their experience section to match the job better."
                        },
                    },
                    "required": ["score", "comment", "suggestion"],
                },
                "technical_skill": {
                    "type": "object",
                    "properties": {
                        "score": {"type": "integer", "minimum": 0, "maximum": 100},
                        "comment": {"type": "string"},
                        "suggestion": {
                            "type": "string",
                            "description": "Advice on showcasing or adding relevant technical skills to improve the match."
                        },
                    },
                    "required": ["score", "comment", "suggestion"],
                },
                "responsibility": {
                    "type": "object",
                    "properties": {
                        "score": {"type": "integer", "minimum": 0, "maximum": 100},
                        "comment": {"type": "string"},
                        "suggestion": {
                            "type": "string",
                            "description": "Suggestions for aligning previous responsibilities more closely with the role."
                        },
                    },
                    "required": ["score", "comment", "suggestion"],
                },
                "certificate": {
                    "type": "object",
                    "properties": {
                        "score": {"type": "integer", "minimum": 0, "maximum": 100},
                        "comment": {"type": "string"},
                        "suggestion": {
                            "type": "string",
                            "description": "Certifications that could improve resume relevance or score."
                        },
                    },
                    "required": ["score", "comment", "suggestion"],
                },
                "soft_skill": {
                    "type": "object",
                    "properties": {
                        "score": {"type": "integer", "minimum": 0, "maximum": 100},
                        "comment": {"type": "string"},
                        "suggestion": {
                            "type": "string",
                            "description": "Tips on how to improve soft skills representation or what to include."
                        },
                    },
                    "required": ["score", "comment", "suggestion"],
                },
                "summary_comment": {
                    "type": "string",
                    "description": "Overall comment about the candidate’s match based on all categories.",
                },
            },
            "required": [
                "degree",
                "experience",
                "technical_skill",
                "responsibility",
                "certificate",
                "soft_skill",
                "summary_comment",
            ],
        },
    }
]
