import streamlit as st
import pandas as pd
import datetime

# Set the page title and layout
st.set_page_config(page_title="Myndful Steps", layout="wide")

# Initialize session state variables
if 'confidence' not in st.session_state:
    st.session_state.confidence = None
if 'stage' not in st.session_state:
    st.session_state.stage = None
if 'exercise_frequency' not in st.session_state:
    st.session_state.exercise_frequency = 0
if 'exercise_duration' not in st.session_state:
    st.session_state.exercise_duration = 0
if 'cardio_minutes' not in st.session_state:
    st.session_state.cardio_minutes = 0
if 'weight_minutes' not in st.session_state:
    st.session_state.weight_minutes = 0
if 'barriers' not in st.session_state:
    st.session_state.barriers = ""
if 'activity_log' not in st.session_state:
    st.session_state.activity_log = {}

# Title of the app
st.title("Myndful Steps")

# Sidebar navigation
st.sidebar.header("Navigation")
app_mode = st.sidebar.radio("Select Mode", ["Home", "Self-Efficacy", "Stages of Change", "Physical Activity", "Barriers to Physical Activity", "Educational Module", "Activity Log", "Results"])

# Home Page
if app_mode == "Home":
    st.header("Welcome to Myndful Steps")
    st.write("""
    This app helps you measure your health behavior change using theories of self-efficacy and stages of change. 
    It also assesses your physical activity using the **Modified Exercise Vital Sign (EVS) Score**. The app will provide personalized recommendations based on your responses.
    """)

# Educational Module
elif app_mode == "Educational Module":
    st.header("Educational Module: Exercise & Behavior Change")
    st.write("""
**World Health Organization for Adult Physical Activity (per week)**:
    - Engage in either:
        - Moderate exercise for 150-300 minutes; OR,
        - Vigorous exercise for 75-150 minutes.
        - Ideally, the exercise is spread throughout the week
    
**Benefits of Exercise**:
    - Improves cardiovascular health, strength, and flexibility
    - Boosts mood and reduces symptoms of depression and anxiety
    - Enhances cognitive function and reduces risks of chronic diseases

**Consequences of Physical Inactivity**:
    Increase risk of:
        - Early death
        - Coronary heart disease
        - Stroke
        - High BP
        - Adverse blood lipid profile
        - Type 2 diabetes
        - Metabolic syndrome
        - Colon cancer
        - Breast cancer
        - Cancer recurrence/secondary cancers

**Theories of Health Behavior Change**:
    - **Self-Efficacy**:
        - The belief in one's ability to accomplish a task
        - People will adhere to behaviors if they:
            - Believe they can initiate and carry out this behavior (self-efficacy),
            - Believe that the behavior will produce valuable outcomes (outcome expectations)
        - Reciprocal determinism: Human functioning is a product of interaction of behavior, environment, and person variables, especially self-efficacy and other cognitive processes
            - Sources of self-efficacy:
                - Mastery Experiences (successes/failures): personal successes and failures that shape a person’s confidence in their abilities.
                    - Successes reinforce self-efficacy,
                    - Failures—if interpreted as a learning experience—can also build resilience and determination.
                - Vicarious Experience (modeling): observing others (role models) successfully perform a behavior, which can enhance self-efficacy in those who feel similar to the model.
                    - If users see someone else succeed, especially someone they identify with, it increases their belief that they, too, can succeed.
                - Social or Verbal Persuasion: encouragement or feedback from others that builds confidence.
                    - Positive reinforcement from friends, coaches, or even virtual sources can strengthen self-efficacy by helping people believe they have the skills to succeed.
                - Physiological Responses: Physical and emotional reactions (e.g., fatigue, stress, or excitement) can influence self-efficacy.
                    - When individuals feel relaxed and positive, they tend to have stronger self-efficacy beliefs.
                    - Conversely, if they experience negative physical symptoms like exhaustion or anxiety, they may doubt their ability to succeed.

    - **Stages of Change**:
        - Pre-contemplation
            - Individuals in this stage have no immediate intention to change their behavior and may be unaware of the problem or its consequences. Often, people in this stage underestimate the benefits of change or see the downsides of change as too significant. Health interventions at this stage aim to raise awareness and encourage self-reflection, helping individuals recognize why the change might be beneficial in the future.
        
        - Contemplation
            - At this stage, individuals acknowledge the need for change and start weighing the pros and cons but have not committed to action. This period can involve ambivalence and may last for extended periods as individuals assess their motivations. Effective interventions in the contemplation stage often provide information on the benefits of change and work to reduce perceived obstacles, helping individuals develop a stronger desire to take action.
        
        - Preparation
            - In the preparation stage, individuals make concrete plans to begin the desired behavior change, such as gathering information, setting goals, or preparing resources. The decision to act is made, and short-term steps are initiated to build momentum toward change. Supportive strategies here can include setting a start date, creating a plan, and finding resources or support systems to help maintain motivation.
        
        - Action
            - This stage involves direct efforts to change behavior, such as actively engaging in exercise routines if the goal is physical activity. It is often the most visible stage, where individuals start adopting new, healthier behaviors. Support during this phase is essential to reinforce motivation, celebrate successes, and provide tools to overcome challenges, ensuring that the change can be sustained.

        - Maintenance
            - Individuals in the maintenance stage continue the behavior consistently, typically for six months or more, and work to prevent relapse. This phase focuses on reinforcing progress and finding strategies to deal with potential triggers that could lead to reverting to old habits. Maintenance often involves a continuous commitment to the behavior, adjusting strategies as necessary, and may include reminders of the initial motivations to help sustain progress.

    **Counseling Services**:
    - **The Counseling Center** is available for all students and offers mental health support.
    - **Contact Information**:
        - Phone: 781-891-2274
        - Location: Callahan Building, 2nd Floor
        - Hours: Mon-Fri, 9am-12pm & 1pm-4pm (Closed 12-1pm for lunch)
    """)

# Self-Efficacy Assessment
elif app_mode == "Self-Efficacy":
    st.header("Self-Efficacy Assessment")
    st.write("""
    Self-efficacy refers to an individual's belief in their ability to succeed in specific situations or accomplish a task. 
    This assessment will help measure your confidence in making health behavior changes.
    """)
    confidence = st.slider("On a scale from 1 to 10, how confident are you in your ability to make a lasting change in your health behaviors?", 1, 10, 5)
    if st.button("Submit Self-Efficacy Score"):
        st.session_state.confidence = confidence
        st.success(f"Your self-efficacy score is: {confidence}. Higher scores indicate greater confidence in making health changes.")

