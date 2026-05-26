# 🤖 Agent Task List (Execution & Data)

> **Focus**: Research, Drafting, Data Entry, Analysis, Repetition.
> **Rule**: Always output in a format ready for Human review (Markdown, Draft mode, etc.).
> **Reference**: See `PROJECT-RULES.md` for the 50 guiding principles.

---

## 🕵️ Research & Intelligence

### 1. Prospect Research (Daily/On-Demand)
- **Trigger**: New lead identified or list provided.
- **Task**:
    - Scrape company website.
    - Summarize value proposition.
    - Identify key decision makers (CEO, COO, Ops Manager).
    - Find recent news/posts for "hooks".
    - **Constraint**: Must use `07-Assets/templates/brand-brief-template.md`.
- **Workflow**: `agent-tasks/workflows/research-prospect.md`

### 2. Competitor Analysis (Weekly)
- **Trigger**: Monday morning.
- **Task**:
    - Visit top 3 competitor LinkedIn profiles/websites.
    - Log new offers, pricing changes, or viral posts.
    - Update `05-Sales/battle-cards/` if needed.
- **Workflow**: `agent-tasks/workflows/analyze-competitor.md`

---

## ✍️ Content Drafting

### 3. Social Media Drafts (Weekly Batch)
- **Trigger**: Topic list provided by Human.
- **Task**:
    - Draft LinkedIn posts using the "Viral Framework" (Hook, Story, Lesson, CTA).
    - Suggest image ideas or generate image prompts.
    - Suggest image ideas or generate image prompts.
    - **Constraint**: Must use `07-Assets/templates/content-post-template.md`.
- **Workflow**: `agent-tasks/workflows/generate-linkedin-post.md`

### 4. Cold Outreach Drafts (Daily)
- **Trigger**: New prospect researched.
- **Task**:
    - Draft "Icebreaker" email based on research.
    - Draft "Follow-up" sequence customized to their industry.
    - Draft "Follow-up" sequence customized to their industry.
    - **Constraint**: Must use `07-Assets/templates/outreach-email-template.md`.
- **Workflow**: `agent-tasks/workflows/draft-cold-email.md`

---

## 📊 Analytics & Reporting

### 5. Data Aggregation (Weekly)
- **Trigger**: Friday morning.
- **Task**:
    - Collect stats from LinkedIn (views, likes), Email (opens, clicks), Website (visitors).
    - Update `06-Analytics/dashboards/weekly-kpi-dashboard.md`.
    - Flag any metric below target (e.g., Open Rate < 25%).

---

## 🛠️ Maintenance

### 6. Link & Asset Check (Monthly)
- **Trigger**: First of the month.
- **Task**:
    - Crawl `AI-Whisperers-Marketing-Hub` to find broken links.
    - Verify all "Source of Truth" files are consistent with each other.
