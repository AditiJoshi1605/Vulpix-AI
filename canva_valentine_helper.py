"""
Simple Canva Valentine's PPT Automation
Uses direct tool calls instead of vision
"""

# Simple plan for Canva Valentine's Day PPT
CANVA_VALENTINE_PLAN = [
    {
        "step": 1,
        "action": "navigate",
        "url": "https://www.canva.com/search/templates?q=valentine%20presentation",
        "description": "Navigate directly to Valentine's templates"
    },
    {
        "step": 2,
        "action": "wait",
        "duration": 3000,
        "description": "Wait for templates to load"
    },
    {
        "step": 3,
        "action": "click",
        "selector": "a[href*='valentine'], div[data-test*='template']:first-child, .template-card:first-child",
        "description": "Click first Valentine template"
    },
    {
        "step": 4,
        "action": "wait",
        "duration": 2000,
        "description": "Wait for editor to load"
    }
]

// Run it!
createValentinePPT();
""")
