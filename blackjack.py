import random

try:
	import tkinter
except ImportError:
	import Tkinter as tkinter

mainWindow = tkinter.Tk()

# Function that create all cards from images
def load_images(card_images):
	suits = ['heart', 'club', 'diamond', 'spade']
	face_cards = ['jack', 'queen', 'king']

	if tkinter.TkVersion >= 8.6:
		extension = 'png'
	else:
		extension = 'ppm'

	# for each suit, retrieve the image for the cards
	for suit in suits:
		# first the number cards 1 to 10
		for card in range(1, 11):
			name = 'cards\{}_{}.{}'.format(str(card), suit, extension)
			image = tkinter.PhotoImage(file=name)
			card_images.append((card, image,))

		# next the face cards
		for card in face_cards:
			name = 'cards\{}_{}.{}'.format(str(card), suit, extension)
			image = tkinter.PhotoImage(file=name)
			card_images.append((10, image,))


# Deal card function
def deal_card(frame):
	next_card = deck.pop()
	tkinter.Label(frame, image=next_card[1], relief="raised").pack(side="left")
	return next_card

# Deal function for dealer (assigned to button)
def deal_dealer():
	deal_card(dealer_card_frame)

# Deal function for player (assigned to button)
def deal_player():
	deal_card(player_card_frame)


mainWindow.title("Black Jack")
mainWindow.geometry("640x480")

resultText = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=resultText)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# Embedded frame for cards
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(column=0, row=3)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky="ew")

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer )
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command=deal_player )
player_button.grid(row=0, column=1)

cards = []
load_images(cards)
print(cards)

# Create a new deck of cards and shuffle them
deck = list(cards)
random.shuffle(deck)

#Create empty dealer and player hands (no cards on the begining
dealer_hand = []
player_hand = []

mainWindow.mainloop()
