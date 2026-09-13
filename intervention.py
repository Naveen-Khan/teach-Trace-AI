def generate_intervention_materials(analysis_data):
    primary_gap = analysis_data.get("primary_gap", "Adding Denominators Directly")
    
    return {
        "concept": primary_gap,
        "reteach_strategy": """
1. **Visual Area Model (5 mins):** Use a pizza or pie chart to show why 1/2 + 1/3 cannot equal 2/5 (show that 2/5 is smaller than 1/2!).
2. **Denominators as Unit Names (5 mins):** Explain that denominators are like labels (e.g., 1 Apple + 1 Orange cannot equal 2 Apploranges; you need a common unit 'Fruits').
3. **Targeted Sort Activity (5 mins):** Have students classify fraction addition problems as 'Same Denominators (Add Top)' vs 'Different Denominators (Convert First)'.
        """,
        "activity_text": """
**Classroom Activity: "Same Unit or Convert First?"**

*Instructions for Students:*
Classify the following fraction pairs. Do you need to convert to a common denominator first? Explain WHY.

1. `1/5 + 3/5`  -->  [ ] Add directly  [ ] Convert first
2. `1/4 + 1/2`  -->  [ ] Add directly  [ ] Convert first
3. `2/7 + 4/7`  -->  [ ] Add directly  [ ] Convert first

*Discussion Prompt:* Why is `1/4 + 1/2` NOT equal to `2/6`? Draw a diagram to justify your answer.
        """,
        "diagnostic_question": """
**Quick Check Question:**
Sara says: *"To add 2/5 and 1/5, I get 3/5. So to add 2/5 and 1/10, I should get 3/15."*

Is Sara correct or incorrect? Explain the specific rule Sara forgot about denominators.
        """
    }
