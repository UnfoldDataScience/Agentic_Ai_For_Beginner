def lambda_handler(event, context):
    agent = event['agent']
    actionGroup = event['actionGroup']
    function = event['function']
    parameters = event.get('parameters', [])

    paramDict = {item['name']: item['value'] for item in parameters}

    years_experience = int(paramDict.get('years_experience', 0)) #Default 0 if not given.
    course_interest = paramDict.get('course_interest', "")

    recommended_course = ""

    if years_experience <= 2:
        recommended_course = "Data Science Fundamentals"
    elif 3 <= years_experience <= 5:
        recommended_course = "Intermediate Machine Learning"
    elif years_experience > 5:
        recommended_course = "Advanced Deep Learning and AI"

    if "specific course name" in course_interest.lower(): #you can add more course names here.
        recommended_course = "Specific course name" #overwrite if they mention a specific course.

    responseBody = {
        "TEXT": {
            "body": recommended_course
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