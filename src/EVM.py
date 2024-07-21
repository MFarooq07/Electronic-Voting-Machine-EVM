import random
from collections import Counter

class Election:
    def __init__(self, candidates):
        self.candidates = candidates
        self.votes = []
        self.total_votes = {candidate: 0 for candidate in candidates}

    def add_vote(self, vote):
        self.votes.append(vote)
        self.total_votes[vote] += 1

    def determine_winner(self):
        vote_count = Counter(self.votes)
        winner = vote_count.most_common(1)[0][0]
        return winner

    def get_votes_per_candidate(self):
        return self.total_votes

def simulate_votes(election, candidates, num_votes):
    for _ in range(num_votes):
        vote = random.choice(candidates)
        election.add_vote(vote)

# Assign votes by popularity for each province
def assign_votes_by_popularity(election, candidate1, candidate2, candidate3, num_votes):
    votes1 = num_votes * 0.5
    votes2 = num_votes * 0.3
    votes3 = num_votes * 0.2
    for _ in range(int(votes1)):
        election.add_vote(candidate1)
    for _ in range(int(votes2)):
        election.add_vote(candidate2)
    for _ in range(int(votes3)):
        election.add_vote(candidate3)

# Print votes earned by each candidate in descending order for each province
def print_votes_per_candidate(votes_per_candidate):
    sorted_votes = sorted(votes_per_candidate.items(), key=lambda x: x[1], reverse=True)
    for candidate, votes in sorted_votes:
        print(f"{candidate}: {votes}")

# Conduct elections in different regions
def conduct_elections():
    # Candidates
    candidates = ["PTI", "PMLN", "PPPP", "MQM", "JUI"]

    # Punjab
    num_votes_punjab = 530
    election_punjab = Election(candidates)
    assign_votes_by_popularity(election_punjab, "PTI", "PMLN", "PPPP", num_votes_punjab)
    simulate_votes(election_punjab, candidates, num_votes=50)
    print("Punjab Results:")
    print("Winner:", election_punjab.determine_winner())
    print("Votes per Candidate:")
    print_votes_per_candidate(election_punjab.get_votes_per_candidate())
    

    # Sindh
    num_votes_sindh = 230
    election_sindh = Election(candidates)
    assign_votes_by_popularity(election_sindh, "PPPP", "MQM", "PTI", num_votes_sindh)
    simulate_votes(election_sindh, candidates, num_votes=50)
    print("\nSindh Results:")
    print("Winner:", election_sindh.determine_winner())
    print("Votes per Candidate:")
    print_votes_per_candidate(election_sindh.get_votes_per_candidate())

    # KPK
    num_votes_kpk = 160
    election_kpk = Election(candidates)
    assign_votes_by_popularity(election_kpk, "PTI", "PMLN", "JUI", num_votes_kpk)
    simulate_votes(election_kpk, candidates, num_votes=50)
    print("\nKPK Results:")
    print("Winner:", election_kpk.determine_winner())
    print("Votes per Candidate:")
    print_votes_per_candidate(election_kpk.get_votes_per_candidate())

    # Balochistan
    num_votes_balochistan = 70
    election_balochistan = Election(candidates)
    assign_votes_by_popularity(election_balochistan, "PPPP", "PMLN", "JUI", num_votes_balochistan)
    simulate_votes(election_balochistan, candidates, num_votes=50)
    print("\nBalochistan Results:")
    print("Winner:", election_balochistan.determine_winner())
    print("Votes per Candidate:")
    print_votes_per_candidate(election_balochistan.get_votes_per_candidate())

    # Federal
    num_votes_federal = 10
    election_federal = Election(candidates)
    assign_votes_by_popularity(election_federal, "PTI", "PMLN", "PPPP", num_votes_federal)
    simulate_votes(election_federal, candidates, num_votes=5)
    print("\nFederal Results:")
    print("Winner:", election_federal.determine_winner())
    print("Votes per Candidate:")
    print_votes_per_candidate(election_federal.get_votes_per_candidate())

    # Calculate total votes for each candidate across all regions
    totals_per_candidate = {candidate: 0 for candidate in candidates}
    for region in [election_punjab, election_sindh, election_kpk, election_balochistan, election_federal]:
        for candidate, votes in region.get_votes_per_candidate().items():
            totals_per_candidate[candidate] += votes

    # Example calculation for PTI
    tot_PTI = totals_per_candidate["PTI"]
    tot_PMLN = totals_per_candidate["PMLN"]
    tot_PPPP = totals_per_candidate["PPPP"]
    tot_MQM = totals_per_candidate["MQM"]
    tot_JUI = totals_per_candidate["JUI"]

    # Calculate adjusted total votes for each candidate and round to the nearest whole number
    adjusted_totals = {
        "PTI": round((tot_PTI/1205) * 265),
        "PMLN": round((tot_PMLN/1205) * 265),
        "PPPP": round((tot_PPPP/1205) * 265),
        "MQM": round((tot_MQM/1205) * 265),
        "JUI": round((tot_JUI/1205) * 265)
    }

    # Sort adjusted total votes for each candidate in descending order
    sorted_adjusted_totals = sorted(adjusted_totals.items(), key=lambda x: x[1], reverse=True)

    # Print adjusted total votes for each candidate in descending order
    print("Adjusted Total Votes per Candidate (Descending Order):")
    for candidate, adjusted_total_votes in sorted_adjusted_totals:
        print(f"{candidate}: {adjusted_total_votes}")


# Conduct elections in different regions
conduct_elections()
