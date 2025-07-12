# importing dependencies
from typing import List

# This class handles getting the numbers and creating the sorted list
class CreateNumbersList:
            
    # This method reads the content of a text file
    def read_txt_file(self, file_name: str) -> str:
        try:
            # Opening the text file
            with open(file_name, "r") as file:
                # reading content from text file
                file_content: str = file.read()
                # removing \n from the content read from the file
                file_content: str = file_content.replace('\n', ',')
            # closing the text file
            file.close()
            return file_content
        except FileNotFoundError as err:
            print(err)
    
    # This method formats the file content as a sorted list
    def create_sorted_list(self, file_content: str) -> List:
        # converting string to a list
        file_content: List = file_content.split(",")
        # Converting items in list to int using map and converting it back to a list
        file_content: List = list(map(int, file_content))
        # Sorting the list
        file_content.sort()
        # Reversing the sorted list
        file_content.reverse()
        return file_content
