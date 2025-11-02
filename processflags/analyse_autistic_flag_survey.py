import numpy as np
import doctest
import drawsvg
from os.path import exists
import copy
import json

EXAMPLE_ROW = 8 # an early participant who does not appear to be updating their responses as new flags are added

SENTINEL = 'sentinel'
STRONG_AGREE = 5

def read_data():
    """
    Read the data into a 2D list, don't worry about converting to int/float.
    :return: a list of lists, and the headers
    >>> dat, header = read_data()
    >>> '5' in dat[0]
    True
    >>> type(dat[0]) == list
    True
    >>> len(dat[0]) == len(header)
    True
    >>> len(dat) != len(header)
    True
    >>> len(dat) > 200
    True
    >>> header[0]
    'Black closed infinity, rainbow background'
    >>> header[1]
    'Black open infinity, rainbow background'
    >>> dat[EXAMPLE_ROW]
    ['4', '5', '1', '1', '1', '1', '3', '1', '1', '3', '2', '4', '2', '2', '2', '2', '3', '4', '4', '3', '1', '5', '5', '2', '1', '4', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '3', '1', '1', '1', '1', '5', '4', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel']
    """
    # read the data in, returning a list of lists and a list of headers
    data = []
    with open('input/autisticflagresults.csv') as f:
        header = f.readline().strip().split('\t')[1:]
        for line in f:
            info = line.strip().split('\t')
            while len(info) <= len(header):
                info.append(SENTINEL) # use SENTINEL for empty votes
            data.append(info[1:])
    return data, header


def count_strong_agrees(data):
    """
    Count how many votes in data are a strong agree for a given flag
    :param data:
    :return: A list of percentages (how many votes for a flag were a strong agree)
    >>> dat, header = read_data()
    >>> perc_sa = count_strong_agrees(dat)
    >>> len(perc_sa) == len(header)
    True
    >>> type(perc_sa) == list and type(perc_sa[0]) == float
    True
    >>> perc_sa[0] > 0.1 and perc_sa[0] < 0.3
    True
    """
    # count how many strong agrees there are
    strong_agrees = [0]*len(header)
    entries = [0]*len(header)
    for row in data:
        for i, vote in enumerate(row):
            if vote and vote != SENTINEL:
                entries[i] += 1
                if int(vote) >= STRONG_AGREE:
                    strong_agrees[i] += 1

    # use percentages rather than absolute values as some flags were added late
    percents = [0]*len(header)
    for i in range(len(header)):
        if entries[i] > 0:
            percents[i] = strong_agrees[i] / entries[i]
        else:
            percents[i] = -1

    return percents


def remove_row_voting_for_argmax(data, argmax, agree_thresh):
    """
    Remove a row of votes if the row voted AGREE_THRESH or higher for the flag with index argmax
    :param data: 2D list
    :param argmax: index of the flag in question
    :return: None - just alter the list since it's mutable
    >>> dat, header = read_data()
    >>> dat[EXAMPLE_ROW]
    ['4', '5', '1', '1', '1', '1', '3', '1', '1', '3', '2', '4', '2', '2', '2', '2', '3', '4', '4', '3', '1', '5', '5', '2', '1', '4', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '3', '1', '1', '1', '1', '5', '4', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel']
    >>> remove_row_voting_for_argmax(dat, 3, 4)
    >>> dat[EXAMPLE_ROW] # shouldn't change
    ['4', '5', '1', '1', '1', '1', '3', '1', '1', '3', '2', '4', '2', '2', '2', '2', '3', '4', '4', '3', '1', '5', '5', '2', '1', '4', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '3', '1', '1', '1', '1', '5', '4', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel']
    >>> remove_row_voting_for_argmax(dat, 1, 4)
    >>> dat[EXAMPLE_ROW]
    ['sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel']
    """
    # every row that has a 5 for argmax is now set to 'removed'
    for i, row in enumerate(data):
        if row[argmax] and row[argmax] != SENTINEL and int(row[argmax]) >= agree_thresh:
           data[i] = [SENTINEL]*len(header)


def remove_just_argmax(data, argmax, agree_thresh):
    """
    Remove a vote if the participant voted AGREE_THRESH or higher for the flag with index argmax
    :param data: 2D list
    :param argmax: index of the flag in question
    :return: None - just alter the list since it's mutable
    >>> dat, header = read_data()
    >>> dat[EXAMPLE_ROW]
    ['4', '5', '1', '1', '1', '1', '3', '1', '1', '3', '2', '4', '2', '2', '2', '2', '3', '4', '4', '3', '1', '5', '5', '2', '1', '4', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '3', '1', '1', '1', '1', '5', '4', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel']
    >>> remove_just_argmax(dat, 3, 4)
    >>> dat[EXAMPLE_ROW] # shouldn't change
    ['4', '5', '1', '1', '1', '1', '3', '1', '1', '3', '2', '4', '2', '2', '2', '2', '3', '4', '4', '3', '1', '5', '5', '2', '1', '4', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '3', '1', '1', '1', '1', '5', '4', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel']
    >>> remove_just_argmax(dat, 1, 4)
    >>> dat[EXAMPLE_ROW]
    ['4', 'sentinel', '1', '1', '1', '1', '3', '1', '1', '3', '2', '4', '2', '2', '2', '2', '3', '4', '4', '3', '1', '5', '5', '2', '1', '4', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '3', '1', '1', '1', '1', '5', '4', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel']
    """
    for i, row in enumerate(data):
        if row[argmax] and row[argmax] != SENTINEL and int(row[argmax]) >= agree_thresh:
            data[i][argmax] = SENTINEL


def remove_row_voting_for_argmax_if_thresh(data, argmax, participants, threshold, agree_thresh):
    """
    Hybrid of removing a whole row for voting for a flag vs just that vote:
    if the participant has a threshold number of flags they've voted for that have made it into the shortlist so far, remove the whole row
    else just remove the single vote
    :param data: 2D list
    :param argmax: index of the flag in question
    :return: None - just alter the list since it's mutable
    >>> dat, header = read_data()
    >>> participants = [0]*len(dat)
    >>> dat[EXAMPLE_ROW]
    ['4', '5', '1', '1', '1', '1', '3', '1', '1', '3', '2', '4', '2', '2', '2', '2', '3', '4', '4', '3', '1', '5', '5', '2', '1', '4', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '3', '1', '1', '1', '1', '5', '4', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel']
    >>> remove_row_voting_for_argmax_if_thresh(dat, 3, participants, 1, 4)
    >>> dat[EXAMPLE_ROW] # shouldn't change
    ['4', '5', '1', '1', '1', '1', '3', '1', '1', '3', '2', '4', '2', '2', '2', '2', '3', '4', '4', '3', '1', '5', '5', '2', '1', '4', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '3', '1', '1', '1', '1', '5', '4', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel']
    >>> remove_row_voting_for_argmax_if_thresh(dat, 1, participants, 1, 4)
    >>> dat[EXAMPLE_ROW]
    ['4', 'sentinel', '1', '1', '1', '1', '3', '1', '1', '3', '2', '4', '2', '2', '2', '2', '3', '4', '4', '3', '1', '5', '5', '2', '1', '4', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '3', '1', '1', '1', '1', '5', '4', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel']
    >>> dat[EXAMPLE_ROW][1] = '5'
    >>> dat[EXAMPLE_ROW]
    ['4', '5', '1', '1', '1', '1', '3', '1', '1', '3', '2', '4', '2', '2', '2', '2', '3', '4', '4', '3', '1', '5', '5', '2', '1', '4', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '3', '1', '1', '1', '1', '5', '4', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel']
    >>> remove_row_voting_for_argmax_if_thresh(dat, 1, participants, 0, 4)
    >>> dat[EXAMPLE_ROW]
    ['sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel', 'sentinel']
    """
    # if a participant has had threshold many SA votes in the shortlist, remove their whole row
    # else just removed the single cell
    for i, row in enumerate(data):
        if row[argmax] and row[argmax] != SENTINEL and int(row[argmax]) >= agree_thresh:
            if participants[i] >= threshold:
                data[i] = [SENTINEL]*len(header)
            else:
                data[i][argmax] = SENTINEL


def remove_rows(data, participants, threshold):
    """
    Remove the rows of participants who have threshold many favoured flags
    in the shortlist thus far.
    :param data: 2D list of votes
    :param participants: 1D list of participants, how many flags they voted for have been shortlisted so far
    :param threshold: threshold of how many flags in the shortlist will lead to removal from data
    :return: nothing, just change data since it's mutable
    >>> dat, header = read_data()
    >>> particip = [0]*6 + [3]*(len(dat)-12) + [2]*6
    >>> particip[:7] + particip[-16:]
    [0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2]
    >>> shortlist = [52, 42, 14, 59, 1, 15, 11]
    >>> remove_rows(dat, particip, 2)
    >>> len(set(dat[0])) > 2
    True
    >>> set(dat[30])
    {'sentinel'}
    >>> len(set(dat[-1])) > 2
    True
    """
    for i, p in enumerate(participants):
        if p > threshold:
            data[i] = [SENTINEL]*len(header)


def update_participant_SAs_in_shortlist(participants, data, argmax, agree_thresh):
    """
    Keep a running tally of how many flags a given participant has approved of that have
    made it into the shortlist of flags.
    :param participants: list, indexed same as data, keeping track of many approved-of flags a participant has in the shortlist
    :param data: the 2D list of data with votes
    :param argmax: the index of a flag that was just added to the shortlist
    :return: nothing - just update participants since it's mutable
    >>> dat, header = read_data()
    >>> participants = [0]*len(dat)
    >>> update_participant_SAs_in_shortlist(participants, dat, 0, 4) # everybody who voted for flag #0
    >>> votes_for_flag_0 = sum(participants)
    >>> votes_for_flag_0 > 20 and votes_for_flag_0 < len(data)/2
    True
    >>> max(participants)
    1
    >>> min(participants)
    0
    >>> update_participant_SAs_in_shortlist(participants, dat, 1, 4) # everybody who voted for flag #0
    >>> updated_sum = sum(participants)
    >>> updated_sum > votes_for_flag_0
    True
    >>> max(participants)
    2
    >>> min(participants)
    0
    """
    for i, row in enumerate(data):
        if row[argmax] and row[argmax] != SENTINEL and int(row[argmax]) >= agree_thresh:
            participants[i] += 1


def how_many_participants_have_above(participants, threshold):
    """
    How many entries in the participant list have a value above threshold
    :param participants: list of int
    :param threshold: threshold
    :return: how many are above the threshold
    >>> how_many_participants_have_above([1, 4, 3, 0], 2)
    2
    >>> how_many_participants_have_above([1, 4, 3, 0], 0)
    3
    >>> how_many_participants_have_above([1, 4, 3, 0], 1)
    2
    >>> how_many_participants_have_above([], 0)
    0
    """
    n = 0
    for p in participants:
        if p > threshold:
            n += 1
    return n


def get_medians(data, header):
    """
    Compute the median vote for every flag in the data set.
    :param data: 2D list, numbers may appear as strings
    :param header: list of flag names
    :return: list with the median of each flag, indexed to header
    >>> dat, header = read_data()
    >>> medians = get_medians(dat, header)
    >>> medians[0] >= 3 # pretty sure Flag 0 (Julietanboy) will remain at or above 3 at this point.
    True
    >>> apl_index = header.index('The Autistic Pride London Flag (purple-green, gold starburst, rainbow infinity)')
    >>> medians[apl_index] # seems pretty stable that the Autistic Pride London flag has a median of 1.0
    1.0
    >>> max(medians)
    4.0
    >>> min(medians) <= 1.0
    True
    >>> len(medians) == len(header)
    True
    """
    medians = [0]*len(header)
    data_transposed = []
    for q in header:
        data_transposed.append(  ['']*len(participants) )

    for i, row in enumerate(data):
        for j, vote in enumerate(row):
            data_transposed[j][i] = vote

    for i, row in enumerate(data_transposed):
        actual_numbers = []
        for vote in row:
            if vote.isnumeric():
                actual_numbers.append(int(vote))
        if len(actual_numbers) == 0:
            medians[i] = -1
        else:
            medians[i] = np.median(actual_numbers)
    return medians


def remove_options_with_negative_medians(data, header, median_threshold = 2):
    # first, remove the flags with a median of 2 or less
    print('STAGE 1: REMOVING FLAGS WITH MEDIAN OF 2 OR LESS')
    medians = get_medians(data, header)
    removed_by_median = []
    for design_id, median in enumerate(medians):
        if median <= median_threshold:
            #print(design_id, header[design_id])
            remove_just_argmax(data, design_id, 5)
            removed_by_median.append(design_id)
    print('Removed:', removed_by_median)
    return medians


def remove_less_liked_variants(data, header, medians):
    print('\nSTAGE 2: REMOVING SIMILAR DESIGNS THAT HAVE A BETTER PERFORMING VERSION')
    # second, remove underperforming variants
    variations = {
        'julietan':['Black open infinity, rainbow background', 'Black closed infinity, rainbow background'],
        'naut-plain':['Autism spectrum nautilus, disability grey background',
                      'Simplified nautilus (7 segments) on grey', '8-segment nautilus on grey', 'Autism Spectrum Nautilus, white background'],
        'naut-stripe':['Autism spectrum nautilus, disability pride stripe background', '7-segment nautilus on disability pride stripes'],
        'spritely':['Red infinity, teal background', 'Red open infinity with teal aesthetic', 'Red infinity on white circle with teal aesthetic'],
        'empire':['Rainbow gradient infinity loop, gold background', 'Rainbow segmented infinity loop with white dividers, gold background', 'Rainbow segmented infinity loop, gold background'],
        'concwhite':['Concentric disability pride, white background', 'Concentric ROYLG, white background',
                     'Autistic Pride Day (Australia), gradient concentric infinities'],
    }
    to_dump = []
    strong_agrees = count_strong_agrees(data)
    # identify which versions to dump
    for varname in variations:
        print(varname)

        max_median = -1
        max_perc_sa = -1
        for design_name in variations[varname]:
            design_id = header.index(design_name)
            print('\t', design_name, design_id, medians[design_id], strong_agrees[design_id])
            max_median = max(max_median, medians[design_id])
            max_perc_sa = max(strong_agrees[design_id], max_perc_sa)

        for design_name in variations[varname]:
            design_id = header.index(design_name)
            if medians[design_id] <= max_median and strong_agrees[design_id] < max_perc_sa:
                to_dump.append(design_id)
                print('\t\tdumping', design_name)

        #print(max_median, max_perc_sa)
        print()

    #print('To dump', to_dump)
    # actually dump them
    for design_id in to_dump:
        remove_just_argmax(data, design_id, 5)


def sort_by_sa(data, header, shortlist, agree_threshold, participants, minimum_flags_to_get, minimum_approval_needed):
    # TODO: SA above threshold first then the other-placating?
    print('STAGE 3: SORT REMAINING FLAGS BY APPROVAL RATING')
    strong_agrees = count_strong_agrees(data)
    max_strong_agree = max(strong_agrees)
    i = 0
    while max_strong_agree > minimum_approval_needed and len(shortlist) < minimum_flags_to_get:
        argmax = np.argmax(np.array(strong_agrees))
        shortlist.append(argmax)

        print('\t', i + 1, header[argmax], round(strong_agrees[argmax], 3))
        i += 1
        update_participant_SAs_in_shortlist(participants, data, argmax, agree_threshold)
        remove_just_argmax(data, argmax, agree_threshold)
        strong_agrees = count_strong_agrees(data)
        max_strong_agree = max(strong_agrees)

    satis_particip = how_many_participants_have_above(participants, 0)
    satis_ratio = round(100 * satis_particip / num_participants, 1)
    print(
        f'Results: {satis_particip} of {num_participants} ({satis_ratio}%) participants have a flag they approved of in the shortlist\n')


def sort_and_eliminate_by_sa(data, header, shortlist, participants, agree_threshold):
    print('STAGE 4: SORT REMAINING FLAGS BY APPROVAL RATING')
    num_with_a_sa = 0
    i = 0
    while len(shortlist) < how_many_flags_to_shortlist:
        strong_agrees = count_strong_agrees(data)
        argmax = np.argmax(np.array(strong_agrees))
        shortlist.append(argmax)

        print('\t', i+1, header[argmax], round(strong_agrees[argmax],3))
        update_participant_SAs_in_shortlist(participants, data, argmax, agree_threshold)

        #remove_row_voting_for_argmax(data, argmax)
        #remove_just_argmax(data, argmax)
        # if not doing a stage beforehand of  SA > 15%
        # threshold of 1 runs out of flags after 10.
        # threshold of 2 means only one nautilus flag
        remove_row_voting_for_argmax_if_thresh(data, argmax, participants, 5, agree_threshold)
        i += 1


def display_shortlist_row(d, shortlist, election_number, key, stat):
    for i, flag_id in enumerate(shortlist):
        flag_name = header[flag_id]
        flag_path = f'input/surveyed_autism_flags/{flag_name}.png'
        assert exists(flag_path), flag_path
        img = drawsvg.Image( disp_hei*(i+.5) + margin, margin + flag_second_dim*2*election_number, flag_size, flag_second_dim, flag_path)
        d.append(img)
        d.append(drawsvg.Text(str(i+1), 30, fill='black',
                              x=disp_hei*(i+1)-margin, y=margin*2 + flag_second_dim*1.5 + flag_second_dim*2*election_number))
        d.append(drawsvg.Text(str(stat), 30, x=margin, y=margin*2 + flag_second_dim*2*election_number + flag_second_dim*.5, fill='black'))
        d.append(drawsvg.Text(str(key), 10, x=d.width-margin-flag_second_dim, y=margin*2 + flag_second_dim*2*election_number + flag_second_dim*.5, fill='black'))



def run_election(data, header, how_many_flags_to_shortlist, agree_threshold, to_eliminate, elimination_threshold, init_sa_thresh):
    shortlist = []
    medians = remove_options_with_negative_medians(data, header) # stage 1
    remove_less_liked_variants(data, header, medians) # stage 2
    sort_by_sa(data, header, shortlist, agree_threshold, participants, how_many_flags_to_shortlist, init_sa_thresh) # stage 3
    if to_eliminate:
        remove_rows(data, participants, elimination_threshold)
    sort_and_eliminate_by_sa(data, header, shortlist, participants, agree_threshold)
    return shortlist

if __name__ == '__main__':
    # basic stats etc from the data
    data, header = read_data()
    num_participants = len(data)

    # input parameters
    how_many_flags_to_shortlist = 12
    satisfaction_threshold = 0

    election_results = {}
    election_stats = {}

    for agree_threshold in [4, 5]:  # 3 doesn't make sense!
        for to_eliminate in [False, True]: # elimination step not very useful apparently
            for init_sa_thresh in [.11]:  #.14,  fairly robust between .14 and .2. Worse stats when .11.
                for elimination_threshold in [0, 1, 2, 3, 4]:
                    participants = [0] * num_participants
                    shortlist = run_election(copy.deepcopy(data), header, how_many_flags_to_shortlist,
                                             agree_threshold, to_eliminate, elimination_threshold, init_sa_thresh)
                    et = elimination_threshold
                    if to_eliminate == False:
                        et = 'f'
                    key = f'a{agree_threshold}e{str(to_eliminate)[0]}@{et}i{init_sa_thresh}'
                    if shortlist[-1] != shortlist[-2] and 0 not in shortlist:
                        election_results[key] = shortlist
                        satis_particip = how_many_participants_have_above(participants, satisfaction_threshold)
                        satis_ratio = round(100*satis_particip/num_participants,1)
                        print(key)
                        print(f'Results: {satis_particip} of {num_participants} ({satis_ratio}%) participants have a flag they approved of in the shortlist')
                        election_stats[key] = satis_ratio

    # then display them
    flag_size = 90
    flag_second_dim = flag_size*(3/5)
    margin = 5
    disp_hei = flag_size + 2*margin
    h = (how_many_flags_to_shortlist+1)*(disp_hei)
    w = (flag_second_dim*2)*len(election_results)
    d = drawsvg.Drawing( h, w)
    d.append(drawsvg.Rectangle(0,0, d.width, d.height, fill='#' + 'c'*6))
    i = 0
    shorted_flags = {}

    for key in election_results:
        display_shortlist_row(d, election_results[key], i, key, election_stats[key])
        i += 1
        for e in election_results[key]:
            flag_name = header[e]
            if flag_name not in shorted_flags:
                shorted_flags[flag_name] = 1
            else:
                shorted_flags[flag_name] += 1


    print(shorted_flags)
    #print(shortlist)

    d.save_svg('test.svg')

    doctest.testmod()

    pretty = json.dumps(shorted_flags, indent=4)
    print(pretty)
    print(len(shorted_flags))