height = int(input("Enter height of the wall:"))
width = int(input("Enter width of the wall:"))
coverage = 5



def get_area_coverage(height, width, coverage):
     no_of_cans = (height * width) / coverage
     print(f"No of cans required are {round(no_of_cans)}")


get_area_coverage(height=height, width=width,coverage=coverage)