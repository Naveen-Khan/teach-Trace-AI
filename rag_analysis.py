import os
import json
import pandas as pd

def analyze_student_answers(uploaded_file, sample_data=True, reference_notes=""):
    """
    Simulates / processes RAG retrieval and linguistic analysis across 4 dimensions:
    1. Grammar & Sentence Structure
    2. Vocabulary & Subject Terminology
    3. Reasoning Steps & Logic
    4. Conceptual Understanding & Misconceptions
    """
    
    # Standard classroom dataset representing 30 students
    student_responses = [
        {"student": "Ali Ahmed", "question": "Q1: What is 1/2 + 1/3?", "answer": "2/5 because 1+1=2 and 2+3=5", "score": 0, "issue": "Added numerators and denominators directly"},
        {"student": "Sara Khan", "question": "Q1: What is 1/2 + 1/3?", "answer": "5/6 (used LCD 6)", "score": 100, "issue": "None — Correct"},
        {"student": "Ahmed Raza", "question": "Q1: What is 1/2 + 1/3?", "answer": "2/5", "score": 0, "issue": "Added numerators and denominators directly"},
        {"student": "Fatima Noor", "question": "Q1: What is 1/2 + 1/3?", "answer": "5/6", "score": 100, "issue": "None — Correct"},
        {"student": "Usman Ali", "question": "Q1: What is 1/2 + 1/3?", "answer": "2/6 because 1+1=2 and 2+3=6", "score": 0, "issue": "Added numerators directly, multiplied denominators"},
        {"student": "Ayesha Malik", "question": "Q1: What is 1/2 + 1/3?", "answer": "2/5", "score": 0, "issue": "Added numerators and denominators directly"},
        {"student": "Zainab Bibi", "question": "Q1: What is 1/2 + 1/3?", "answer": "3/5", "score": 0, "issue": "Added numerators (1+2=3) and denominators"},
        {"student": "Bilal Hassan", "question": "Q1: What is 1/2 + 1/3?", "answer": "5/6", "score": 100, "issue": "None — Correct"},
        {"student": "Hamza Tariq", "question": "Q1: What is 1/2 + 1/3?", "answer": "2/5", "score": 0, "issue": "Added numerators and denominators directly"},
        {"student": "Maryam Saeed", "question": "Q1: What is 1/2 + 1/3?", "answer": "2/5", "score": 0, "issue": "Added numerators and denominators directly"}
    ]
    
    gaps_summary = [
        {
            "concept": "Adding Denominators Directly",
            "affected": "18 / 30 (60%)",
            "severity": "High",
            "type": "Major Misconception",
            "evidence": "Students add numerators (1+1) and denominators (2+3) directly to get 2/5 instead of converting to common denominator 6."
        },
        {
            "concept": "Finding Least Common Multiple (LCM)",
            "affected": "12 / 30 (40%)",
            "severity": "Medium",
            "type": "Concept Confusion",
            "evidence": "Students struggle to convert fractions into equivalent fractions with equal denominators before addition."
        },
        {
            "concept": "Fraction Terminology (Numerator vs Denominator)",
            "affected": "9 / 30 (30%)",
            "severity": "Medium",
            "type": "Vocabulary Error",
            "evidence": "Incorrect use of 'top number' and 'bottom number' without understanding fractional parts."
        },
        {
            "concept": "Incomplete Explanation Steps",
            "affected": "7 / 30 (23%)",
            "severity": "Low",
            "type": "Reasoning Logic Gap",
            "evidence": "Students state correct final answer without showing the intermediate common denominator conversion."
        }
    ]
    
    question_ambiguity = {
        "flagged": True,
        "question": "Q3: Explain what happens when you combine two different fractions.",
        "issue": "Question wording is ambiguous. 8 students interpreted 'combine' as multiplication rather than addition.",
        "recommendation": "Rephrase to: 'Explain the steps required to add two fractions with different denominators.'"
    }
    
    return {
        "student_responses": student_responses,
        "gaps_summary": gaps_summary,
        "question_ambiguity": question_ambiguity,
        "class_average": 64,
        "primary_gap": "Adding Denominators Directly"
    }
