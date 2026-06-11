# PR Quality Metrics Guide

## Core Metrics

### 1. Review Time & Cycles
- Goal: 1-2 review rounds
- Track: Number of review iterations

### 2. Change Size
- Target: < 400 lines, < 10 files

### 3. Review Comments
- Fewer substantive comments = better

### 4. Post-Merge Bug Rate
- Link bugs to PRs in tickets
- Calculate % of PRs with associated bugs

### 5. Test Coverage Added
- Meaningful tests for new code

### 6. Architectural Impact
- New deps added?
- Tech debt signals (e.g., complexity score)

### 7. AI Cost per Good PR
- Track token usage if AI tools were involved
- Chart cost vs quality

## Implementation Tips
- Use GitHub labels or custom fields for "Business Impact"
- Automate where possible with GitHub Actions