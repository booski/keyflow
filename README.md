# keyflow.py - find words that flow across the keyboard

Given a file (or a pipe from stdin), prints all words in the input that 
can be written on a (Swedish qwerty) keyboard by moving from left to 
right, never repeating a keystroke.

Words that pass this test include awful, edgy, setup and thump.

Letters are considered in columns, so the progression is 
q, a, z, w, s, x...
