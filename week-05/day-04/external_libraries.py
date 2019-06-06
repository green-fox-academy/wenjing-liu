def prettify_graph(graph):
    """Modify the given graph according to Jimmy's requests: add a title, make the y-axis
    start at 0, label the y-axis. (And, if you're feeling ambitious, format the tick marks
    as dollar amounts using the "$" symbol.)
    """
    # Complete steps 2 and 3 here
    graph.set_title("Results of 500 slot machine pulls")
    graph.set_ylim(0)
    graph.set_ylabel("Balance")
    current_labels = graph.get_yticks()
    new_labels = ['${}'.format(int(label)) for label in current_labels]
    # Set the new labels
    graph.set_yticklabels(new_labels)

# graph = jimmy_slots.get_graph()
# prettify_graph(graph)
# graph



# Import luigi's full dataset of race data
from learntools.python.luigi_analysis import full_dataset as fd
# Fix me!
def best_items(racers):
    winner_item_counts = {}
    for i in range(len(racers)):
        # The i'th racer dictionary
        racer = racers[i]
        # We're only interested in racers who finished in first
        if racer['finish'] == 1:
            for j in racer['items']:
                # Add one to the count for this item (adding it to the dict if necessary)
                if j not in winner_item_counts:
                    winner_item_counts[j] = 0
                winner_item_counts[j] += 1

        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                i+1, len(racers), racers.index(racer))
                 )
    return winner_item_counts

# Try analyzing the imported full dataset
best_items(fd)

print(best_items(sample))



def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    sum_hand1 = 0
    num_A_1 = 0
    for item in hand_1:
        if item in ('J', 'Q', 'K'): 
            sum_hand1 += 10
        elif item != 'A':
            sum_hand1 += int(item)
        else:
            num_A_1 += 1
            sum_hand1 += 1
    
    if num_A_1 > 0 and sum_hand1 <12: sum_hand1 += 10
    
    sum_hand2 = 0
    num_A_2 = 0
    for item in hand_2:
        if item in ('J', 'Q', 'K'): 
            sum_hand2 += 10
        elif item != 'A':
            sum_hand2 += int(item)
        else:
            num_A_2 += 1
            sum_hand2 += 1
    
    if num_A_2 > 0 and sum_hand2 < 12: sum_hand2 += 10

    
    return sum_hand1 > sum_hand2 and sum_hand1 < 22 or sum_hand1 < 22 and sum_hand2 > 21




