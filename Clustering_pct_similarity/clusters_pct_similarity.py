import os

def read_txt(filename):
    '''read in text file, return as list'''
    with open(filename) as f:
        var_name = f.read().splitlines()
        
    return var_name

def calculate_percent_overlap(list1, list2):
    '''accepts two lists, counts how many index locations contain same value,
    calculates % similarity using fact that each list is 57508 elements long '''
    counter = 0
    for vertex, item in enumerate(list1):
        if item == list2[vertex]:
            counter += 1
    
    return round((counter/57508) * 100, 2)


def main():
    #set base path
    base_path = '/Users/daliak/Downloads/Newtextfiles'
   
    #read in all kmeans .txt results 
    subj1_sess1_k5 = read_txt(f"{base_path}/P1S1_match5.txt")
    subj1_sess1_k10 = read_txt(f"{base_path}/P1S1_match10.txt")
    subj1_sess1_k20 = read_txt(f"{base_path}/P1S1_match20.txt")
    subj1_sess1_k50 = read_txt(f"{base_path}/P1S1_match50.txt")
    subj1_sess2_k5 = read_txt(f"{base_path}/P1S2_match5.txt")
    subj1_sess2_k10 = read_txt(f"{base_path}/P1S2_match10.txt")
    subj1_sess2_k20 = read_txt(f"{base_path}/P1S2_match20.txt")
    subj1_sess2_k50 = read_txt(f"{base_path}/P1S2_match50.txt")
    subj2_sess1_k5 = read_txt(f"{base_path}/P2S1_match5.txt")
    subj2_sess1_k10 = read_txt(f"{base_path}/P2S1_match10.txt")
    subj2_sess1_k20 = read_txt(f"{base_path}/P2S1_match20.txt")
    subj2_sess1_k50 = read_txt(f"{base_path}/P2S1_match50.txt")
    subj2_sess2_k5 = read_txt(f"{base_path}/P2S2_match5.txt")
    subj2_sess2_k10 = read_txt(f"{base_path}/P2S2_match10.txt")
    subj2_sess2_k20 = read_txt(f"{base_path}/P2S2_match20.txt")
    subj2_sess2_k50 = read_txt(f"{base_path}/P2S2_match50.txt")

    #within subject percent overlap calc
    #separated by k 
    P1S1_vs_P1S2_k5 = calculate_percent_overlap(subj1_sess1_k5, subj1_sess2_k5)
    P1S1_vs_P1S2_k10 = calculate_percent_overlap(subj1_sess1_k10, subj1_sess2_k10)
    P1S1_vs_P1S2_k20 = calculate_percent_overlap(subj1_sess1_k20, subj1_sess2_k20)
    P1S1_vs_P1S2_k50 = calculate_percent_overlap(subj1_sess1_k50, subj1_sess2_k50)

    P2S1_vs_P2S2_k5 = calculate_percent_overlap(subj2_sess1_k5, subj2_sess2_k5)
    P2S1_vs_P2S2_k10 = calculate_percent_overlap(subj2_sess1_k10, subj2_sess2_k10)
    P2S1_vs_P2S2_k20 = calculate_percent_overlap(subj2_sess1_k20, subj2_sess2_k20)
    P2S1_vs_P2S2_k50 = calculate_percent_overlap(subj2_sess1_k50, subj2_sess2_k50)

    #between subject percent overlap calc
    #separated by k 
    P1S1_vs_P2S1_k5 = calculate_percent_overlap(subj1_sess1_k5, subj2_sess1_k5)
    P1S1_vs_P2S2_k5 = calculate_percent_overlap(subj1_sess1_k5, subj2_sess2_k5)
    P1S2_vs_P2S1_k5 = calculate_percent_overlap(subj1_sess2_k5, subj2_sess1_k5)
    P1S2_vs_P2S2_k5 = calculate_percent_overlap(subj1_sess2_k5, subj2_sess2_k5)

    P1S1_vs_P2S1_k10 = calculate_percent_overlap(subj1_sess1_k10, subj2_sess1_k10)
    P1S1_vs_P2S2_k10 = calculate_percent_overlap(subj1_sess1_k10, subj2_sess2_k10)
    P1S2_vs_P2S1_k10 = calculate_percent_overlap(subj1_sess2_k10, subj2_sess1_k10)
    P1S2_vs_P2S2_k10 = calculate_percent_overlap(subj1_sess2_k10, subj2_sess2_k10)

    P1S1_vs_P2S1_k20 = calculate_percent_overlap(subj1_sess1_k20, subj2_sess1_k20)
    P1S1_vs_P2S2_k20 = calculate_percent_overlap(subj1_sess1_k20, subj2_sess2_k20)
    P1S2_vs_P2S1_k20 = calculate_percent_overlap(subj1_sess2_k20, subj2_sess1_k20)
    P1S2_vs_P2S2_k20 = calculate_percent_overlap(subj1_sess2_k20, subj2_sess2_k20)

    P1S1_vs_P2S1_k50 = calculate_percent_overlap(subj1_sess1_k50, subj2_sess1_k50)
    P1S1_vs_P2S2_k50 = calculate_percent_overlap(subj1_sess1_k50, subj2_sess2_k50)
    P1S2_vs_P2S1_k50 = calculate_percent_overlap(subj1_sess2_k50, subj2_sess1_k50)
    P1S2_vs_P2S2_k50 = calculate_percent_overlap(subj1_sess2_k50, subj2_sess2_k50)
    
    #calculates average from all within % overlaps (all ks)
    avg_within = round((P1S1_vs_P1S2_k5 + P1S1_vs_P1S2_k10 + P1S1_vs_P1S2_k20 + 
    P1S1_vs_P1S2_k50 + P2S1_vs_P2S2_k5 + P2S1_vs_P2S2_k10 + P2S1_vs_P2S2_k20 + P2S1_vs_P2S2_k50)/8, 2)

    #calculates average from all between % overlaps (all ks)
    avg_between = round((P1S1_vs_P2S1_k5 + P1S1_vs_P2S2_k5 + P1S2_vs_P2S1_k5 + P1S2_vs_P2S2_k5 +
    P1S1_vs_P2S1_k10 + P1S1_vs_P2S2_k10 + P1S2_vs_P2S1_k10 + P1S2_vs_P2S2_k10 +
    P1S1_vs_P2S1_k20 + P1S1_vs_P2S2_k20 + P1S2_vs_P2S1_k20 + P1S2_vs_P2S2_k20 + 
    P1S1_vs_P2S1_k50 + P1S1_vs_P2S2_k50 + P1S2_vs_P2S1_k50 + P1S2_vs_P2S2_k50)/16, 2)

    #create dictionaries w/ results
    within_dict_k5 =  {
        "P1S1_vs_P1S2_k5": P1S1_vs_P1S2_k5, 
        "P2S1_vs_P2S2_k5":  P2S1_vs_P2S2_k5}
        
    within_dict_k10 =  {
        "P1S1_vs_P1S2_k10": P1S1_vs_P1S2_k10, 
        "P2S1_vs_P2S2_k10":  P2S1_vs_P2S2_k10}

    within_dict_k20 =  {
        "P1S1_vs_P1S2_k20":  P1S1_vs_P1S2_k20,
        "P2S1_vs_P2S2_k20": P2S1_vs_P2S2_k20}

    within_dict_k50 =  {
        "P1S1_vs_P1S2_k50": P1S1_vs_P1S2_k50,
        "P2S1_vs_P2S2_k50": P2S1_vs_P2S2_k50}

    between_dict_k5 = {
    "P1S1_vs_P2S1_k5": P1S1_vs_P2S1_k5, 
    "P1S1_vs_P2S2_k5": P1S1_vs_P2S2_k5, 
    "P1S2_vs_P2S1_k5": P1S2_vs_P2S1_k5, 
    "P1S2_vs_P2S2_k5": P1S2_vs_P2S2_k5}

    between_dict_k10 = {
    "P1S1_vs_P2S1_k10": P1S1_vs_P2S1_k10, 
    "P1S1_vs_P2S2_k10": P1S1_vs_P2S2_k10, 
    "P1S2_vs_P2S1_k10": P1S2_vs_P2S1_k10, 
    "P1S2_vs_P2S2_k10": P1S2_vs_P2S2_k10}

    between_dict_k20 = {
    "P1S1_vs_P2S1_k20": P1S1_vs_P2S1_k20,
    "P1S1_vs_P2S2_k20": P1S1_vs_P2S2_k20, 
    "P1S2_vs_P2S1_k20": P1S2_vs_P2S1_k20, 
    "P1S2_vs_P2S2_k20": P1S2_vs_P2S2_k20} 

    between_dict_k50 = {
    "P1S1_vs_P2S1_k50": P1S1_vs_P2S1_k50, 
    "P1S1_vs_P2S2_k50": P1S1_vs_P2S2_k50, 
    "P1S2_vs_P2S1_k50": P1S2_vs_P2S1_k50, 
    "P1S2_vs_P2S2_k50": P1S2_vs_P2S2_k50}

    #create string with all results for output as .txt
    results = f'''
    Avg_within_pct_similarity:{avg_within} 
    Avg_between_pct_similarity:{avg_between} 
    \n\nWITHIN_K=5 \n {within_dict_k5} \n\n WITHIN_K=10 \n {within_dict_k10} \n\n WITHIN_K=20 \n {within_dict_k20} \n\n WITHIN_K=50 \n {within_dict_k50} 
    \n\n BETWEEN_K=5\n {between_dict_k5} \n\nBETWEEN_K=10\n {between_dict_k10} \n\nBETWEEN_K=20\n {between_dict_k20} \n\nBETWEEN_K=50\n {between_dict_k50}'''
    print(results)
    
    #write to .txt file & format
    outputFile = open( "percent_similarity.txt", "w")
    outputFile.write(str(results))
    outputFile.flush()
    outputFile.close()


if __name__ == '__main__':
    main()



