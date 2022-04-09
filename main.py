#import request library
import requests

#import beautiful soup
from bs4 import BeautifulSoup

def request_github_trending(url):
	'''
		this function sends a get request
		to the website and get its reponse.

		parameters : 
			url : url of the website

		returns :
			reponse of the get request of the
			url.

	'''	

	#send a get request and get the response
	response = requests.get(url)

	#return the response
	return response

def extract(page):
	'''
		this function gets information of
		trending repos in the github.

		parameters : 
			page : 	response of the get request to the 
					github page

		returns :
			html code corresponding to all the rows 
			which are related to each repository.

	'''	

	#make a beautifulsoup object using the html of the page
	doc = BeautifulSoup(page.text, "html.parser")

	#getting all rows related to repositories
	repo_info = doc.find_all("article")

	#return repositories
	return repo_info

def transfrom(html_repos):
	'''
		this function makes a hash using repository
		information.

		parameters : 
			html_repos	:	html code related to repository information
							rows.

		returns :
			list of hash in the format of 
			{
				developer : "Developer",
				name of repository : "Name of repository",
				stars : "Stars"
			}

				related to all the repositories

	'''	

	#stores the repository list
	transfromed_repo_info = []

	#do this for all the repositories
	for i in range(len(html_repos)):

		#get a empty hash
		my_hash = {}

		#get the currennt repository
		curr_repo = html_repos[i]

		#get the developer of the current repo and add it to hash
		developer = curr_repo.find("h1").find("span").string.strip()
		developer = developer.replace(" /","")
		my_hash['deverloper'] = developer

		#get the name of the repo and add it to hash
		repo_name = curr_repo.find("h1").find_all("a")[0].text.split("/")[1]
		repo_name = repo_name.strip()
		my_hash['repository_name'] = repo_name

		#get the number of stars of the repo and add it to hash
		nbr_stars = curr_repo.find_all("div")[2].find("a").text
		nbr_stars = nbr_stars.strip()
		my_hash['nbr_stars'] = nbr_stars

		#append the current hash to the list
		transfromed_repo_info.append(my_hash)

	#return the list of repository hashes
	return transfromed_repo_info

def format(repositories_data):
	'''
		this function stores the repo infor in a
		file named trending_repositories.csv

		parameters : 
			repositories_data : 
				list of hashes related to repositories

		returns :
			nothing.
			(just making a .csv file)

	'''	

	#set the filename
	filename = "trending_repositories.csv"

	#open the file for writing
	file = open(filename,"w")

	#write the header in the file
	file.write("Developer,Repository Name,Number of Stars\n")

	#write all the repo info in the file
	for info in repositories_data:
		#stores content related to one row
		row = ""

		#get infor from the hash
		for key in info:
			row += str(info[key]) + ","
		
		#remove the last comma and add a new line
		row = row[:-1] + "\n"

		#write this row to the file
		file.write(row)

	#close the file
	file.close()

def main():

	#URL of the website
	URL = "https://github.com/trending"
	
	#get the response
	page = request_github_trending(URL)

	#get the html code related to repo rows
	repo_info = extract(page)

	#get the hash list related to repo rows
	transformed_repo_info = transfrom(repo_info)

	#write repo info in a .csv file
	format(transformed_repo_info) 

#call the main function
main()
