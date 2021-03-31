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

class Person():
    def __init__(self, firstname, surname, gender):
        self.fname = firstname
        self.sname = surname
        self.gender = gender # 'm' or 'f' or '?'
    
    @property
    def username(self, ):
        fname = self.fname.replace(' ','') #remove spaces
        return (fname + self.sname[0]).lower() #full fname + 1st in lastname
        #return (fname[:3].replace(' ','') + self.sname[:3]).lower() #3 first in fname + 3 first in sname
    
    @property
    def name(self):
        return f'{self.fname} {self.sname}'

    def __repr__(self):
        return f'({self.gender}): {self.fname} {self.sname} -> {self.username} ({len(self.username)})'

def rand_person():
    fname = random.choice(fn_all)
    surname = random.choice(surnames)
    if fname in fn_male: gender = 'm'
    elif fname in fn_female: gender = 'f'
    else: gender = '?'

    return Person(fname, surname, gender=gender)

def n_rand_people(n=100):
    return [rand_person() for n in range(n)]

def export_csv():
    with open('names.csv','w') as f:
        f.write(f'gender,username,firstname,surname\n')
        for p in n_rand_people():
            f.write(f'{p.gender},{p.username},{p.fname},{p.sname}\n')

def main():
    export_csv()

if __name__ == '__main__':
    main()





