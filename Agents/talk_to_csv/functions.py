from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
import pandas as pd
import glob
import json
from datetime import datetime

def save_chart(query):
    q_s = ' If any charts or graphs or plots were created save them localy and include the save file names in your response.'
    query += ' . '+ q_s
    return query

def save_uploaded_file(uploaded_file):
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
    df_arr, df_arr_names = load_dataframe()

    agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df_arr, return_intermediate_steps=True, save_charts=True, verbose=True)
    return agent, df_arr, df_arr_names

def load_dataframe():
  selected_df = []

  all_files_csv = glob.glob("*.csv")
  all_files_xlsx = glob.glob("*.xlsx")
  all_files_xls = glob.glob("*.xls")
  for filename in all_files_csv:
      df = pd.read_csv(filename)
      selected_df.append(df)
  for filename in all_files_xlsx:
      df = pd.read_excel(filename)
      selected_df.append(df)
  for filename in all_files_xls:
      df = pd.read_excel(filename)
      selected_df.append(df)
  selected_df_names = all_files_csv + all_files_xlsx + all_files_xls
  return selected_df, selected_df_names

def run_query(agent, query_):
    if 'chart' or 'charts' or 'graph' or 'graphs' or 'plot' or 'plt' in query_:
        query_ = save_chart(query_)
    output = agent(query_)
    response, intermediate_steps = output['output'], output['intermediate_steps']
    thought, action, action_input, observation, steps = decode_intermediate_steps(intermediate_steps)
    store_convo(query_, steps, response)
    return response, thought, action, action_input, observation

def decode_intermediate_steps(steps):
    log, thought_, action_, action_input_, observation_ = [], [], [], [], []
    text = ''
    
    for step in steps:
        # Add debug prints to understand the structure of step
        print(f"Step: {step}")
        if not isinstance(step, list) or len(step) < 2:
            print(f"Invalid step structure: {step}")
            continue
        if not isinstance(step[0], list) or len(step[0]) < 3:
            print(f"Invalid step[0] structure: {step[0]}")
            continue
        
        thought_text = step[0][2].split('Action:')[0] if 'Action:' in step[0][2] else step[0][2]
        action_text = step[0][2].split('Action:')[1].split('Action Input:')[0] if 'Action:' in step[0][2] and 'Action Input:' in step[0][2] else step[0][2]
        action_input_text = step[0][2].split('Action Input:')[1] if 'Action Input:' in step[0][2] else step[0][2]
        observation_text = step[1]
        
        thought_.append(':green[{}]'.format(thought_text))
        action_.append(':green[Action:] {}'.format(action_text))
        action_input_.append(':green[Action Input:] {}'.format(action_input_text))
        observation_.append(':green[Observation:] {}'.format(observation_text))
        log.append(step[0][2])
        text = step[0][2] + ' Observation: {}'.format(observation_text)
    
    return thought_, action_, action_input_, observation_, text


def get_convo():
    convo_file = 'convo_history.json'
    with open(convo_file, 'r',encoding='utf-8') as f:
        data = json.load(f)
    return data, convo_file

def store_convo(query, response_, response):
    data, convo_file = get_convo()
    current_dateTime = datetime.now()
    data['{}'.format(current_dateTime)] = []
    data['{}'.format(current_dateTime)].append({'Question': query, 'Answer':response, 'Steps':response_})
    
    with open(convo_file, 'w',encoding='utf-8') as f:
        json.dump(data, f,ensure_ascii=False, indent=4)