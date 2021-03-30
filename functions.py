from names import etternavn, jenter, gutter, dobbel_g, dobbel_j
from names import norrøne_fornavn, norrøne_kvinnenavn
import random
from varinfo import *

fn_male = [] # all male firstnames
fn_male += [g for g in gutter] #892
fn_male += [g for g in dobbel_g] #50

fn_female = [] # all female firstnames
fn_female += [j for j in jenter] #960
fn_female += [j for j in dobbel_j] #50
fn_female += [j for j in norrøne_kvinnenavn] #983

fn_both_genders = [n for n in norrøne_fornavn] #98

fn_all = fn_male + fn_female + fn_both_genders #3033
surnames = etternavn #1460


#fnavn_nor_jente = [n for n in fnavn_begge if n in norrøne_kvinnenavn] #28 ???
#fnavn_nor_gutt = [n for n in fnavn_begge if n not in norrøne_kvinnenavn] #70 ???

class Name():
    def __init__(self, firstname, surname):
        self.fname = firstname
        self.sname = surname
    
    username_policies = [
        'fullfname', #full first name + first char last
        '3first3last', #3 first from fname, 3 first from last
    ]

    def un_policy_fullfname(fname,lname):
        return f'{fname[:3]}{lname[-3:]}'

    def un_policy_3first3last(fname,lname):
        return f'{fname}{lname[0]}'
    

    def username(self, policy='fullfname'):
        return getattr(self,policy(self.fname,self.sname))



def rand_fullname():
    return f'{random.choice(fn_all)} {random.choice(surnames)}'


def n_rand_fullnames(n=10):
    names = []
    for i in range(n):
        pick = rand_fullname()
        names.append(pick)
    return names

print(n_rand_fullnames())

