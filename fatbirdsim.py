import sys
import math;
import random




def shuffledeck():
	deck = [
		"seed",
		"seed",
		"seed",
		"seed",
		"seed",
		"peck",
		"squawk",
		"plummage",
		"seed",
		"seed",
		"seed",
		"seed",
		"seed",
		"peck",
		"squawk",
		"plummage",
		"seed",
		"seed",
		"seed",
		"seed",
		"seed",
		"peck",
		"squawk",
		"plummage",
		"seed",
		"seed",
		"seed",
		"seed",
		"seed",
		"peck",
		"squawk",
		"plummage",
		"seed",
		"seed",
		"seed",
		"seed",
		"seed",
		"peck",
		"squawk",
		"plummage",
	];
	random.shuffle(deck);
	return deck;


def gameloop():

	cards = [];
	numplayers = 4;
	players = [];

	nturn=0
	cards = shuffledeck();
	for p in range(0,numplayers):
		players.append(dict({"cards": [], "score": 0}));

	#starting hand 3
	for i in range(0,3):
		for p in players:
			p['cards'].append(cards.pop());

	for p in players:
		print str(p);	


	#play one draw one
	while(True):
		nturn+=1;
		print "";
		print "";
		print "TURN NUMBER" + str(nturn);
		for p in players:
			print "";
			print "";
			print "MY turn! player" + str(players.index(p));
			random.shuffle(p['cards']);
			cardplayed = p['cards'].pop();			

			if(cardplayed == "seed"):
				p['score']+=1;

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
					p['score']+=math.floor(highscore/2);
					playertotarget['score']-=math.floor(highscore/2);



			print "I played: " + str(cardplayed);
			print "My Score: " + str(p['score']);

			if p['score'] >=10:
				print "I win!! player" + str(players.index(p));
				return;



			if(cards.__len__() < 2):
				cards = shuffledeck();
			p['cards'].append(cards.pop());


if __name__ == '__main__':
	gameloop();


	
	






