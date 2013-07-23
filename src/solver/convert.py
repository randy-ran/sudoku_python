# GeneralConverver class: auxiliar class that helps to return the desire input
#                         for the required classes.
# Author: Oscar Walker Tapia Merida - oscar.tapia@jalasoft.com
# Automation Class (Sudoku project) - 2013

import collections
from readfiles import *

class GeneralConverter:
    def __init__(self):
        pass
        
    def convert_txt_file_to_string(self,txt_file):
        """ Convert a txt file into a string """
        txtreader = SudokuFileReader(txt_file)
        buffertxt = txtreader.reading_txt()
        if(txtreader.validate_size_txt()==81 and txtreader.validate_values_txt()):
            string = ''
            for x in buffertxt:
                if(x != '\n'):string += x
            return string
        else:
            print "Please insert a txt file with the correct dimensions"
            return "Please insert a txt file with the correct dimensions"

    def convert_csv_file_to_string(self,csv_file):
        """ Convert a csv file into a string """
        csvreader = SudokuFileReader(csv_file)
        buffercsv = csvreader.reading_csv()
        if(csvreader.validate_size_csv()==81 and csvreader.validate_values_csv()):
            string = ''
            for i in buffercsv:
                for j in i:
                    string += j
            return string
        else:
            print "Please insert a csv file with the correct dimensions"
            return "Please insert a csv file with the correct dimensions"


    def convert_dictionary_to_string(self,dictionary):
        """ Order and convert a dictionary into a string """
        ordered = collections.OrderedDict(sorted(dictionary.items()))
        string = ''
        for k, v in ordered.iteritems():
            string += v
        return string

    def convert_txt_file_to_matrix(self,txt_file):
        """ Convert a txt file to a matrix of integers """
        txtreader = SudokuFileReader(txt_file)
        buffertxt = txtreader.reading_txt()
        M=[]
        for i in range(9):
            M.append([0]*9)
        i = 0
        j = 0
        try:
            for x in buffertxt:
                if(x != '\n'):
                    M[i][j] = int(x)
                    j += 1
                    if(j == 9):
                        i += 1
                        j = 0
        except IndexError:
            print "PLEASE INSERT A 9x9 MATRIZ in a TXT file"
            return False
        return M

    def convert_matrix_to_string(self,matrix):
        """ Convert a matrix to a string  """
        string = ''
        for i in matrix:
            for j in i:
                string += str(j)
        return string

    def convert_string_to_matrix(self, string):
        """ Convert a string to a matrix"""
        M=[]
        for i in range(9):
            M.append([0]*9)
        i = 0
        j = 0
        try:
            for x in string:
                M[i][j] = str(x)
                j += 1
                if(j == 9):
                    i += 1
                    j = 0
        except IndexError:
            print "PLEASE INSERT A 9x9 MATRIZ in a TXT file"
            return False
        return M

    def convert_string_to_matrix_int(self, string):
        """ Convert a string to a matrix"""
        M=[]
        for i in range(9):
            M.append([0]*9)
        i = 0
        j = 0
        try:
            for x in string:
                M[i][j] = int(x)
                j += 1
                if(j == 9):
                    i += 1
                    j = 0
        except IndexError:
            print "PLEASE INSERT A 9x9 MATRIZ in a TXT file"
            return False
        return M

    def convert_matrix_to_dict(self,matrix):
        self.digits   = '123456789'
        self.rows     = 'ABCDEFGHI'
        self.cols     = self.digits
        self.squares  = self.cross(self.rows, self.cols)
        dictionary = {}
        #print self.squares
        for x in self.squares:
            dictionary[x] = x
        ordered = collections.OrderedDict(sorted(dictionary.items()))
        #print ordered
        dicti = {}
        i = 0
        j = 0
        for x in ordered:
            #print str(i) +'  '+str(j)
            dicti[x] = str(matrix[i][j])
            #print dicti
            j += 1
            if(j==9):
                #print 'nivel 1'
                i += 1
                j = 0
            #if(i == 9):
             #   return
        return dicti
        #ordered = collections.OrderedDict(sorted(dicti.items()))
        #print ordered
            
    def matrixreader(self,matrix,i,j):
        for i in matrix:
            for j in i:
         #       print type(j)
                return j




            #dicti[x] = x
        #print ordered

        #print dictionary
        #print ordered
        #print dictionary.values()

    def cross(self, A, B):
        "Cross product of elements in A and elements in B."
        return [a+b for a in A for b in B]

default_matrx= \
        [[0,0,3,0,2,0,6,0,0],\
        [0,9,0,3,0,5,0,0,1],\
        [0,0,1,8,0,6,4,0,0],\
        [0,0,8,1,0,2,9,0,0],\
        [7,0,0,0,0,0,0,0,8],\
        [0,0,6,7,0,8,2,0,0],\
        [0,0,2,6,0,9,5,0,0],\
        [8,0,0,2,0,3,0,0,9],\
        [0,0,5,0,1,0,3,0,0]]
con = GeneralConverter()
con.convert_matrix_to_dict(default_matrx)
#a = con.convert_string_to_matrix('483921657967345821251876493548132976729564138136798245372689514814253769695417382')
#print a