__author__ = 'andrew.sielen'

from bs4 import BeautifulSoup
from selenium import webdriver
import pprint as pp #just to make the output look pretty, isn't needed to actually make it work


def soupify(url):
    """
        I like to define this because rule number one of programming is never do something more than once
    """
    driver = webdriver.Firefox()
    driver.get(url)
    page = driver.page_source
    soup = BeautifulSoup(page)
    return soup


def parse_html_table(table_tags):
    """
        Tables in html are in the following format:
            <table> #attributes about the table are in this tag
                <tbody>
                    <tr>    #tr tags indicate a row
                        <td> </td>  #td tags indicate a cell in a row
                        <td> </td>
                    </tr>
                    <tr>
                        <td> </td>
                        <td> </td>
                    </tr>
                </tbody>
            </table>

        This would be a 2x2 table
    """
    table_body = table_tags.find("tbody")   #find the table body

    table_array = []    #initiate the array

    line_tags = table_body.findAll("tr")  #make a list of all the rows
    for k in line_tags:
        table_array.append(k.findAll("td")) #add a list of cells to the table array

    return table_array


def get_table_row(table,row):
    return table[row]

def get_table_column(table,column):
    """
        Given a 2D array, return a column from the array as a list
    """
    #This does the same thing as the lines commented out below
    return [row[column] for row in table]

    #column_list = []
    #for row in table:
    #    column_list.append(row[column])
    #
    #return column_list

def main():
    """
        This function is all just to show it works, nothing in here is an essential part of the process
    """

    #You can change this url to anything you want, it will return the first table on that url (and probably throw an error if there isn't one)
    url = "http://www.house.gov/representatives/" #"http://therealityprose.wordpress.com/2013/01/17/what_happened_with_lego/"
    soup = soupify(url)

    #Find the first table tag on the page
    parse_table = soup.find("table")

    table_array = parse_html_table(parse_table)

    #Print each row
    for r in range(0,len(table_array)):
        print("Row ", r)
        pp.pprint(get_table_row(table_array,r))

    print("")

    #Print each column
    for c in range(0,len(table_array[0])):
        print("Column ", c)
        pp.pprint(get_table_column(table_array,c))

main()