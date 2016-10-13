#! /usr/bin/env python
from Jarvis import Morse
import RPi.GPIO
import time

PIN = 2 # The GPIO Pin you want to use, really. I like 2. 2 is a good number. Be like 2.
WAIT = 0.3 # Wait time between beeps
DAH_WAIT = 0.9 # Wait time between dashes

gpio = RPi.GPIO
gpio.setmode(gpio.BCM)
gpio.setup(PIN, gpio.OUT)


def speak(morse_list):
	for dit in morse_list:
		if dit == 1:
			gpio.output(PIN, True) # True or gpio.HIGH. Whatevs.
			time.sleep(WAIT)
			gpio.output(PIN, False)
			time.sleep(WAIT) # pause between letters
		else:
			gpio.output(PIN, True) # or gpio.LOW
			time.sleep(DAH_WAIT)
			gpio.output(PIN, False)
			time.sleep(WAIT) # pause between letters

def wordPause():
	time.sleep(DAH_WAIT*2 + WAIT)

def letterPause():
	time.sleep(WAIT*3)

def cleanup():
	gpio.cleanup()

if __name__ == "__main__":
	#str.upper, since I lazily defined the chars as  only capital letters
	text = str.upper(raw_input('Enter your sentence (A-Z only): '))

	#break it into words
	tokenized_text = text.split()
	m_tokenized_text = list()
	for word in tokenized_text:
		morse_builder = list()
		for char in word:
			morse_builder.append(Morse.Alphabet[char])
		m_tokenized_text.append(morse_builder)

	#m_tokenized_text is now a list of morse code words
	

	for word in m_tokenized_text:
		for letter in word:
			print letter
			speak(letter)
			letterPause()
		wordPause()
	cleanup()

