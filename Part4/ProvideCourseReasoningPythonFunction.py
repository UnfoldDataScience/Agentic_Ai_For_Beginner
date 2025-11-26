def lambda_handler(event, context):
    agent = event['agent']
    actionGroup = event['actionGroup']
    function = event['function']
    parameters = event.get('parameters', [])

    paramDict = {item['name']: item['value'] for item in parameters}

    years_experience = int(paramDict.get('years_experience', 0))
    course_interest = paramDict.get('course_interest', "")
    recommended_course = paramDict.get('recommended_course', "") #From first action group.

    reasoning = ""

    if recommended_course == "Data Science Fundamentals":
        reasoning = f"Given your {years_experience} years of experience, the Data Science Fundamentals course will provide you with a strong foundation in essential concepts like Python, data manipulation, and basic machine learning. It's perfect for beginners looking to start their data science journey."
    elif recommended_course == "Intermediate Machine Learning":
        reasoning = f"With {years_experience} years of experience, you're ready to dive deeper into machine learning. Our Intermediate Machine Learning course covers advanced algorithms, model evaluation, and practical project work to enhance your skills."
    elif recommended_course == "Advanced Deep Learning and AI":
        reasoning = f"Your {years_experience} years of experience make you well-suited for our Advanced Deep Learning and AI course. You'll learn cutting-edge techniques in neural networks, deep learning frameworks, and AI applications, preparing you for complex real-world challenges."
    elif recommended_course == "Specific course name":
        reasoning = f"The specific course name course is highly relevant, given your experience and interest in {course_interest}. This course covers [specific topics] and will help you achieve [specific goals]."
    else:
        reasoning = "I need more information to give you specific reasoning."

    responseBody = {
        "TEXT": {
            "body": reasoning
        }
    }

    action_response = {
        'actionGroup': actionGroup,
        'function': function,
        'functionResponse': {
            'responseBody': responseBody
        }
    }

    dummy_function_response = {'response': action_response, 'messageVersion': event['messageVersion']}
    print("Response: {}".format(dummy_function_response))

    return dummy_function_response