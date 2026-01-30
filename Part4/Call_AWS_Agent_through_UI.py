import streamlit as st
import boto3
import uuid

# Initialize Bedrock Agent Runtime client
bedrock_agent_runtime = boto3.client(service_name='bedrock-agent-runtime')

# Replace with your Agent ID and Alias ID
agent_id = 'M1WVZ52PBV'
agent_alias_id = 'BME9YBJ7UK'

# Initialize session ID in session state
if 'session_id' not in st.session_state:
    st.session_state['session_id'] = str(uuid.uuid4())

# Streamlit UI
st.title("Bedrock Agent Chat")

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Display chat messages from history
for message in st.session_state['chat_history']:
    if message['role'] == 'user':
        st.text(f"You: {message['content']}")
    else:
        st.text(f"Agent: {message['content']}")

# Input field for user message
user_input = st.text_input("Type your message:")

if st.button("Send"):
    if user_input:
        # Add user message to chat history
        st.session_state['chat_history'].append({'role': 'user', 'content': user_input})
    try:
            # Invoke the agent
            response = bedrock_agent_runtime.invoke_agent(
                agentId=agent_id,
                agentAliasId=agent_alias_id,
                inputText=user_input,
                sessionId=st.session_state['session_id']
            )

            # Extract agent's response
            event_stream = response["completion"]
            full_response = ""

            for event in event_stream:
                if 'chunk' in event:
                    full_response += event['chunk']['bytes'].decode('utf-8')
                elif 'trace' in event:
                    trace_data = event['trace']
                    if 'traceType' in trace_data and trace_data['traceType'] == 'AGENT_ORCHESTRATION':
                        if 'orchestrationSteps' in trace_data:
                            for step in trace_data['orchestrationSteps']:
                                if 'agentAction' in step and 'agentActionType' in step['agentAction'] and step['agentAction']['agentActionType'] == 'RETURN_FINAL_RESPONSE':
                                    if 'agentActionOutput' in step['agentAction']:
                                        full_response += step['agentAction']['agentActionOutput']['finalResponse']
                                    elif 'agentActionOutput' in step['agentAction'] and 'invokeModelResponse' in step['agentAction']['agentActionOutput'] and 'outputText' in step['agentAction']['agentActionOutput']['invokeModelResponse']:
                                        full_response += step['agentAction']['agentActionOutput']['invokeModelResponse']['outputText']
            # Add agent's response to chat history
            st.session_state['chat_history'].append({'role': 'agent', 'content': full_response})
    except Exception as e:
            st.error(f"An error occurred: {e}")
            st.session_state['chat_history'].append({'role': 'agent', 'content': f"Error: {e}"})
    # Rerun to update the chat display
    st.rerun()






