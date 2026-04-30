def generate_report(data):
    status = "Pass" if data["marks"] >= 50 else "Fail"

    report = f"""
Student Name : {data['student_name']}
Course       : {data['course']}
Marks        : {data['marks']}
Status       : {status}
"""
    return report
