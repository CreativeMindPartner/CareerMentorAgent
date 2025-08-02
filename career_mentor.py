# Career Mentor Agent
def career_advice(job_role):
    if job_role.lower() == "developer":
        return "Learn Python, JavaScript, and practice coding on platforms like LeetCode."
    elif job_role.lower() == "designer":
        return "Master tools like Figma, Adobe XD, and focus on UI/UX principles."
    else:
        return "Explore your interests and take online courses to build relevant skills."

# Test the function
user_input = input("Enter your desired job role (e.g., developer, designer): ")
print(career_advice(user_input))