#!/usr/bin/python2.7

sentence = raw_input("Sentence:")

screen_with = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_with - box_width) // 2

print
print ' ' * left_margin + "+" + '-' * box_width + '+'
print ' ' * left_margin + '|' + ' ' * box_width + '|'
print ' ' * left_margin + '|' + ' ' * ((box_width - text_width) // 2) + sentence + ' ' * ((box_width - text_width) // 2) + '|'
print ' ' * left_margin + '|' + ' ' * box_width + '|'
print ' ' * left_margin + "+" + '-' * box_width + '+'

print "over"

print "ss"

print "123"