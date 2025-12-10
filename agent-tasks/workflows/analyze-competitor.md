# Workflow: Analyze Competitor

**Role**: You are a Competitive Intelligence Analyst.

**Context**:
- **Goal**: Understand how competitors are positioning themselves to find our "Wedge".
- **Reference**: `05-Sales/battle-cards/`

## Inputs
*(Replace these variables when running the prompt)*
- `{{COMPETITOR_URL}}`: [URL]
- `{{COMPETITOR_NAME}}`: [Name]

## Instructions

1. **Analyze Pricing**:
   - Do they show pricing? Is it high ($$$), low ($), or "Contact Us"?
   - Do they charge hourly or project-based?
2. **Analyze Positioning**:
   - What is their headline?
   - Do they focus on "Strategy" (Consultants) or "Tools" (Devs)?
3. **Analyze Content**:
   - Check their Blog/LinkedIn. Are they active?
   - What topics are they covering?
4. **Find Weaknesses**:
   - Is their site slow/broken?
   - Is their copy vague?
   - Do they lack case studies?

## Output Format

```markdown
# Competitor Analysis: {{COMPETITOR_NAME}}

## 1. Positioning
- **Headline**: "[Text]"
- **Vibe**: [e.g., Corporate, Hipster, Tech-Heavy]

## 2. Pricing Strategy
- [Details]

## 3. Their Strengths (Be Honest)
- [What do they do well?]

## 4. Their Weaknesses (Our Opportunity)
- [Where are they failing?]

## 5. Action Item
- Update Battle Card? [Yes/No]
- Counter-content idea: "[Idea]"
```
