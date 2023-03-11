#BLACK JACK GAME WITH BET OPTION BY RAPHAEL MSOMEA
player_name = str(input (" Enter your name: "))
while True:
    money=10000
#Money controlling loop
    while money>0:
        import random 
        import time
        deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13]
        1=='Ace'
        11=='Jacky'
        12=='Queen'
        13=='King'
    #Player hands
        player_hand_1 = random.choice(deck)
        player_hand_2 = random.choice(deck)
        player_hand_3 = random.choice(deck)
        player_hand_4 = random.choice(deck)
        player_hand_5 = random.choice(deck)
        player_hand_6 = random.choice(deck)
    #Dealer hands 
        dealer_hand_1 = random.choice(deck)
        dealer_hand_2 = random.choice(deck)
        dealer_hand_3 = random.choice(deck)
        dealer_hand_4 = random.choice(deck)
        dealer_hand_5 = random.choice(deck)
        dealer_hand_6 = random.choice(deck)
    #Global variables
        player_hit = ["h", "H" ]
        player_stand = ["s", "S"]
        player_quite = ["q", "Q"]
        player_proceed = ["p", "P"]
    #Ends of variables
        print(" Your balance: $", money)
        bet=int(input(" Enter your bet: "))
        if bet>money:
            print(" You Dont have enough balance")
            bet=int(input(" Enter your bet: "))
        if bet<500:
            print(" You can place bet starting from $ 500 ")
            bet=int(input(" Enter your bet: "))
        balance=((int(money))-bet)
#First Round Dealing
        print()
        print (" New Game") 
        print (" First dealing")
        wait = ("****")
        print(" Dealer is Dealing. Please Wait!....")
        print(" " + wait[:1])
        time.sleep(0.5)
        print(" " + wait[:2])
        time.sleep(0.5)
        player_total = player_hand_1
        player_card_count=1
        print (" " + str(player_name) + " has " + str(player_total) + " on hand")
        dealer_total = dealer_hand_1
        print (" Dealer has " + str(dealer_total) + " on hand")
        print (" ")
        time.sleep(0.5)
    #Second round Dealing
        player_total = (player_total + player_hand_2)
        player_card_count=2
        dealer_total = dealer_hand_1
        print (" Second Dealing")
        wait = ("****")
        print(" Dealer is Dealing. Please Wait!....")
        print(" " + wait[:1])
        time.sleep(0.5)
        print(" " + wait[:2])
        time.sleep(0.5)
    #Player Bast
        if player_total > 21:
            pass
            if player_card_count==2:
                print (" " + str(player_name) + " Bast. Yo have: " + str(player_hand_1) + " and " + str(player_hand_2) +" on hand.")
            print (" Total " + str(player_name) + " card: "+ str(player_total))
            win_condition="2"
            lose_condition="1"
            if "1" in win_condition:
                bet_win=(bet*2)
            if "1" in lose_condition:
                bet_win=0
            money=(balance+bet_win)
            choice = str(input(" To quite press q/Q. To Proceed press p/P: "))
            if choice in player_quite:
                break
            if choice in player_proceed:
                continue
        
    #Player still in player
        else:
            pass
            if player_card_count==2:
                print (" " + str(player_name) + " has " + str(player_hand_1) + " and "+str(player_hand_2) + " on hand.")
            if player_card_count==3:
                print (" " + str(player_name) + " has " + str(player_hand_1) + ", "+str(player_hand_2)+ " and " +str(player_hand_3) + " on hand.")
            print (" Total " + str(player_name) + " card: "+ str(player_total))
            print (" Dealer has " + str(dealer_hand_1) + " and XXX on hand")
            print (" Total Dealer Card: " + str(dealer_total) + "+XXX")
            print (" ")
            hit_choice = str(input (" Press h/H to Hit. Press s/S to Stand: "))
            print(),print()
    #Player Hit Round One 
        if hit_choice in player_hit:
            dealer_total = dealer_hand_1
            player_total = (player_total + player_hand_3)
            player_card_count=3
            print (" Third Dealing")
            wait = ("....")
            print(" Dealer is Dealing. Please Wait!....")
            print(" " + wait[:1])
            time.sleep(0.5)
            print(" " + wait[:2])
            time.sleep(0.5)
            if player_total > 21:
                print (" " + str(player_name) + " Bast. Yo have: "+ str(player_hand_1) +", "+str(player_hand_2)+" and "+ str(player_hand_3)+ " on hand")
                print (" Total" + str(player_name) + " card: "+ str(player_total))
                lose_condition="1"
                win_condition="2"
                if "1" in win_condition:
                    bet_win=(bet*2)
                if "1" in lose_condition:
                    bet_win=0
                money=(balance+bet_win)
                choice = str(input(" To quite press q/Q. To Proceed press p/P: "))
                if choice in player_quite:
                    break
                if choice in player_proceed:
                    continue
            else:
                print (" " + str(player_name) + " have: "+ str(player_hand_1) +", "+str(player_hand_2)+" and "+str(player_hand_3)+ " on hand")
                print (" Total" + str(player_name) + " card: " + str(player_total))
                print (" Dealer has " + str(dealer_hand_1) + "+ XXX on hand")
                print (" Total Dealer Card: " + str(dealer_hand_1) + "+XXX")
                print (" ")
                hit_choice = str(input (" Press h/H to Hit. Press s/S to Stand: "))
                print(),print() 
    #Player Hit Round Two
        if hit_choice in player_hit:
            dealer_total = dealer_hand_1
            player_total = (player_total + player_hand_4)
            player_card_count=4
            print (" Fouth Dealing")
            wait = ("....")
            print(" Dealer is Dealing. Please Wait!....")
            print(" " + wait[:1])
            time.sleep(0.5)
            print(" " + wait[:2])
            time.sleep(0.5)
            if player_total > 21:
                print (" " + str(player_name) + " Bast. Yo have: "+ str(player_hand_1) +", "+str(player_hand_2)+", "+str(player_hand_3)+", "+" and "+ str(player_hand_4)+ " on hand")
                print (" Total" + str(player_name) + " card: "+ str(player_total))
                lose_condition="1"
                win_condition="2"
                if "1" in win_condition:
                    bet_win=(bet*2)
                if "1" in lose_condition:
                    bet_win=0
                money=(balance+bet_win)
                choice = str(input(" To quite press q/Q. To Proceed press p/P: "))
                if choice in player_quite:
                    break
                if choice in player_proceed:
                    continue
            else:
                print (" " + str(player_name) + " have: "+ str(player_hand_1) +", "+str(player_hand_2)+", "+str(player_hand_3)+" and "+str(player_hand_4)+ " on hand")
                print (" Total" + str(player_name) + " card: " + str(player_total))
                print()
                print (" Dealer has " + str(dealer_hand_1) + "+ XXX on hand")
                print (" Total Dealer Card: " + str(dealer_hand_1) + "+XXX")
                print (" ")
                  
                print(),print()
    #Player Hit Round Three
        if hit_choice in player_hit:
            dealer_total = dealer_hand_1
            player_total = (player_total + player_hand_5)
            player_card_count=5
            print (" Fifth Dealing")
            wait = ("....")
            print(" Dealer is Dealing. Please Wait!....")
            print(" " + wait[:1])
            time.sleep(0.5)
            print(" " + wait[:2])
            time.sleep(0.5)
            if player_total > 21:
                print (" " + str(player_name) + " Bast. Yo have: "+ str(player_hand_1) +","+str(player_hand_2)+","+str(player_hand_3)+","+str(player_hand_4)+" and "+ str(player_hand_5)+ " on hand")
                print (" Total" + str(player_name) + " card: "+ str(player_total))
                lose_condition="1"
                win_condition="2"
                if "1" in win_condition:
                    bet_win=(bet*2)
                if "1" in lose_condition:
                    bet_win=0
                money=(balance+bet_win)
                choice = str(input(" To quite press q/Q. To Proceed press p/P: "))
                if choice in player_quite:
                    break
                if choice in player_proceed:
                    continue
            else:
                print (" " + str(player_name) + " have: "+ str(player_hand_1) +", "+str(player_hand_2)+", "+str(player_hand_3)+", "+str(player_hand_4)+" and "+ str(player_hand_5)+ " on hand")
                print (" Total" + str(player_name) + " card: " + str(player_total))
                print()
                print (" Dealer has " + str(dealer_hand_1) + "+ XXX on hand")
                print (" Total Dealer Card: " + str(dealer_hand_1) + "+XXX")
                print (" ")
                hit_choice = str(input (" Press h/H to Hit. Press s/S to Stand: "))
                print(),print()
    #Player Hit Round Four
        if hit_choice in player_hit:
            dealer_total = dealer_hand_1
            player_total = (player_total + player_hand_6)
            player_card_count=6
            print (" Sixth Dealing")
            wait = ("....")
            print(" Dealer is Dealing. Please Wait!....")
            print(" " + wait[:1])
            time.sleep(0.5)
            print(" " + wait[:2])
            time.sleep(0.5)
            if player_total > 21:
                print (" " + str(player_name) + " Bast. Yo have: "+ str(player_hand_1) +", "+str(player_hand_2)+", "+str(player_hand_3)+", "+str(player_hand_4)+", "+str(player_hand_5)+" and "+ str(player_hand_6)+ " on hand")
                print (" Total" + str(player_name) + " card: "+ str(player_total))
                lose_condition="1"
                win_condition="2"
                if "1" in win_condition:
                    bet_win=(bet*2)
                if "1" in lose_condition:
                    bet_win=0
                money=(balance+bet_win)
                choice = str(input(" To quite press q/Q. To Proceed press p/P: "))
                if choice in player_quite:
                    break
                if choice in player_proceed:
                    continue
            else:
                print (" " + str(player_name) + " have: "+ str(player_hand_1) +", "+str(player_hand_2)+", "+str(player_hand_3)+", "+str(player_hand_4)+ str(player_hand_5)+" and "+str(player_hand_6)+" on hand")
                print (" Total" + str(player_name) + " card: " + str(player_total))
                print()
                print (" Dealer has " + str(dealer_hand_1) + "+ XXX on hand")
                print (" Total Dealer Card: " + str(dealer_hand_1) + "+XXX")
                print (" ")
                hit_choice = str(input (" Press h/H to Hit. Press s/S to Stand: "))
                print(),print()
    #No more Dealing
        if hit_choice in player_hit:
            print (" No more Dealing is Allowed!")
    #Player Stand Round
        if hit_choice in player_stand:
            dealer_total = dealer_hand_1
            if dealer_total < 17:
                dealer_total = (dealer_total + dealer_hand_2)
                dealer_card_counter=2
            if dealer_total < 17:
                dealer_total = (dealer_total + dealer_hand_3)
                dealer_card_counter=3
            if dealer_total < 17:
                dealer_total = (dealer_total + dealer_hand_4)
                dealer_card_counter=4
            if dealer_total < 17:
                dealer_total = (dealer_total + dealer_hand_5)
                dealer_card_counter=5
            if dealer_total < 17:
                dealer_total = (dealer_total + dealer_hand_6)
                dealer_card_counter=6
            wait = ("*****")
            print(" Dealer is Hiting. Please Wait!....")
            print(" " + wait[:1])
            time.sleep(0.5)
            print(" " + wait[:2])
            time.sleep(0.5)
            print(" " + wait[:3])
            time.sleep(0.5)
            print(" " + wait[:4])
            time.sleep(0.5)
            print(" " + wait[:5])
    #Tie Condition
        if player_total==dealer_total:
            print(" Tie Game")
            if dealer_card_counter==2:
                print (" Dealer have: "+ str(dealer_hand_1) +" and "+str(dealer_hand_2) +" on hand")
            if dealer_card_counter==3:
                print (" Dealer have: "+ str(dealer_hand_1) +", "+str(dealer_hand_2)+" and "+str(dealer_hand_3) +" on hand")
            elif dealer_card_counter==4:
                print (" Dealer have: "+ str(dealer_hand_1) +", "+str(dealer_hand_2)+", "+str(dealer_hand_3) + " and "+str(dealer_hand_4) +" on hand")
            elif dealer_card_counter==5:
                    print (" Dealer have: "+ str(dealer_hand_1) +", "+str(dealer_hand_2)+", "+str(dealer_hand_3) + " and "+str(dealer_hand_4)+" and "+ str(dealer_hand_5) + " on hand")
            elif dealer_card_counter==6:
                print (" Dealer have: "+ str(dealer_hand_1) +", "+str(dealer_hand_2)+", "+str(dealer_hand_3) + " and "+str(dealer_hand_4)+" and "+ str(dealer_hand_5) +str(dealer_hand_6)+" on hand")
            print (" Dealer has total of " + str(dealer_total) + " card")
            if player_card_count ==2:
                print (" " +str(player_name)+"  have: " +str(player_hand_1) +" and "+str(player_hand_2) +" on hand")
            if player_card_count==3:
                print (" " +str(player_name)+"  have: " +str(player_hand_1) +" and "+str(player_hand_2) +str(player_hand_3) +" on hand")
            elif player_card_count ==4:
                print (" " +str(player_name)+"  have: " +str(player_hand_1) +" and "+str(player_hand_2) +str(player_hand_3)+str(player_hand_4)+" on hand")
            elif player_card_count==5:
                    print (" " +str(player_name)+"  have: " +str(player_hand_1) +" and "+str(player_hand_2) +str(player_hand_3)+str(player_hand_4) +str(player_hand_5)+ " on hand")
            elif player_card_count==6:
                print (" " +str(player_name)+"  have: " +str(player_hand_1) +" and "+str(player_hand_2) +str(player_hand_3)+str(player_hand_4) +str(player_hand_5)+str(player_hand_6)+" on hand")
            print (" " +str(player_name)+ " have Total of " +str(player_total) + " card")
            draw_condition="1"
            if "1" in draw_condition:
                bet_win=(bet)
            money=(balance+bet_win)
    #Player win condition
        #Normal win
        if 21 > player_total > dealer_total or dealer_total > 21 > player_total:
            win_condition="1"
            lose_condition="2"
            if "1" in win_condition:
                bet_win=(bet*2)
            if "1" in lose_condition:
                bet_win=0
            money=(balance+bet_win)
            if player_card_count ==2:
                print (" " +str(player_name)+"  have: " +str(player_hand_1) +" and "+str(player_hand_2) +" on hand")
            if player_card_count==3:
                print (" " +str(player_name)+"  have: " +str(player_hand_1) +", "+str(player_hand_2)+" and " +str(player_hand_3) +" on hand")
            elif player_card_count ==4:
                print (" " +str(player_name)+"  have: " +str(player_hand_1) +", "+str(player_hand_2)+", "+str(player_hand_3)+" and "+str(player_hand_4)+" on hand")
            elif player_card_count==5:
                    print (" " +str(player_name)+"  have: " +str(player_hand_1) +", "+str(player_hand_2)+", "+str(player_hand_3)+", " +str(player_hand_4)+" and " +str(player_hand_5)+ " on hand")
            elif player_card_count==6:
                print (" " +str(player_name)+"  have: " +str(player_hand_1) +", "+str(player_hand_2)+", " +str(player_hand_3)+", " +str(player_hand_4)+", "+str(player_hand_5)+" and " +str(player_hand_6)+" on hand")
            print (" " + str(player_name) + " Win with total of " + str(player_total) + " card")
            
            if dealer_card_counter==2:
                print (" Dealer have: "+ str(dealer_hand_1) +" and "+str(dealer_hand_2) +" on hand")
            if dealer_card_counter==3:
                print (" Dealer have: "+ str(dealer_hand_1) +", "+str(dealer_hand_2)+" and "+str(dealer_hand_3) +" on hand")
            elif dealer_card_counter==4:
                print (" Dealer have: "+ str(dealer_hand_1) +", "+str(dealer_hand_2)+", "+str(dealer_hand_3) + " and "+str(dealer_hand_4) +" on hand")
            elif dealer_card_counter==5:
                print (" Dealer have: "+ str(dealer_hand_1) +", "+str(dealer_hand_2)+", "+str(dealer_hand_3) + ", "+str(dealer_hand_4)+" and "+ str(dealer_hand_5) + " on hand")
            elif dealer_card_counter==6:
                print (" Dealer have: "+ str(dealer_hand_1) +", "+str(dealer_hand_2)+", "+str(dealer_hand_3) + ", "+str(dealer_hand_4)+", "+ str(dealer_hand_5)+" and " +str(dealer_hand_6)+" on hand")
            print (" Dealer has total of " + str(dealer_total) + " card")
            choice = str(input(" To quite press q/Q. To Proceed press p/P: "))
            print ()
            if choice in player_quite:
                break
            if choice in player_proceed:
                continue
    #Black Jack win
        if 21 == player_total > dealer_total or dealer_total > 21 == player_total:
            win_condition="1"
            lose_condition="2"
            if "1" in win_condition:
                bet_win=(bet*2)
            if "1" in lose_condition:
                bet_win=0
            money=(balance+bet_win)
            if player_card_count ==2:
                print (" " +str(player_name)+"  have: " +str(player_hand_1) +" and "+str(player_hand_2) +" on hand")
            if player_card_count==3:
                print (" "+str(player_name)+" have: " +str(player_hand_1) +", "+str(player_hand_2) +" and "+str(player_hand_3) +" on hand")
            elif player_card_count ==4:
                print (" " +str(player_name)+"  have: " +str(player_hand_1) +", "+str(player_hand_2)+", " +str(player_hand_3)+ " and " +str(player_hand_4)+" on hand")
            elif player_card_count==5:
                    print (" " +str(player_name)+"  have: " +str(player_hand_1) +", "+str(player_hand_2)+", " +str(player_hand_3)+", "+str(player_hand_4)+" and " +str(player_hand_5)+ " on hand")
            elif player_card_count==6:
                print (" " +str(player_name)+"  have: " +str(player_hand_1) +", "+str(player_hand_2)+", "+str(player_hand_3)+", "+str(player_hand_4)+", " +str(player_hand_5)+" and "+str(player_hand_6)+" on hand")
            print (" Black Jack! " + str(player_name) + " Win with total of " + str(player_total) + " card")

            if dealer_card_counter==2:
                print (" Dealer have: "+ str(dealer_hand_1) +" and "+str(dealer_hand_2) +" on hand")
            if dealer_card_counter==3:
                print (" Dealer have: "+ str(dealer_hand_1) +", "+str(dealer_hand_2)+" and "+str(dealer_hand_3) +" on hand")
            elif dealer_card_counter==4:
                print (" Dealer have: "+ str(dealer_hand_1) +", "+str(dealer_hand_2)+", "+str(dealer_hand_3) + " and "+str(dealer_hand_4) +" on hand")
            elif dealer_card_counter==5:
                print (" Dealer have: "+ str(dealer_hand_1) +", "+str(dealer_hand_2)+", "+str(dealer_hand_3) + ", "+str(dealer_hand_4)+" and "+ str(dealer_hand_5) + " on hand")
            elif dealer_card_counter==6:
                print (" Dealer have: "+ str(dealer_hand_1) +", "+str(dealer_hand_2)+", "+str(dealer_hand_3) + ", "+str(dealer_hand_4)+", "+ str(dealer_hand_5)+" and " +str(dealer_hand_6)+" on hand")
            print (" Dealer has total of " + str(dealer_total) + " card")
            choice = str(input(" To quite press q/Q. To Proceed press p/P: "))
            print ()
            if choice in player_quite:
                break
            if choice in player_proceed:
                continue
    #Dealer win condition
        #Normal win
        if 21 > dealer_total > player_total or player_total > 21 > dealer_total:
            lose_condition="1"
            win_condition="2"
            if "1" in win_condition:
                bet_win=(bet*2)
            if "1" in lose_condition:
                bet_win=0
            money=(balance+bet_win)
            if dealer_card_counter==2:
                print (" Dealer have: "+ str(dealer_hand_1) +" and "+str(dealer_hand_2) +" on hand")
            if dealer_card_counter==3:
                print (" Dealer have: "+ str(dealer_hand_1) +", "+str(dealer_hand_2)+" and "+str(dealer_hand_3) +" on hand")
            elif dealer_card_counter==4:
                print (" Dealer have: "+ str(dealer_hand_1) +", "+str(dealer_hand_2)+", "+str(dealer_hand_3) + " and "+str(dealer_hand_4) +" on hand")
            elif dealer_card_counter==5:
                print (" Dealer have: "+ str(dealer_hand_1) +", "+str(dealer_hand_2)+", "+str(dealer_hand_3) + ", "+str(dealer_hand_4)+" and "+ str(dealer_hand_5) + " on hand")
            elif dealer_card_counter==6:
                print (" Dealer have: "+ str(dealer_hand_1) +", "+str(dealer_hand_2)+", "+str(dealer_hand_3) + ", "+str(dealer_hand_4)+", "+ str(dealer_hand_5)+" and " +str(dealer_hand_6)+" on hand")
            print (" Dealer Win with: " + str(dealer_total))
            print (" " +str(player_name)+ " have Total: "+ str(player_total)+ " Card")
            choice = str(input(" To quite press q/Q. To Proceed press p/P: "))
            print ()
            if choice in player_quite:
                break
            if choice in player_proceed:
                continue
        #Black Jack Win
        if 21 == dealer_total > player_total or player_total > 21 == dealer_total:
            lose_condition="1"
            win_condition="2"
            if "1" in win_condition:
                bet_win=(bet*2)
            if "1" in lose_condition:
                bet_win=0
            money=(balance+bet_win)
            if dealer_card_counter==2:
                print (" Dealer have: "+ str(dealer_hand_1) +" and "+str(dealer_hand_2) +" on hand")
            if dealer_card_counter==3:
                print (" Dealer have: "+ str(dealer_hand_1) +", "+str(dealer_hand_2)+" and "+str(dealer_hand_3) +" on hand")
            elif dealer_card_counter==4:
                print (" Dealer have: "+ str(dealer_hand_1) +", "+str(dealer_hand_2)+", "+str(dealer_hand_3) + " and "+str(dealer_hand_4) +" on hand")
            elif dealer_card_counter==5:
                print (" Dealer have: "+ str(dealer_hand_1) +", "+str(dealer_hand_2)+", "+str(dealer_hand_3) + " and "+str(dealer_hand_4)+" and "+ str(dealer_hand_5) + " on hand")
            elif dealer_card_counter==6:
                print (" Dealer have: "+ str(dealer_hand_1) +", "+str(dealer_hand_2)+", "+str(dealer_hand_3) + " and "+str(dealer_hand_4)+" and "+ str(dealer_hand_5) +str(dealer_hand_6)+" on hand")
            print (" Black Jack! Dealer Win with: " + str(dealer_total))
            print (" " +str(player_name)+ " have Total: "+ str(player_total)+ " Card")
            choice = str(input(" To quite press q/Q. To Proceed press p/P: "))
            print ()
            if choice in player_quite:
                break
            if choice in player_proceed:
                continue
        choice = str(input(" To quite press q/Q. To Proceed press p/P: "))
        print ()
        if choice in player_quite:
            break
        if choice in player_proceed:
            continue
    #Ending game 
    print(" You are out of Cash!")
    choice = str(input(" To quite press q/Q. To Start New Game press p/P: "))
    print (" ")
    if choice in player_quite:
        break
    if choice in player_proceed:
        continue 