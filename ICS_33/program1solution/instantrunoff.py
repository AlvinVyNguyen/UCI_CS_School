import goody

def read_voter_preferences(open_file : open):
    votes = dict()
    for line in open_file:
        entry = line.rstrip().split(';')
        votes[entry[0]] = entry[1:]
    open_file.close()
    return votes


def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
#     answer = ''
#     for k in sorted(d,key=key,reverse=reverse):
#         answer += '  '+str(k)+' -> '+str(d[k])+'\n'
#     return answer
    return '\n'.join('  '+str(k)+' -> '+str(d[k]) for k in sorted(d,key=key,reverse=reverse))+'\n'


def evaluate_ballot(vp : {str:[str]}, cie : {str}) -> {str:int}:
    vd = {c : 0 for c in cie} # defaultdict(int)
    for clist in vp.values():
        for c in clist:
            if c in cie:
                vd[c] += 1
                break
    return vd


def remaining_candidates(vd : {str:int}) -> {str}:
    min_votes = min(vd.values())
    return {c for c in vd if (vd[c] > min_votes)}       


def run_election(vp_file : open) -> {str}:
    vp = read_voter_preferences(vp_file)
    print('Voter Preferences\n'+dict_as_str(vp,lambda k : k))
    cie = {c for cs in vp.values() for c in cs}     
    
    ballot = 1
    while len(cie) > 1:
        vd = evaluate_ballot(vp,cie)
        print('Vote count on ballot #' +str(ballot) + ' with candidates (alphabetically) = ' + str(cie)+'\n'+dict_as_str (vd))
        print('Vote count on ballot #' +str(ballot) + ' with candidates (numerical)      = ' + str(cie)+'\n'+dict_as_str (vd,lambda x : vd[x],True))
        cie = remaining_candidates(vd)
        ballot += 1
    if len(cie) == 1:
        print('Winner is ',cie)
    else:
        print('No winner: election is a tie among the candidates remaining on the last ballot')
    return cie
  
  
  
  
    
if __name__ == '__main__':
    pref_file = goody.safe_open('Enter file with voter preferences', 'r', 'Could not find that file')
    print()
    run_election(pref_file)
    
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
