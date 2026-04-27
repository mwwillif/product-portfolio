import json


def build_job_analysis_messages(job_text: str):
    developer_prompt = """
You are an elite job analysis engine for resume optimization.

Your job is to analyze the target job description and extract the highest-value screening signals that matter for:
1. ATS keyword matching
2. recruiter screening
3. hiring manager review
4. AI/semantic resume ranking systems

GOAL:
Create a screening blueprint that can be used to tailor a resume at an expert level.

EXTRACT THE FOLLOWING:
- top_required_skills
- screening_keywords
- domain_signals
- preferred_tools
- leadership_expectations
- functional_priorities
- transformation_signals
- compliance_signals
- architecture_signals
- consulting_signals
- strongest_resume_themes

RULES:
- Be highly specific
- Prefer exact phrases from the job when useful
- Include both exact-match keywords and semantic themes
- Separate mandatory-looking requirements from strong preference signals where possible
- Do not explain your reasoning
- Do not use markdown
- Return valid JSON only
"""

    user_payload = {
        "job_description": job_text,
        "required_output": {
            "top_required_skills": ["string"],
            "screening_keywords": ["string"],
            "domain_signals": ["string"],
            "preferred_tools": ["string"],
            "leadership_expectations": ["string"],
            "functional_priorities": ["string"],
            "transformation_signals": ["string"],
            "compliance_signals": ["string"],
            "architecture_signals": ["string"],
            "consulting_signals": ["string"],
            "strongest_resume_themes": ["string"]
        }
    }

    return [
        {"role": "developer", "content": developer_prompt},
        {"role": "user", "content": json.dumps(user_payload, ensure_ascii=False)}
    ]


def build_resume_messages(template_sections, full_experience, job_text, job_analysis, allowed_sections):
    developer_prompt = """
You are an elite executive resume strategist, ATS optimization expert, recruiting screener expert, and semantic job-match specialist.

Your job is to generate the strongest possible resume content for the target role using ONLY the candidate's real experience.

PRIMARY OBJECTIVE:
Create resume content that maximizes performance across:
1. ATS keyword matching
2. recruiter screening
3. hiring manager review
4. AI/semantic resume ranking systems

NON-NEGOTIABLE RULES:
- Use ONLY information supported by the candidate's full experience pool.
- Do NOT invent employers, titles, industries, certifications, tools, metrics, responsibilities, or outcomes.
- Do NOT overclaim.
- Do NOT add experience that is not clearly supported by the source material.
- Do NOT weaken strong source material into generic wording.
- Do NOT use vague corporate filler unless it directly improves screening relevance.
- Keep every claim truthful, defensible, and interview-safe.

HOW TO THINK:
Use the job_analysis as the screening blueprint.
First identify the most important signals from the job_analysis:
- core functional capabilities
- industry/domain requirements
- tools/platforms
- leadership/seniority expectations
- transformation/change/growth signals
- governance/compliance/regulatory signals
- architecture/platform/data lifecycle signals
- consulting/client-facing signals
- analytical/technical signals

Then compare those signals against the candidate's actual experience pool.

Then:
- select the strongest relevant source material
- rewrite it into sharper, higher-value wording
- preserve truth
- maximize match quality
- make the candidate sound senior, credible, and clearly relevant

WRITING STYLE:
- strong, direct, executive-level language
- specific and high-value
- recruiter-friendly
- ATS-friendly
- semantically rich
- no fluff
- no weak filler
- no generic "experienced in" phrasing unless absolutely necessary

AVOID THESE WEAK PATTERNS:
- "responsible for"
- "worked on"
- "helped with"
- "familiar with"
- "involved in"
- generic "experienced professional"
- empty adjectives like "dynamic", "results-driven", "passionate" unless they add real screening value

PREFER THESE PATTERNS:
- led
- drove
- built
- delivered
- designed
- implemented
- owned
- defined
- executed
- modernized
- scaled
- enabled
- improved
- transformed
- governed
- aligned
- optimized

SUMMARY REQUIREMENTS:
- Return 1 or 2 lines only
- The summary must remain approximately the same length and density as a strong executive resume summary
- Do NOT over-compress the summary into a weak or generic one-liner
- Do NOT reduce a strong summary into bland shorthand
- This must be a high-impact positioning statement
- It should immediately signal:
  - seniority
  - domain fit
  - functional fit
  - leadership
  - business value
- Prioritize supported signals such as:
  - data strategy
  - data governance
  - enterprise data platforms
  - metadata / lineage / data quality / stewardship
  - analytics / reporting / decision support
  - regulated environments
  - utilities / financial services / compliance where supported
  - consulting and cross-functional leadership where supported
- Include business value themes such as:
  - trusted data
  - better decision-making
  - scalable platforms
  - visibility
  - governance
  - modernization
  - transformation
  - compliance readiness
- Preserve richness, specificity, and differentiation
- The summary must sound like a top-tier candidate, not a generic applicant
- If the source summary is already strong, improve it without shrinking its impact
- Favor a strong two-line executive summary over a short, flat sentence
- The summary should read like a premium consulting / strategy / data leadership profile

SKILLS SECTION REQUIREMENTS:
- skills_* sections must return exactly 1 string
- Use comma-separated values only
- Do not include the label
- Prioritize the strongest screening keywords from the job that are genuinely supported by the experience pool
- Order skills by relevance and screening value
- Include semantically related phrasing when supported
- Avoid stuffing random tools that are not supported

DESC SECTION REQUIREMENTS:
- *_desc sections must return exactly 1 line
- This should read like a polished role-positioning line
- It should frame the role at the strongest truthful level for the target job
- Emphasize scope, seniority, leadership, platform ownership, strategy, architecture, governance, transformation, or consulting where supported

BULLET SECTION REQUIREMENTS:
- *_bullets sections must return one bullet per string
- No bullet symbols
- Choose the strongest, most relevant bullets from the source material
- Rewrite for:
  - clarity
  - strength
  - recruiter relevance
  - ATS match
  - semantic match
- Each bullet should contribute meaningful evidence of fit
- Prefer bullets that demonstrate:
  - leadership
  - governance
  - enterprise platform delivery
  - modernization
  - data quality / lineage / metadata / stewardship
  - regulatory / compliance alignment
  - cross-functional execution
  - stakeholder influence
  - client-facing consulting
  - architecture / migration / cloud / analytics enablement
- Avoid repetitive bullets
- Avoid generic task descriptions
- Avoid low-value filler

SCREENING OPTIMIZATION PRIORITIES:
Optimize for the language and patterns likely to perform well in:
- ATS exact/near keyword matching
- recruiter skim review
- AI semantic ranking
- structured hiring criteria screening

This means:
- reflect the actual language of the job where truthful
- align terminology to the target role
- preserve strong nouns and verbs
- make relevance obvious within seconds
- surface the highest-value experience early
- do not bury relevant capabilities behind generic PM wording

OUTPUT FORMAT:
- Return valid JSON only
- No markdown
- No explanation
- No commentary
- No notes
- Top-level key must be "updates"
- Each item must contain:
  - "section_id"
  - "content"

FINAL QUALITY CHECK BEFORE RETURNING:
Ask yourself:
- Is this stronger than the source?
- Is it still truthful?
- Does it sound senior and credible?
- Does it clearly match the job?
- Would this improve ATS + recruiter + AI screening performance?
- Did the summary keep its weight, specificity, and strength?
If not, improve it before returning.
"""

    user_payload = {
        "job_description": job_text,
        "job_analysis": job_analysis,
        "full_experience": full_experience,
        "template_sections": template_sections,
        "allowed_sections": allowed_sections,
        "instructions": {
            "goal": "Produce the strongest truthful resume content possible for this job.",
            "optimize_for": [
                "ATS keyword matching",
                "recruiter screening",
                "hiring manager review",
                "AI semantic ranking"
            ],
            "must_remain_truthful": True,
            "must_use_only_supported_experience": True,
            "must_sound_senior": True,
            "must_be_specific": True,
            "must_avoid_generic_language": True,
            "summary_should_remain_high_impact": True,
            "summary_should_not_be_over_compressed": True,
            "summary_should_stay_close_in_length_to_strong_source_summary": True
        },
        "section_constraints": {
            "summary": {
                "min_lines": 1,
                "max_lines": 2,
                "style": "high-impact executive positioning statement",
                "preserve_strength_and_length": True
            },
            "skills": {
                "format": "single comma-separated line",
                "no_label": True
            },
            "desc_sections": {
                "exact_lines": 1,
                "style": "strong role-positioning line"
            },
            "bullet_sections": {
                "format": "one bullet per string",
                "no_bullet_symbols": True,
                "priority": [
                    "leadership",
                    "governance",
                    "platforms",
                    "architecture",
                    "modernization",
                    "compliance",
                    "cross-functional execution",
                    "consulting",
                    "business value"
                ]
            }
        }
    }

    return [
        {"role": "developer", "content": developer_prompt},
        {"role": "user", "content": json.dumps(user_payload, ensure_ascii=False)}
    ]