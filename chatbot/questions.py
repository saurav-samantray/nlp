# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 18:58:49 2019

@author: Saurav Samantray
"""

pairs = [
   [
        r"where is my order (.*)?",
        ["Order %1 has been shipped and will reach you in 3 days",]
        
    ],
    [
        r"(.*) cancel (.*) order",
        ["Order cannot be cancelled now as it has already been shipped. Please try the refund/return option incase you are not satisfied with the product",]
        
    ],
    [
        r"(.*) (refund|return) ?",
        ['%2 initiated for your order',]
    ],
    [
        r"(.*)when (.*) (in stock|instock|available)?",
        ["Produt is expected to come in stock in about 2 weeks",]
    ],
]