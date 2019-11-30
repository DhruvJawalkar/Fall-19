
# coding: utf-8

# In[36]:


import requests
import json

def write_to_file(fn, data):
    with open(fn, 'w') as outfile:
        json.dump(data, outfile)

def read_from_file(fn):
    with open(fn) as json_file:
        data = json.load(json_file)
    return data    

def query_q1():
    r_all = requests.get(url="https://chroniclingamerica.loc.gov/newspapers.json")
    data_all = r_all.json()
    
    write_to_file("1.json", data_all)
    return data_all

data_all = read_from_file("1.json")
print("Total number of newspapers: ", len(data_all["newspapers"]))
print("\n")
state_wise_count = {}

for item in data_all["newspapers"]:
    if(item["state"] not in state_wise_count):
        state_wise_count[item["state"]] = 1
    else:    
        state_wise_count[item["state"]] += 1
    
states = list(state_wise_count.keys())
counts = list(state_wise_count.values())
idx_of_state_with_min_publications = counts.index(min(counts))
idx_of_state_with_max_publications = counts.index(max(counts))

state_with_min_publications = states[idx_of_state_with_min_publications]
state_with_max_publications = states[idx_of_state_with_max_publications]

print("State with the highest number of publications,", state_with_max_publications+" :",counts[idx_of_state_with_max_publications])
print("\n")
print("State with the least number of publications,", state_with_min_publications+" :",counts[idx_of_state_with_min_publications])
print("\n")
print("Alabama, total number of newspapers:", state_wise_count["Alabama"])
print("\n")

my_state = "Oregon"
print("Total number of newspapers for my state, "+my_state+" :", state_wise_count[my_state])
print("\n")

def save_all_newspaper_info_for_q5(data_all, my_state):
    state_papers = []
    result = []
    for paper in data_all["newspapers"]:
        if(paper["state"]==my_state):
            state_papers.append(paper)
            r = requests.get(url=paper["url"])
            data = r.json()
            result.append({"title":paper["title"],"start_year":data["start_year"], "issues": len(data["issues"])})
            
    write_to_file("5.json", state_papers)
    write_to_file("5-result.json", result)
    return state_papers

oregon_papers = read_from_file("5-result.json")
for item in oregon_papers:
    print(item["title"]," Start year:", item["start_year"], "Issues:", item["issues"])

def query_all_newspaper_info_for_q6(data_all):
    result = []
    for paper in data_all["newspapers"]:
        r = requests.get(url=paper["url"])
        data = r.json()
        result.append({"title":paper["title"],"start_year":data["start_year"]})
            
    write_to_file("6.json", result)
    return result    
all_papers = read_from_file("6.json")

def get_replacement_position(start_year, top5_start_year):
    i = 5-1  
    while(start_year<top5_start_year[i] and i>0):
        i-=1
    return i

def get_updated_top_5_results(idx, start_year, item, top5_start_year, top5):
    if(idx==0):
        top5_start_year = [start_year] + top5_start_year[:-1]
        top5 = [{'title' : item["title"], 'start_year' : int(item["start_year"])}] + top5[:-1]     
        
    elif(idx<4):
        top5_start_year = top5_start_year[:idx+1] + [start_year] + top5_start_year[idx+1:-1]
        top5 = top5[:idx+1] + [{'title' : item["title"], 'start_year' : int(item["start_year"])}] + top5[idx+1:-1]     
    return top5_start_year, top5

print("\n")
print("=================================")
def get_top5(all_papers):
    top5 = [{}, {}, {}, {}, {}]
    top5_start_year = [2019, 2019, 2019, 2019, 2019]

    for item in all_papers:
        try:
            start_year = int(item["start_year"])
        except:
            start_year = 2019
        print(start_year)    
        idx = get_replacement_position(start_year, top5_start_year)
        top5_start_year, top5 = get_updated_top_5_results(idx, start_year, item, top5_start_year, top5)
    
    return top5_start_year, top5


top5 = read_from_file("top5-results.json")
print("Printing top 5 publications with the earliest start years:\n")

for result in top5:
    print(result["title"]+" - "+str(result["start_year"]))

