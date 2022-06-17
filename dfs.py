import pandas as pd
import numpy as np
from collections import Counter


df = pd.read_csv('data2.csv', header=0)

# CLEAN DATAFRAME
def clean_df(df=df):
    
    # select cols
    df = (df[['Recorded Date', 'unique_id', 'Complete Spontaneous Bowel Movements\n\n \nA Complete Spontaneous Bowel Movement (CSBM) is defined as an episode of spontaneous and complete bowel movement without discomfort.\n\n \n\nIn the last 7 days, how often has your child passed stools:', "This chart shows the different types of stools. Based on this chart, please rate your child's most common stool in the last 7 days:", 'Cleveland Constipation Score\n\n\n\nThese questions describe the difficulty your child has passing stools.\n\n \nFrequency of bowel movements', 'Time: minutes in lavatory per episode', 'Difficulty: painful evacuation effort', 'Assistance: type of assistance', 'Completeness: feeling Incomplete evacuation', 'Failure: unsucessful attempts at evacuation in the last 7 days', 'Pain: abdominal pain', 'History: duration of constipation', "St Mark's Score\n\n\n\nThese questions describe how often your child soiled in the last 1 month. - Incontinence of solid stool", "St Mark's Score\n\n\n\nThese questions describe how often your child soiled in the last 1 month. - Incontinence of liquid stool (including smears)", "St Mark's Score\n\n\n\nThese questions describe how often your child soiled in the last 1 month. - Incontinence for gas (excessive farting)", "St Mark's Score\n\n\n\nThese questions describe how often your child soiled in the last 1 month. - Incontinence causing changes to usual activities", '. - Need to wear a pad or nappy', '. - Taking constipation medicines', '. - Inability to hold stools for more than 15 minutes', "Daily Activity Diary\n\nThis diary records your child's daily routine. In the past 7 days, please select all the activities your child has done each day: - [OtherDate-DM--7%20day]", "Daily Activity Diary\n\nThis diary records your child's daily routine. In the past 7 days, please select all the activities your child has done each day: - [OtherDate-DM--6%20day]", "Daily Activity Diary\n\nThis diary records your child's daily routine. In the past 7 days, please select all the activities your child has done each day: - [OtherDate-DM--5%20day]", "Daily Activity Diary\n\nThis diary records your child's daily routine. In the past 7 days, please select all the activities your child has done each day: - [OtherDate-DM--4%20day]", "Daily Activity Diary\n\nThis diary records your child's daily routine. In the past 7 days, please select all the activities your child has done each day: - [OtherDate-DM--3%20day]", "Daily Activity Diary\n\nThis diary records your child's daily routine. In the past 7 days, please select all the activities your child has done each day: - [OtherDate-DM--2%20day]", "Daily Activity Diary\n\nThis diary records your child's daily routine. In the past 7 days, please select all the activities your child has done each day: - [OtherDate-DM--1%20day]", "Daily Activity Diary\n\nThis diary records your child's daily routine. In the past 7 days, please select all the activities your child has done each day: - [CurrentDate-DM]", 'Management Plan\n\n\n\nThis form describes the different types of care your child is receiving:', 'Impact Measurement Tool (Carer)\n\nThese questions describe the impact of constipation on your daily life.\n\n\n \n\nIn the past 6 months, how much of a problem has your child had with everyday activities: - Doing chores around the house', 'Impact Measurement Tool (Carer)\n\nThese questions describe the impact of constipation on your daily life.\n\n\n \n\nIn the past 6 months, how much of a problem has your child had with everyday activities: - Having hurts or aches', 'Impact Measurement Tool (Carer)\n\nThese questions describe the impact of constipation on your daily life.\n\n\n \n\nIn the past 6 months, how much of a problem has your child had with everyday activities: - Lifting something heavy', 'Impact Measurement Tool (Carer)\n\nThese questions describe the impact of constipation on your daily life.\n\n\n \n\nIn the past 6 months, how much of a problem has your child had with everyday activities: - Low energy level', 'Impact Measurement Tool (Carer)\n\nThese questions describe the impact of constipation on your daily life.\n\n\n \n\nIn the past 6 months, how much of a problem has your child had with everyday activities: - Participating in sports activity / exercise', 'Impact Measurement Tool (Carer)\n\nThese questions describe the impact of constipation on your daily life.\n\n\n \n\nIn the past 6 months, how much of a problem has your child had with everyday activities: - Running', 'Impact Measurement Tool (Carer)\n\nThese questions describe the impact of constipation on your daily life.\n\n\n \n\nIn the past 6 months, how much of a problem has your child had with everyday activities: - Taking a bath or shower by him or herself', 'Impact Measurement Tool (Carer)\n\nThese questions describe the impact of constipation on your daily life.\n\n\n \n\nIn the past 6 months, how much of a problem has your child had with everyday activities: - Walking more than one block', 'Impact Measurement Tool (Child)\n\nThese questions describe the impact of constipation on your daily life.\n\nIn the past 6 months, how much of a problem have you had with your health and activities: - I have low energy', 'Impact Measurement Tool (Child)\n\nThese questions describe the impact of constipation on your daily life.\n\nIn the past 6 months, how much of a problem have you had with your health and activities: - I hurt or ache', 'Impact Measurement Tool (Child)\n\nThese questions describe the impact of constipation on your daily life.\n\nIn the past 6 months, how much of a problem have you had with your health and activities: - It is hard for me to do chores around the house', 'Impact Measurement Tool (Child)\n\nThese questions describe the impact of constipation on your daily life.\n\nIn the past 6 months, how much of a problem have you had with your health and activities: - It is hard for me to do sports activity or exercise', 'Impact Measurement Tool (Child)\n\nThese questions describe the impact of constipation on your daily life.\n\nIn the past 6 months, how much of a problem have you had with your health and activities: - It is hard for me to lift something heavy', 'Impact Measurement Tool (Child)\n\nThese questions describe the impact of constipation on your daily life.\n\nIn the past 6 months, how much of a problem have you had with your health and activities: - It is hard for me to run', 'Impact Measurement Tool (Child)\n\nThese questions describe the impact of constipation on your daily life.\n\nIn the past 6 months, how much of a problem have you had with your health and activities: - It is hard for me to take a bath or shower by myself', 'Impact Measurement Tool (Child)\n\nThese questions describe the impact of constipation on your daily life.\n\nIn the past 6 months, how much of a problem have you had with your health and activities: - It is hard for me to walk more than one block', 'In the past 6 months, how much of a problem has your child had with emotional functioning: - Feeling afraid or scared', 'In the past 6 months, how much of a problem has your child had with emotional functioning: - Feeling angry', 'In the past 6 months, how much of a problem has your child had with emotional functioning: - Feeling sad or blue', 'In the past 6 months, how much of a problem has your child had with emotional functioning: - Trouble sleeping', 'In the past 6 months, how much of a problem has your child had with emotional functioning: - Worrying about what will happen to him or her', 'In the past 6 months, how much of a problem has your child had with school functioning: - Forgetting things', 'In the past 6 months, how much of a problem has your child had with school functioning: - Keeping up with schoolwork', 'In the past 6 months, how much of a problem has your child had with school functioning: - Missing school because of not feeling well', 'In the past 6 months, how much of a problem has your child had with school functioning: - Missing school to go to the doctor / hospital', 'In the past 6 months, how much of a problem has your child had with school functioning: - Paying attention in class', 'In the past 6 months, how much of a problem has your child had with social functioning: - Getting along with other children', 'In the past 6 months, how much of a problem has your child had with social functioning: - Getting teased by other children', 'In the past 6 months, how much of a problem has your child had with social functioning: - Keeping up when playing with other children', 'In the past 6 months, how much of a problem has your child had with social functioning: - Not able to do things that other children his or her age can do', 'In the past 6 months, how much of a problem has your child had with social functioning: - Other kids not wanting to be his or her friend', 'In the past 6 months, how much of a problem have you had with getting along with others: - I cannot do things that other kids my age can do', 'In the past 6 months, how much of a problem have you had with getting along with others: - I have trouble getting along with other kids', 'In the past 6 months, how much of a problem have you had with getting along with others: - It is hard to keep up when I play with other kids', 'In the past 6 months, how much of a problem have you had with getting along with others: - Other kids do not want to be my friend', 'In the past 6 months, how much of a problem have you had with getting along with others: - Other kids tease me', 'In the past 6 months, how much of a problem have you had with your feelings: - I feel afraid or scared', 'In the past 6 months, how much of a problem have you had with your feelings: - I feel angry', 'In the past 6 months, how much of a problem have you had with your feelings: - I feel sad or blue', 'In the past 6 months, how much of a problem have you had with your feelings: - I have trouble sleeping', 'In the past 6 months, how much of a problem have you had with your feelings: - I worry about what will happen to me', 'In the past 6 months, how much of a problem have you had with your school: - I forget things', 'In the past 6 months, how much of a problem have you had with your school: - I have trouble keeping up with my schoolwork', 'In the past 6 months, how much of a problem have you had with your school: - I miss school because of not feeling well', 'In the past 6 months, how much of a problem have you had with your school: - I miss school to go to the doctor or hospital', 'In the past 6 months, how much of a problem have you had with your school: - It is hard to pay attention in class', 'Dietary Recall Diary\n\n\n\nThis diary records what your child has eaten in the last 3 days. Please list your child\'s food and drink below. \n\n\n\nNOTE: please separate each food with a comma e.g. "apple, banana, oranges"\n\n \nPlease record what your child ate and drank 3 days ago on [OtherDate-DM--3%20day] - Breakfast', 'Dietary Recall Diary\n\n\n\nThis diary records what your child has eaten in the last 3 days. Please list your child\'s food and drink below. \n\n\n\nNOTE: please separate each food with a comma e.g. "apple, banana, oranges"\n\n \nPlease record what your child ate and drank 3 days ago on [OtherDate-DM--3%20day] - Dinner', 'Dietary Recall Diary\n\n\n\nThis diary records what your child has eaten in the last 3 days. Please list your child\'s food and drink below. \n\n\n\nNOTE: please separate each food with a comma e.g. "apple, banana, oranges"\n\n \nPlease record what your child ate and drank 3 days ago on [OtherDate-DM--3%20day] - Lunch', 'Dietary Recall Diary\n\n\n\nThis diary records what your child has eaten in the last 3 days. Please list your child\'s food and drink below. \n\n\n\nNOTE: please separate each food with a comma e.g. "apple, banana, oranges"\n\n \nPlease record what your child ate and drank 3 days ago on [OtherDate-DM--3%20day] - Snack', 'Please recall what your child ate and drank yesterday on [OtherDate-DM--1%20day] - Breakfast', 'Please recall what your child ate and drank yesterday on [OtherDate-DM--1%20day] - Dinner', 'Please recall what your child ate and drank yesterday on [OtherDate-DM--1%20day] - Lunch', 'Please recall what your child ate and drank yesterday on [OtherDate-DM--1%20day] - Snack', 'Please record what your child ate and drank 2 days ago on [OtherDate-DM--2%20day] - Breakfast', 'Please record what your child ate and drank 2 days ago on [OtherDate-DM--2%20day] - Dinner', 'Please record what your child ate and drank 2 days ago on [OtherDate-DM--2%20day] - Lunch', 'Please record what your child ate and drank 2 days ago on [OtherDate-DM--2%20day] - Snack']]
        .copy()
        .rename(
            columns=
            {
                'Recorded Date':'recorded_date',
                'unique_id' : "QIPID",
                "Complete Spontaneous Bowel Movements\n\n \nA Complete Spontaneous Bowel Movement (CSBM) is defined as an episode of spontaneous and complete bowel movement without discomfort.\n\n \n\nIn the last 7 days, how often has your child passed stools:" : "csbm",
                "This chart shows the different types of stools. Based on this chart, please rate your child's most common stool in the last 7 days:" : "bristol_stool_chart",
                'Cleveland Constipation Score\n\n\n\nThese questions describe the difficulty your child has passing stools.\n\n \nFrequency of bowel movements' : "cleve_freq",
                'Time: minutes in lavatory per episode' : "cleve_time",
                'Difficulty: painful evacuation effort' : "cleve_difficulty",
                'Assistance: type of assistance' : "cleve_assistance",
                'Completeness: feeling Incomplete evacuation' : "clevel_complete",
                'Failure: unsucessful attempts at evacuation in the last 7 days' : "cleve_fail",
                'Pain: abdominal pain' : "cleve_pain", 
                'History: duration of constipation' : "cleve_duration",
                "St Mark's Score\n\n\n\nThese questions describe how often your child soiled in the last 1 month. - Incontinence of solid stool" : "SM_solid",
                "St Mark's Score\n\n\n\nThese questions describe how often your child soiled in the last 1 month. - Incontinence of liquid stool (including smears)" : "SM_liquid",
                "St Mark's Score\n\n\n\nThese questions describe how often your child soiled in the last 1 month. - Incontinence for gas (excessive farting)" : "SM_gas",
                "St Mark's Score\n\n\n\nThese questions describe how often your child soiled in the last 1 month. - Incontinence causing changes to usual activities" : "SM_activity_change",
                '. - Need to wear a pad or nappy' : "SM_pad",
                    '. - Taking constipation medicines' : "SM_constipation_med",
                '. - Inability to hold stools for more than 15 minutes' : "SM_inability_stool_15min",
                "Daily Activity Diary\n\nThis diary records your child's daily routine. In the past 7 days, please select all the activities your child has done each day: - [OtherDate-DM--7%20day]" : "daily_routine_7d",
                "Daily Activity Diary\n\nThis diary records your child's daily routine. In the past 7 days, please select all the activities your child has done each day: - [OtherDate-DM--6%20day]" : "daily_routine_6d",
                "Daily Activity Diary\n\nThis diary records your child's daily routine. In the past 7 days, please select all the activities your child has done each day: - [OtherDate-DM--5%20day]" : "daily_routine_5d",
                "Daily Activity Diary\n\nThis diary records your child's daily routine. In the past 7 days, please select all the activities your child has done each day: - [OtherDate-DM--4%20day]" : "daily_routine_4d",
                "Daily Activity Diary\n\nThis diary records your child's daily routine. In the past 7 days, please select all the activities your child has done each day: - [OtherDate-DM--3%20day]" : "daily_routine_3d",
                "Daily Activity Diary\n\nThis diary records your child's daily routine. In the past 7 days, please select all the activities your child has done each day: - [OtherDate-DM--2%20day]" : "daily_routine_2d",
                "Daily Activity Diary\n\nThis diary records your child's daily routine. In the past 7 days, please select all the activities your child has done each day: - [OtherDate-DM--1%20day]" : "daily_routine_1d",
                "Daily Activity Diary\n\nThis diary records your child's daily routine. In the past 7 days, please select all the activities your child has done each day: - [CurrentDate-DM]" : "daily_routine_0d",
                'Management Plan\n\n\n\nThis form describes the different types of care your child is receiving:' : "management",
                'Impact Measurement Tool (Carer)\n\nThese questions describe the impact of constipation on your daily life.\n\n\n \n\nIn the past 6 months, how much of a problem has your child had with everyday activities: - Doing chores around the house': 'carer_everyday_chores',
                'Impact Measurement Tool (Carer)\n\nThese questions describe the impact of constipation on your daily life.\n\n\n \n\nIn the past 6 months, how much of a problem has your child had with everyday activities: - Having hurts or aches': 'carer_everyday_pain',
                'Impact Measurement Tool (Carer)\n\nThese questions describe the impact of constipation on your daily life.\n\n\n \n\nIn the past 6 months, how much of a problem has your child had with everyday activities: - Lifting something heavy': 'carer_everyday_lift_heavy',
                'Impact Measurement Tool (Carer)\n\nThese questions describe the impact of constipation on your daily life.\n\n\n \n\nIn the past 6 months, how much of a problem has your child had with everyday activities: - Low energy level': 'carer_everyday_lethargy',
                'Impact Measurement Tool (Carer)\n\nThese questions describe the impact of constipation on your daily life.\n\n\n \n\nIn the past 6 months, how much of a problem has your child had with everyday activities: - Participating in sports activity / exercise': 'carer_everyday_participate_exercise',
                'Impact Measurement Tool (Carer)\n\nThese questions describe the impact of constipation on your daily life.\n\n\n \n\nIn the past 6 months, how much of a problem has your child had with everyday activities: - Running': 'carer_everyday_running',
                'Impact Measurement Tool (Carer)\n\nThese questions describe the impact of constipation on your daily life.\n\n\n \n\nIn the past 6 months, how much of a problem has your child had with everyday activities: - Taking a bath or shower by him or herself': 'carer_everyday_bath_self',
                'Impact Measurement Tool (Carer)\n\nThese questions describe the impact of constipation on your daily life.\n\n\n \n\nIn the past 6 months, how much of a problem has your child had with everyday activities: - Walking more than one block': 'carer_everyday_walking_block',
                'Impact Measurement Tool (Child)\n\nThese questions describe the impact of constipation on your daily life.\n\nIn the past 6 months, how much of a problem have you had with your health and activities: - I have low energy': 'child_everyday_lethargy',
                'Impact Measurement Tool (Child)\n\nThese questions describe the impact of constipation on your daily life.\n\nIn the past 6 months, how much of a problem have you had with your health and activities: - I hurt or ache': 'child_everyday_pain',
                'Impact Measurement Tool (Child)\n\nThese questions describe the impact of constipation on your daily life.\n\nIn the past 6 months, how much of a problem have you had with your health and activities: - It is hard for me to do chores around the house': 'child_everyday_chores',
                'Impact Measurement Tool (Child)\n\nThese questions describe the impact of constipation on your daily life.\n\nIn the past 6 months, how much of a problem have you had with your health and activities: - It is hard for me to do sports activity or exercise': 'child_everyday_participate_exercise',
                'Impact Measurement Tool (Child)\n\nThese questions describe the impact of constipation on your daily life.\n\nIn the past 6 months, how much of a problem have you had with your health and activities: - It is hard for me to lift something heavy': 'child_everyday_lift_heavy',
                'Impact Measurement Tool (Child)\n\nThese questions describe the impact of constipation on your daily life.\n\nIn the past 6 months, how much of a problem have you had with your health and activities: - It is hard for me to run': 'child_everyday_running',
                'Impact Measurement Tool (Child)\n\nThese questions describe the impact of constipation on your daily life.\n\nIn the past 6 months, how much of a problem have you had with your health and activities: - It is hard for me to take a bath or shower by myself': 'child_everyday_bath_self',
                'Impact Measurement Tool (Child)\n\nThese questions describe the impact of constipation on your daily life.\n\nIn the past 6 months, how much of a problem have you had with your health and activities: - It is hard for me to walk more than one block': 'child_everyday_walking_block',
                'In the past 6 months, how much of a problem has your child had with emotional functioning: - Feeling afraid or scared': 'carer_emotion_afraid',
                'In the past 6 months, how much of a problem has your child had with emotional functioning: - Feeling angry': 'carer_emotion_angry',
                'In the past 6 months, how much of a problem has your child had with emotional functioning: - Feeling sad or blue': 'carer_emotion_sad',
                'In the past 6 months, how much of a problem has your child had with emotional functioning: - Trouble sleeping': 'carer_emotion_insomnia',
                'In the past 6 months, how much of a problem has your child had with emotional functioning: - Worrying about what will happen to him or her': 'carer_emotion_worry',
                'In the past 6 months, how much of a problem has your child had with school functioning: - Forgetting things': 'carer_school_forget',
                'In the past 6 months, how much of a problem has your child had with school functioning: - Keeping up with schoolwork': 'carer_school_school_work',
                'In the past 6 months, how much of a problem has your child had with school functioning: - Missing school because of not feeling well': 'carer_school_missing_unwell',
                'In the past 6 months, how much of a problem has your child had with school functioning: - Missing school to go to the doctor / hospital': 'carer_school_missing_doctor',
                'In the past 6 months, how much of a problem has your child had with school functioning: - Paying attention in class': 'carer_school_attention',
                'In the past 6 months, how much of a problem has your child had with social functioning: - Getting along with other children': 'carer_social_get_along_others',
                'In the past 6 months, how much of a problem has your child had with social functioning: - Getting teased by other children': 'carer_social_teasing',
                'In the past 6 months, how much of a problem has your child had with social functioning: - Keeping up when playing with other children': 'carer_social_keep_up',
                'In the past 6 months, how much of a problem has your child had with social functioning: - Not able to do things that other children his or her age can do': 'carer_social_inability',
                'In the past 6 months, how much of a problem has your child had with social functioning: - Other kids not wanting to be his or her friend': 'carer_social_no_friends',
                'In the past 6 months, how much of a problem have you had with getting along with others: - I cannot do things that other kids my age can do': 'child_social_inability',
                'In the past 6 months, how much of a problem have you had with getting along with others: - I have trouble getting along with other kids': 'child_social_get_along_others',
                'In the past 6 months, how much of a problem have you had with getting along with others: - It is hard to keep up when I play with other kids': 'child_social_keep_up',
                'In the past 6 months, how much of a problem have you had with getting along with others: - Other kids do not want to be my friend': 'child_social_no_friends',
                'In the past 6 months, how much of a problem have you had with getting along with others: - Other kids tease me': 'child_social_teasing',
                'In the past 6 months, how much of a problem have you had with your feelings: - I feel afraid or scared': 'child_emotion_afraid',
                'In the past 6 months, how much of a problem have you had with your feelings: - I feel angry': 'child_emotion_angry',
                'In the past 6 months, how much of a problem have you had with your feelings: - I feel sad or blue': 'child_emotion_sad',
                'In the past 6 months, how much of a problem have you had with your feelings: - I have trouble sleeping': 'child_emotion_insomnia',
                'In the past 6 months, how much of a problem have you had with your feelings: - I worry about what will happen to me': 'child_emotion_worry',
                'In the past 6 months, how much of a problem have you had with your school: - I forget things': 'child_school_forget',
                'In the past 6 months, how much of a problem have you had with your school: - I have trouble keeping up with my schoolwork': 'child_school_school_work',
                'In the past 6 months, how much of a problem have you had with your school: - I miss school because of not feeling well': 'child_school_missing_unwell',
                'In the past 6 months, how much of a problem have you had with your school: - I miss school to go to the doctor or hospital': 'child_school_missing_doctor',
                'In the past 6 months, how much of a problem have you had with your school: - It is hard to pay attention in class': 'child_school_attention',
                'Dietary Recall Diary\n\n\n\nThis diary records what your child has eaten in the last 3 days. Please list your child\'s food and drink below. \n\n\n\nNOTE: please separate each food with a comma e.g. "apple, banana, oranges"\n\n \nPlease record what your child ate and drank 3 days ago on [OtherDate-DM--3%20day] - Breakfast': '3D_breakfast',
                'Dietary Recall Diary\n\n\n\nThis diary records what your child has eaten in the last 3 days. Please list your child\'s food and drink below. \n\n\n\nNOTE: please separate each food with a comma e.g. "apple, banana, oranges"\n\n \nPlease record what your child ate and drank 3 days ago on [OtherDate-DM--3%20day] - Dinner': '3D_dinner',
                'Dietary Recall Diary\n\n\n\nThis diary records what your child has eaten in the last 3 days. Please list your child\'s food and drink below. \n\n\n\nNOTE: please separate each food with a comma e.g. "apple, banana, oranges"\n\n \nPlease record what your child ate and drank 3 days ago on [OtherDate-DM--3%20day] - Lunch': '3D_lunch',
                'Dietary Recall Diary\n\n\n\nThis diary records what your child has eaten in the last 3 days. Please list your child\'s food and drink below. \n\n\n\nNOTE: please separate each food with a comma e.g. "apple, banana, oranges"\n\n \nPlease record what your child ate and drank 3 days ago on [OtherDate-DM--3%20day] - Snack': '3D_snack',
                'Please recall what your child ate and drank yesterday on [OtherDate-DM--1%20day] - Breakfast': '1D_breakfast',
                'Please recall what your child ate and drank yesterday on [OtherDate-DM--1%20day] - Dinner': '1D_dinner',
                'Please recall what your child ate and drank yesterday on [OtherDate-DM--1%20day] - Lunch': '1D_lunch',
                'Please recall what your child ate and drank yesterday on [OtherDate-DM--1%20day] - Snack': '1D_snack',
                'Please record what your child ate and drank 2 days ago on [OtherDate-DM--2%20day] - Breakfast': '2D_breakfast',
                'Please record what your child ate and drank 2 days ago on [OtherDate-DM--2%20day] - Dinner': '2D_dinner',
                'Please record what your child ate and drank 2 days ago on [OtherDate-DM--2%20day] - Lunch': '2D_lunch',
                'Please record what your child ate and drank 2 days ago on [OtherDate-DM--2%20day] - Snack': '2D_snack'
            }
        )
        #FILL ANY BLANKS
        .replace("",np.nan) 
    )


    # CONVERT DATE COLUMN TO DATETIME TYPE
    df['recorded_date'] = pd.to_datetime(df['recorded_date'])

    # SORT VALUES ACCORDING TO START DATE
    df = df.sort_values(by=['QIPID','recorded_date']).reset_index(drop=True)

    # CALCULATE NUMBER OF DAYS SINCE STARTING TREATMENT
    df['time'] = df.groupby('QIPID')['recorded_date'].diff().fillna(pd.Timedelta(seconds=0))

    # JUST GET THE NUMBER OF DAYS FROM THE TIMEDELTA
    df['time'] = df.apply(lambda x: x['time'].days,axis=1)

    # DROP NA ON TIME
    df = df.dropna(subset=['time'])

    # CONVERT TIME TO INT
    df['time'] = df['time'].astype(int)

    # CONVERT DATETIME TO JUST DATE
    df['recorded_date'] = df['recorded_date'].dt.strftime("%d-%m-%Y")

    # # MAKE BINS FOR DATE PER WEEK
    bins = [x for x in range(0,df.time.max()+8) if x%7 == 0]
    labels = [y+1 for y in range(len(bins))][:-1]
    df['week'] = pd.cut(df['time'],bins=bins, labels=labels, include_lowest=True).astype(int)

    # convert recorded date to datetime
    df['recorded_date'] = pd.to_datetime(df['recorded_date'], infer_datetime_format=True)

    return df

# CSBM DF
def make_csbm_df_function(qipid='ALL', df=clean_df(df)):
    #MAKE COPY OF DF
    csbm_df = df.copy()

    if qipid != 'ALL':
        csbm_df = csbm_df[csbm_df["QIPID"]==qipid]

    # SELECT CORRECT COLUMNS 
    csbm_df=csbm_df.loc[:, ['recorded_date','QIPID','csbm','bristol_stool_chart','time','week']]

    before_csbm_df_size = csbm_df.shape[0]

    # REMOVE NA VALUES CSBM
    csbm_df = csbm_df.dropna(axis=0)
    num_dropped=before_csbm_df_size - csbm_df.shape[0]
    print(f"CSBM:{num_dropped} data points have been dropped due to NA")

      # MAP ORIGINAL RESPONSE VALUES FOR CSBM TO NUMERICAL
    csbm_df['csbm'] = csbm_df['csbm'].map({
        'More than 1 every day':9,
        'Only 1 every day':8,
        'Once every 2 days':7,
        'Once every 3 days':6,
        'Once every 4 days':5,
        'Once every 5 days':4,
        'Once every 6 days':3,
        'Once every 7 days':2,
        'Less than once every 7 days':1
    })

    # REMOVE 'TYPE' FROM BRISTOL STOOL CHART ANSWERS TO SET TO INT
    csbm_df['bristol_stool_chart'] = csbm_df['bristol_stool_chart'].str.replace('Type ','').astype(int)

    #ORDER DATAFRAME BY BRISTOL STOOL SCORE
    csbm_df.sort_values(by='bristol_stool_chart',inplace=True)

     # SORT VALUES ACCORDING TO START DATE
    csbm_df = csbm_df.sort_values(by=['QIPID','recorded_date']).reset_index(drop=True)



    return csbm_df, num_dropped

# ST MARK SCORE FUNCTION
def make_sms_df(qipid='ALL', df=clean_df(df)):

    #MAKE COPY OF DF
    sms_df = df.copy()

    if qipid != 'ALL':
        sms_df = sms_df[sms_df["QIPID"]==qipid]
    
    # Select correct columns
    sms_df = sms_df.loc[:, ['recorded_date', 
                          'QIPID',
                          'SM_solid',
                          'SM_liquid', 
                          'SM_gas', 
                          'SM_activity_change', 
                          'SM_pad',
                          'SM_constipation_med',
                          'SM_inability_stool_15min',
                          'time'
                          ]]

    # COUNT HOW MANY ENTRIES DROPPED DUE TO NA
    before_sms_df_size = sms_df.shape[0]
    sms_df.dropna(inplace=True)
    num_dropped = before_sms_df_size - sms_df.shape[0]
    print(f"SMS: Dropped {num_dropped} due to NA.")

    #MAP THE RESPONSE TO THE APPROPRIATE VALUE SOLID AND LIQUID
    for col in sms_df.loc[:,['SM_solid','SM_liquid']]:

        sms_df[col] = sms_df[col].replace(
            {
            'Never':0,
            'Less than 1 per month':0.1,
            'More than 1 per month':0.2,
            'Weekly':0.5,
            'Daily':1
            }
        )

    # GAS AND SOCIAL ACTIVITY
    for col in sms_df.loc[:,['SM_gas', 'SM_activity_change']]:

        sms_df[col] = sms_df[col].replace(
            {
            'Never':0,
            'Less than 1 per month':0.1,
            'More than 1 per month':0.2,
            'Weekly':0.1,
            'Daily':0.1
            }
        )

    # INCONTINCENCE
    for col in sms_df.loc[:,['SM_inability_stool_15min']]:

        sms_df[col] = sms_df[col].replace(
            {
            'Yes' : 4 ,
            'No' : 0
            }
        )
    
    # NAPPY, MEDS
    for col in sms_df.loc[:,['SM_pad', 'SM_constipation_med']]:

        sms_df[col] = sms_df[col].replace(
            {
            'Yes' : 2,
            'No' : 0
            }
        )

    # CALCULATE TOTAL SCORE
    sms_df['total_score'] = sms_df[['SM_solid', 'SM_liquid', 'SM_gas',
       'SM_activity_change', 'SM_pad', 'SM_constipation_med',
       'SM_inability_stool_15min']].apply(lambda x: x.sum(),axis=1)

    def sm_score_col_func(x):
        if x <= 2.6:
            return 'green'
        elif x > 5.2:
            return 'red'
        else:
            return 'amber'

    # MAP SCORE TO COLOUR VALUE
    sms_df['score_colour'] = sms_df.total_score.apply(sm_score_col_func)

    # print(sms_df.columns)

    # SORT VALUES ACCORDING TO START DATE
    sms_df = sms_df.sort_values(by=['QIPID','recorded_date']).reset_index(drop=True)


    return sms_df, num_dropped

#DACT DF
def make_dact_df_function(qipid='ALL', df=clean_df(df)):

  #MAKE COPY OF DF
  dact_df = df.copy()

  if qipid != 'ALL':
    dact_df = dact_df[dact_df["QIPID"]==qipid]

  # SELECT CORRECT COLUMNS 
  dact_df=dact_df.loc[:, ['time', 'week','recorded_date','QIPID','daily_routine_7d', 'daily_routine_6d','daily_routine_5d', 'daily_routine_4d', 'daily_routine_3d','daily_routine_2d', 'daily_routine_1d', 'daily_routine_0d']]

  before_dact_df_size = dact_df.shape[0]

  # REMOVE NA VALUES CSBM
  dact_df = dact_df.dropna(axis=0)
  num_dropped = before_dact_df_size - dact_df.shape[0]
  print(f"DAILY ACTIVITY:{num_dropped} data points have been dropped due to NA")

  # function to calculate score
  def calculate_daily_routine_score(x):

    # CREATE COUNTER OBJECT TO COUNT EACH REPORTED ACTIVITY
    daily_activity_list = Counter(x.split(','))

    # ITERATE THROUGH COUNTER LIST TO MAP SOILING TO -3
    for x in daily_activity_list:
      if x == 'Any soiling?':
        daily_activity_list[x] = -3

    # CALCULATE AND RETURN SUM
    return sum(daily_activity_list.values())

  # MAKE SCORE COLUMNS
  for daily_routine_col in dact_df.columns[4:]:

    dact_df["score_"+str(daily_routine_col)] = dact_df.apply(lambda x: calculate_daily_routine_score(x[daily_routine_col]), axis=1)
    
  # CALCULATE TOTAL SCORE
  dact_df['total_score_daily_routine'] = dact_df.iloc[:,12:].apply(lambda x: x.sum(), axis=1)

  def dact_score_col_func(x):
    if x == 40:
      return 'green'
    elif 35 <= x < 50:
      return 'amber'
    else:
      return 'red'

  # CALCULATE TOTAL SCORE
  dact_df['colour'] = dact_df.apply(lambda x: dact_score_col_func(x['total_score_daily_routine']), axis=1)

  # REARRANGE COLUMNS
  dact_df = dact_df[['recorded_date',
                    'QIPID',
                    'total_score_daily_routine',
                      'time',
                     'colour',
                      'week',
                    'daily_routine_7d',
                    'daily_routine_6d',
                    'daily_routine_5d',
                    'daily_routine_4d',
                    'daily_routine_3d',
                    'daily_routine_2d',
                    'daily_routine_1d',
                    'daily_routine_0d',
                    'score_daily_routine_7d',
                    'score_daily_routine_6d',
                    'score_daily_routine_5d',
                    'score_daily_routine_4d',
                    'score_daily_routine_3d',
                    'score_daily_routine_2d',
                    'score_daily_routine_1d',
                    'score_daily_routine_0d',
                    ]]

  return dact_df, num_dropped