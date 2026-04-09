# HCDE 530 Project Context

## Project Purpose
This project demonstrates how to process a data file effectively and highlight the most important parts of the code.  
It is designed as a fully functional classroom demo dataset and workflow, based on paraphrased real-world UX themes.

## Audience
- Primary: HCDE/UX classmates, instructors, and TAs
- Skill level: mixed (complete beginners, beginner coders, and intermediate users)
- Design implication: prioritize beginner-friendly clarity without limiting more advanced users

## Desired Experience
- Any audience member should be able to:
  - run the script
  - understand what each major code section is doing
  - optionally view results in a web page/dashboard

## Priority Outcomes (Effort Signal)
1. **Data pipeline clarity**  
   Code clearly shows how raw CSV data becomes structured outputs.
2. **Insightful summaries**  
   Outputs include practical metrics and simple interpretation.
3. **Reproducible workflow**  
   Running the script and previewing the dashboard should be straightforward.
4. **Important code emphasis**  
   Key blocks are easy to identify (load, transform, summarize, render).
5. **Adaptability**  
   Project can be updated to a new CSV with minimal edits.

## Required Outputs
The script/dashboard should consistently support:
- total number of responses
- response-length statistics (average, shortest, longest)
- role-based breakdowns
- frequent words/themes (with basic filtering)
- response-level detail view (table/list)

## Code Style Expectations
- Readability first: clear names, plain language, simple flow
- Keep functions short and focused where possible
- Include practical error handling for common issues (missing file/columns)
- Keep output formatting clean and scannable
- Make customization easy (e.g., a single place to change file input settings)
- Avoid unnecessary complexity and heavy dependencies unless needed

## Data and Content Notes
- Use classroom-safe demo data
- Keep themes realistic and useful for UX discussion
- Avoid exposing sensitive or identifiable real participant information

## Definition of Done
Work is complete when:
- script runs successfully on the project dataset
- dashboard loads and communicates key findings clearly
- important code sections are obvious and explainable
- README/run instructions are accurate
- project is easy for non-engineers to follow

## Collaboration Guidance for AI Assistants
When assisting on this project:
- explain intent first, then mechanics
- propose small, focused changes
- preserve behavior unless change is explicitly requested
- include brief next steps (run, preview, commit) when relevant
