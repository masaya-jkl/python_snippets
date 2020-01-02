# -*- coding: utf-8 -*-
"""
Image-in-image Steganography with PIL

https://en.wikipedia.org/wiki/Steganography#Techniques
in the Digital messages subsection:

"The hidden image is revealed by removing all but the two least significant 
bits of each color component and a subsequent normalization."

Create Image objects with PIL.Image.open(filepath or fileobject) or another factory method,
then pass them to encode_message or extract_message. "lsb" stands for "least significant bit(s)",
that parameter is meant to receive the value of bits in which the message is supposed to be en/decoded
with. Use PIL.Image.save to save the result later.

Note: both images need to have the same mode (grayscale, rgb, rgba, palette...), convert one of them
if necessary.

Extra: I recommend using a console/IDE which supports visualizing the images in-line. It's very handy.
However, you can also just visualize the images as tempfiles opened with the default image viewer
with PIL.Image.show()

Created on Tue Dec 31 18:51:01 2019

@author: masaya-jkl
"""

import PIL, PIL.ImageChops #, PIL.ImageDraw, PIL.ImageFont
# import functools, itertools, operator
# import io

def clear_lsb(image, bits):
    '''Clears least significant bits from image
    '''
    
    # return image.point(lambda n: n if n > ((1 << bits) - 1) else 0)
    # return image.point(lambda n: n & (~((1 << bits) - 1)))
    return image.point(lambda n: n >> bits << bits) # fastest

def get_lsb(image, bits):
    '''Gets least significant bits from image
    '''
    
    # return image.point(lambda n: n if n <= ((1 << bits) - 1) else 0)
    return image.point(lambda n: n & ((1 << bits) - 1))

def normalize(image, sbits, rbits=8):
    '''Not a true normalizer, it only shifts the bits around.
    
    The problem are the zeroes that are left when shifting left, or
    the values that are destroyed when shifting right
    '''
    if rbits > sbits:
        shift = rbits - sbits
        lut = lambda n: n << shift
        # lut = lambda n: (n << shift) + ((1 << shift - 1) - 1)
    else:
        shift = sbits - rbits
        lut = lambda n: n >> shift
        
    return image.point(lut)

def _normalize(n, d1, d2):
    '''n: input, d1: current size, d2: next size
    '''
    
    ratio = d2/d1
    return n * ratio
    

# use the *_bits function to encode and decode binary secret files
def get_lsb_bits(image, bits):
    raise NotImplementedError
    pass

def put_lsb_bits(image, bits, buffer):
    raise NotImplementedError
    pass

def encode_message(cover, message, lsb, bits=8):
    '''cover -> Image, message -> Image, lsb -> int, bits -> int
    
    Encodes the message image in the least significant bits of the cover image
    '''
    
    layers = [clear_lsb(cover, lsb),
              normalize(message, bits, lsb)]
    
    return PIL.ImageChops.add_modulo(*layers)

def extract_message(image, lsb, bits=8):
    return normalize(get_lsb(image, lsb), lsb, bits)
