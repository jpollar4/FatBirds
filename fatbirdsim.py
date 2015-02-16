import sys
import math;
import random




def shuffledeck(seedsplayed):

	seed = 20 - seedsplayed;
	peck = 10;
	squawk = 10;
	plummage = 10;
	deck = [];

	for i in range(0,seed):
		deck.append("seed");

	for i in range(0,peck):
		deck.append("peck");

	for i in range(0,squawk):
		deck.append("squawk");

	for i in range(0,plummage):
		deck.append("plummage");

	random.shuffle(deck);
	#print "seed count: " + str(deck.count("seed"));
	return deck;


def gameloop(numplayers):

	cards = [];
	
	players = [];
	seedsplayed = 0;
	handsize = 3;

	nturn=0
	cards = shuffledeck(0);
	for p in range(0,numplayers):
		players.append(dict({"cards": [], "score": 3}));

	#starting hand 3
	for i in range(0,handsize):
		for p in players:
			p['cards'].append(cards.pop());

	#play one draw one
	while(True):
		nturn+=1;
		#print "";
		#print "";
		#print "TURN NUMBER" + str(nturn);
		for p in players:

			while(p['cards'].__len__() < handsize):
				if(cards.__len__() <= 0):
					cards = shuffledeck(seedsplayed);
				p['cards'].append(cards.pop());

			#print "";
			#print "";
			#print "MY turn! player" + str(players.index(p));
			random.shuffle(p['cards']);
			cardplayed = p['cards'].pop();
			if(cardplayed == "squawk" and p['cards'].count("plummage") >= 1):
				p['cards'].remove("plummage");
				p['cards'].append("squawk");
				cardplayed = "peck";			
			elif(cardplayed == "squawk" and p['cards'].count("peck") >= 1):
				p['cards'].remove("peck");
				p['cards'].append("squawk");
				cardplayed = "peck";
			elif(cardplayed == "squawk" and p['cards'].count("seed") >= 1):
				p['cards'].remove("seed");
				p['cards'].append("squawk");
				cardplayed = "seed";
			else:
				if(cards.__len__() <= 0):
					cards = shuffledeck(seedsplayed);
				p['cards'].append(cards.pop());


			if(cardplayed == "seed"):
				p['score']+=1;
				seedsplayed+=1;

			if(cardplayed == "plummage"):
				for x in players:
					if(p!=x and x['score']>=1):
						p['score']+=1;
						x['score']-=1;
			if(cardplayed == "peck"):
				playertotarget=None;
				highscore=0;
				for x in players:
					if(p!=x and x['score']>highscore):
						playertotarget = x;
						highscore = x['score'];
				if(highscore > 0):
					if(playertotarget['cards'].count("squawk") >= 1):
						playertotarget['cards'].remove("squawk");
					else:
						stolen = min(math.floor(highscore/2),1);
						p['score']+=stolen;
						playertotarget['score']-=stolen;



			#print "I played: " + str(cardplayed);
			#print "My Score: " + str(p['score']);

			if p['score'] >=10:
				#print "I win!! player" + str(players.index(p));
				return dict({"winner": str(players.index(p)), "turns": nturn});
					

if __name__ == '__main__':

	numplayers = 4;
	games = 1000;
	totalturns=0;
	winners = [];

	for i in range(1,games):
		gamedata = gameloop(numplayers);
		totalturns += gamedata["turns"];
		winners.append(gamedata["winner"]);


	print "average turns = " + str((totalturns/games));

	for i in range(0,numplayers):
		print "player " + str(i) + " wins: " + str(winners.count(str(i)));




	
	






