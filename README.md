# CS340_client-server

(The following is taken from my Final Exam which documents how the program works and whose explanations were accompanied by pictures not seen here)

A RESTful API and User Documentation for a Financial Service

As a newly hired software developer for a startup business, my job is to assess the company’s needs and design and implement a stock market information service which is easily understood, accessible and flexible.  For this reason, I’ve chosen to implement a RESTful application interface (API) architectural style. REST stands for representational state transfer which is a highly accessible design that takes advantage of existing protocols, particularly HTTP. 
Additionally, I’ve chosen to use a distributed database (NoSQL/non-relational) called MongoDB since the company has professed to have future goals for securities other than company stock and also because of its driver API’s versatility in various languages. For this project I’ve chosen Python, version 2.7.6.  The RESTful API is a part of popular application server frameworks; thus developers only need to test and code uniform resource identifiers (URI’s) and locators (URLs) which are paths that allow for high level functionality using an HTTP connection. For the project we will use client side URL’s or CURLS.

Collection Management

The first step in collection management is to create a database using the Mongo import tool. Here I create a database which holds collections of data. Note that we can have more than one collection in our database. Here I’ve taken the data provided me by the company and inserted it into an active directory named ‘datasets’ with a database named ‘market’ with a collection named ‘stocks’. The terminal then confirms that 6,756 objects (documents) were successfully imported. Each document stores a set of data for a particular company. 
 
After assessing the data and the functionality I would like to implement, I decided to create several indexes for the database which will take advantage of what a distributed database is capable of. Traditional SQL relational databases hold your data in a table with rows and columns which require you to perform table-scans to store, retrieve, update, and delete the data within. Table scans require you to search the entire database which becomes tedious and slow as your database grows. 
A NoSQL distributed database uses rows only. This ability allows you to index fields so that when searches are performed on the indexed field, only that field is looked at (by using a pointer). This option will yield higher performance and efficiency as your database grows. For example, say you have ten thousand documents. Indexed fields have the power to limit a search of the entire database by more than one factor so that, for example, only twenty documents are accessed when doing a search- rather than the entire database. Indexes are not for all situations. Consider carefully whether you need access to a few, or all documents to perform some function.
For example, a typical query (table scan) on the stocks collection for industries titled “Medical Laboratories & Research” takes an average of 8 milliseconds. This number will grow as your collection does.  

After an index was created for the key field “Industries” this search now only takes under one millisecond. Therefore, MongoDB was a great choice for this industry, as the database promises to grow rather large due to its founder’s aspirations. 

This type of index only indexes one field, but you can index as many fields as you like. I made several more single-field indexes to assist in the efficiency of programs which will be described later. Here I make a “Sector” index. Note that you can give the indexes unique names (otherwise the names defaults to “NAME_1”). Also note that the ‘1’ is ascending, you can also use -1 for descending indexes. 
 
The field ‘ticker’ is an acronym for company names in the collection. I decided to make the field “Ticker” a unique index. What this does is ensure that no duplicate ‘tickers’ can be added to the database, much like a unique id. Currently when a new document is created it’s given an id automatically, but this doesn’t ensure that it’s1/ unique, as every id created like this is unique in itself. Thus making the ‘ticker’ unique ensures not only that duplicates can’t be made, but that creates, reads, updates and deletes (CRUD functionality) that rely on the ‘ticker’ id do not become dysfunctional or irrelevant due to duplicate documents. Updates, for example, might only work on one document- making feedback to the user possibly flawed. Note that I tried to give this index a ‘name’ of my creation, but it did not work. Programming is a continuous learning experience and I learned here that unique indexes cannot be named. 
 
Lastly, I created a compound index for a program I made which can find a document that matches a user defined industry and returns a list of ticker symbols (later described). A compound index will index more than one field. Now we can limit the search of the entire database (6,756 documents) by more than one factor, selecting first only the matching user’s industry, and then selecting only the ticker fields of those industries to present to the user with no need to scan the entire document for the tickers. 

Document Manipulation

Now on to the fun stuff. The following programs were designed to be modular, or in other words, reusable as well as improvable. They are reusable in that entries can be inputted by users in real-time, they do not contain hard-coded user options. These program’s abilities are only limited by the imagination. In any of the programs you could add or remove key fields (meaning the first entry in a document’s listing- which are all presented as key/values and their possible subdocument key/values and which we can also reach onto using MongoDB), and any of these key fields could be a user defined entry. In this way, the possibility for improvements, or more complex reads, writes, and other database manipulations are endless.
 
An example of only 3 of the 66 possible key/values available in each document
These following programs are non-web framework based, in that they do not use the REST API (but they easily could). These programs could work internally in the organization. 
This program takes user defined input and creates a new document to add to the ‘stocks’ collection in the ‘market’ database. When the program executes, it will ask the user to enter data in the form {“key” : “value”} with the entries separated by commas. This data could be copy pasted or it could also be formatted, using a program, previous to entry. 
 When the document is created successfully, we get the result “Document created! True”. The following entry was one fabricated by me and can easily be removed using the delete program.
 
Another way to check the for the successful creation of a program is to search for it in the actual database by doing a query “db.stocks.find ({“Ticker” : “JK”})
 
If there is already an entry ‘ticker’ with the acronym “JK” we get a duplicate error:
 
Finally, if the user enters invalid input, we get an error that the document has a bad format: 
This next program will accept a user defined ‘ticker’ to find a file, and update the ‘volume’ key with a new user defined value.

The prompt’s requests and entries result in a “Document updated!” result as well as showing the MongoDB result: “nModified 1”. If this said zero, the document wouldn’t have been changed.

The database shows that the modification was successful.
Additionally, this program will notice if the file was already modified and inform the user of that. (note that ‘nModified’ is now zero). 

This program has two more abilities, it can insert new data into the file if the key is a new key: 
 
The program can also inform the user that the file they wish to update could not be found.


This is the deletion program which deletes user defined files by requesting the ticker the user would like to delete, to be entered in a specific format, (as always).
 

If the program is successfully deleted, the user will be informed. They will also be informed if the requested ‘ticker’ wasn’t found.
 
The user will also be told if their formatting was bad.
 
Document Retrieval

The following program is a good example of a program that did not require an index, because it needed to scan the entire collection to capably carry out its work. This program reads from files and presents data to the user. Specifically, it takes a high and low user-defined number and returns to the user a count of all “50-Day Simple Moving Average” results that are between the high and low number.
 
Additionally, the program informs the user if their entry was wrongly formatted.

This program will take a user defined string, such as “Medical Laboratories & Research” and search all industries for this string, returning a list of ‘ticker’ symbols for matching industries.
 
This program uses the compound index for industries and tickers. 

The program also informs the user if their entry was wrongly formatted:
 
Additionally, the program will inform the user if no result matching the criteria was found:

Finally, the last query is a bit more complex than the last two, as it uses an aggregated pipeline which typically modifies or adds to the query before performing the next command. For example, this aggregation first matches the first criteria, ‘sector’ which is provided by the user. Then it  groups the results by ‘Industry’ with a summation of the industries ‘outstanding shares’ value. 

The results of said aggregation. Note that the code needs to be more beautified for easier readability. I felt this was a job for version 2.0 as functionality comes first- then beautification.

This program also considers if there is no such industry for the users input, and whether the input was wrongly formatted when it was entered:
 
 
Now we come to making a REST API. First we develop a web-based service application in order to implement a RESTful application programming interface for the MongoDB database. I’ve named the API ‘myrestapi’ and given it a place in the home directory.  Next, I switch to the directory and I import a ‘rest_server’ file to test out the API’s functionality.  
I noticed the ‘rest_server’ file wasn’t an executable so I went ahead and gave it some permissions (turning it green where before it was white) This probably doesn’t matter but I learned from using Linux that it’s a good practice. 
 
After assuring my programs are executable, I test out the rest_server file and get a positive server response after using the CURLS (client side URL’s) on the client side: 
 
This time the curls provide the user input. As you can see, the curl in the client above says within it “name=Robert” or “name=Jessica” . The program is designed to output a ‘return’ to the client with some “Hello world” code if the greeting doesn’t have a request for the name, or print out “Hello <name>” if there is a request for the name. We extract these names using our program which is designed to extract the request and print it in a preformatted string, otherwise the program aborts.
 
Next I enable some CRUD functionality, starting with file creation. Here I design a program that creates new documents for a ticker symbol using data provided by a curl request with a POST http action.

…  (it’s a long document, 66 lines of key/values)
 
Remember when tickers are duplicate inserts an error is returned.
 
The document is created using a CURL provided by the client which contains a stream of information that the client entered. We enter this URL into the client side and the file will be created or rejected. Again, later this clunky feedback can be beautified for legibility.
 
When the document is successfully created, we get a “Document created! True” reply on the server side and a return code of ‘200’ meaning that the creating was successful. 
  
Otherwise we get a duplicate error or write concern error.
The next program allows the user to update the value in the ‘volume’ key in for document of their choosing. First it takes from the curl the users document they would like to modify, and then it gets the value for ‘volume’ provided by the curl.  

If the query exists and was modified, we get a “Document Updated!” reply. If the query exist and the document was not modified, we get a “File has already been modified” reply, otherwise the query couldn’t find the document.  The program also has the ability to return MongoDB errors. Note that we could make ‘volume’ a user specified field and update anything we like.

Next, we have delete functionality, that takes a user curl and extracts the ticker name for the file they want deleted. If the deletion is successful, the document is removed. Otherwise it’s likely the document wasn’t found because it doesn’t exist, and we get an error message. 
 
Next we have simple’ read’ functionality which will query the given file.. The user enters a ticker to read a file by the ticker name, and their results are returned.  
Here the file is read, and then I delete the file, to show that next time we read we get an error that there was “No File Found With That Criteria”.

The limits of what’s possible with the REST API and MongoDB are that of user imagination. I would highly recommend that your knowledgeable stock experts communicate their ideas about what they would like to see implemented into the system. For now, I have a few mock example queries they can study to get some ideas about what’s possible.  
First is a simple query that selects and presents specific stock summary information from a user-derived list of ticker symbols. In this query we create a stock report for the list of user ticker symbols using the data provided by the request in the curl.
 
Note that the in curl there is an array of tickers within it: {“array” : [“AA”, “BA”, “T”]}. Execution prints a big block of code that we can beautify into whatever look you may want.
 
For now, what we care about is that the query was successful. And it was, which is indicated by the ‘200’ code at the end.

Finally, we perform an aggregation, the most complex query of all, but also the most powerful. The aggregation program extracts a company name from a curl, and inserts it into an aggregation pipeline type of search. This aggregation searches the collection and reports a portfolio on the top five shares (given some criteria to look for), first using a user-defined industry to conduct the search. We match this industry (for which we have an index) and group the top “max” companies by several factors. Researching a little on stocks I decided to go with ‘relative strength index’ and the highest 200-Day Simple Moving Average (SMA). Then these companies are sorted by their highest strength index. The ‘regex’ code looks within the given names for industries and conducts searches for single words. For example, here we search for “Telecom”, a word which can only be found embedded within a given industry’s name.
 
MongoDB will return an error if there was something wrong with the aggregation query. 
 
If no files where found that match the industry given, the program will return an error. 
 
Given the right feedback from some knowledgeable stock market peers, I’m sure these reports could increase in quality, quantity and pay for themselves ten times over- proving to be a great addition as well as an asset to your business. 
