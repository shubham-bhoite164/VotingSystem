# First we'll take the input of what nominee what we want to keep

nominee1 = input("Enter the name of First nominee :")
nominee2 = input("Enter the name of Second nominee :")

# initially vote count for both must be 0
nm1_votes = 0
nm2_votes = 0

voter_id = [1,2,3,4,5,6,7,8,9,10]

nO_of_voter = len(voter_id)

while True:
    if voter_id == []:  # to check when voter list is completed
        print("Votting session is over !!")
        if nm1_votes > nm2_votes:
            percent = (nm1_votes/nm2_votes)*100          # To calculate the percentage
            print(nominee1,"Has won the election with",percent,"% of votes")
            break     # To get rid of infinite loop

        elif nm2_votes > nm1_votes:
            percent = (nm2_votes/nm1_votes)*100
            print(nominee2,"Has won the election with", percent, "% of votes")
            break

        else:
            print("Both have Equal number votes !!!!")
            break


    voter = int(input("Enter your voter id : "))
    if voter in voter_id:
        print("You are voter")
        voter_id.remove(voter) #we will remove so that again the same voter can't vote
        print("TO give vote to ",nominee1,"Press 1 ")
        print("TO give vote to ",nominee2,"Press 2 ")
        print("------------------------------------")
        vote = int(input("Enter your precious vote :"))
        if vote == 1:
            nm1_votes += 1
            print(nominee1,"Thank you to give your importat vote to them !!")

        elif vote == 2:
            nm2_votes += 1
            print(nominee2,"Thank you to give your importat vote to them !!")

        elif vote > 2:
            print("Check your pressed key !!")

        else:
            print("You are not voter OR You have alredy voted")

